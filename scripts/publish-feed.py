"""Publish only the feed attached to the owner's published release."""
import base64, json, os, pathlib, urllib.request, xml.etree.ElementTree as ET
repo = "xyloshin/codex-meter-releases"
event = json.loads(pathlib.Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
release = event["release"]
assert event["action"] == "published" and not release["draft"]
assert event["repository"]["full_name"] == repo
assets = {asset["name"]: asset for asset in release["assets"]}
url = assets["appcast.xml"]["browser_download_url"]
prefix = f"https://github.com/{repo}/releases/download/{release['tag_name']}/"
assert url == prefix + "appcast.xml"
with urllib.request.urlopen(url, timeout=30) as response:
    data = response.read(65537)
assert len(data) <= 65536
assert b"<!DOCTYPE" not in data and b"<!ENTITY" not in data
root = ET.fromstring(data)
ns = "{http://www.andymatuschak.org/xml-namespaces/sparkle}"
items = root.findall("./channel/item")
assert items, "Release feed has no updates"
versions = []
for item in items:
    versions.append(int(item.findtext(ns + "version")))
    enclosure = item.find("enclosure")
    target = enclosure.attrib["url"]
    assert target.startswith(prefix)
    name = target[len(prefix):]
    assert name in assets and assets[name]["browser_download_url"] == target
    assert int(enclosure.attrib["length"]) == assets[name]["size"]
    assert len(base64.b64decode(enclosure.attrib[ns + "edSignature"], validate=True)) == 64
# Never roll clients back when an older draft is published later.
existing = ET.parse("appcast.xml")
old = [int(i.findtext(ns + "version")) for i in existing.findall("./channel/item")]
assert not old or max(versions) >= max(old), "Refusing an older feed"
pathlib.Path("appcast.xml").write_bytes(data)
