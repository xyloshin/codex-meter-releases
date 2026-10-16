"""Smoke-test the exact beta.2 binary on disposable macOS CI machines.

No signing credentials, source checkout, Codex account or personal data required.
This checks runtime startup, not interactive UI or physical-device behavior.
"""
import hashlib
import json
import os
from pathlib import Path
import plistlib
import subprocess
import sys
import time

root = Path(sys.argv[1]).resolve()
archive = root / 'Codex-Meter-2.2.0-beta.2-macos-universal.zip'
expected = 'a0a22166021f26d069d2abe39348672f8dc6065e841c7929147d34e6eec9cfdd'
assert hashlib.sha256(archive.read_bytes()).hexdigest() == expected

def run(args, **kwargs):
    result = subprocess.run(args, check=True, text=True, capture_output=True, **kwargs)
    print(result.stdout.strip(), result.stderr.strip(), flush=True)
    return result.stdout.strip()

os_version = run(['/usr/bin/sw_vers', '-productVersion'])
arch = run(['/usr/bin/uname', '-m'])
run(['/usr/bin/ditto', '-x', '-k', str(archive), str(root / 'extracted')])
app = root / 'extracted/Codex Meter.app'
info = plistlib.loads((app / 'Contents/Info.plist').read_bytes())
assert info['CFBundleVersion'] == '2'
assert info['LSMinimumSystemVersion'] == '14.0'
run(['/usr/bin/codesign', '--verify', '--deep', '--strict', str(app)])
run(['/usr/bin/xcrun', 'stapler', 'validate', str(app)])
run(['/usr/sbin/spctl', '--assess', '--type', 'execute', '--verbose=2', str(app)])
node = app / 'Contents/MacOS/node'
env = dict(os.environ, PATH='/usr/bin:/bin:/usr/sbin:/sbin')
env.pop('NODE_OPTIONS', None)
env.pop('NODE_PATH', None)
node_version = run([str(node), '--version'], env=env)
reply = json.loads(run([str(node), str(app / 'Contents/Resources/poll.mjs'), str(root / 'empty-history'), '--cached'], env=env))
assert reply['ok'] and reply['cached'] and reply['accounts'] == []
# Native startup exercises linked frameworks, SwiftUI/AppKit and the bundled
# usage helper on an actual older OS. A clean runner has no Codex login.
log = root / 'native-startup.log'
with log.open('w') as output:
    process = subprocess.Popen([str(app / 'Contents/MacOS/CodexMeter')], stdout=output, stderr=output, env=env)
    try:
        time.sleep(15)
        assert process.poll() is None, 'Native app exited early: ' + log.read_text()[-6000:]
        run(['/bin/ps', '-p', str(process.pid), '-o', 'pid=,comm='])
    finally:
        if process.poll() is None:
            process.terminate()
            process.wait(timeout=15)
result = dict(macOS=os_version, architecture=arch, sha256=expected, node=node_version,
              signature=True, stapledTicket=True, gatekeeper=True, emptyHistory=True,
              nativeStartup15Seconds=True, interactiveUI=False, signedInUsage=False,
              physicalDeviceUserTest=False)
print(json.dumps(result, indent=2))
with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
    summary.write('## Exact release smoke test\n\n```json\n' + json.dumps(result, indent=2) + '\n```\n')
