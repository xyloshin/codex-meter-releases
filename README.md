# Codex Meter

**Your Codex allowance, at a glance.**

A small Mac menu-bar app for keeping track of your remaining allowance, reset time and extra credits. Open its window for usage history and alerts when your balance is running low.

**[Download for Mac](https://github.com/xyloshin/codex-meter-releases/releases/download/v2.2.0-beta.9/Codex-Meter-2.2.0-beta.9-macos-universal.zip)** · Beta 2.2.0-beta.9 · macOS 14+ · Apple Silicon & Intel

<p>
<img src="https://raw.githubusercontent.com/xyloshin/codex-meter-releases/main/assets/beta9-menu-tight.png" alt="In your Mac’s menu bar: normal, warning and low allowance, shown beside Wi-Fi and battery icons. Changes colour as your allowance runs low." width="600"><br>
<img src="https://raw.githubusercontent.com/xyloshin/codex-meter-releases/main/assets/beta8-allowance-reset-chart.png" alt="Allowance history with varied usage, exhaustion and a reset to 100%" width="337" height="238" align="top"><img src="https://raw.githubusercontent.com/xyloshin/codex-meter-releases/main/assets/beta9-usage-forecast-compact.png" alt="Remaining allowance, extra credits and forecast timeline before reset" width="263" height="238" align="top">
</p>

*Demo data. Click an image to see it larger.*

## What you get

- **A quick menu-bar reading:** remaining allowance and its reset date.
- **Allowance and extra credits:** separate balances, with purchased-credit usage shown when your allowance runs out.
- **History and alerts:** saved readings over 24 hours, 7 days and 30 days, plus low-balance and fast-usage warnings.
- **Built-in updates:** a Check for Updates command and signed update downloads.
- **Local history:** readings stay on your Mac. No separate analytics account or cloud history sync.

## Requirements

This beta bundles Node, so you do not need to install Node separately. A compatible Codex client signed in with your ChatGPT account is still required.

Beta 2.2.0-beta.9 is built for Apple Silicon and Intel with a macOS 14 minimum. In addition to local macOS 26 testing, the exact release passed automated download, Gatekeeper, bundled-runtime and native-startup checks on clean macOS 14.8.9 Apple Silicon and macOS 15.7.9 Intel runners. [Test results](https://github.com/xyloshin/codex-meter-releases/actions/runs/39235191489). Interactive use, signed-in usage on those older systems, and physical-device sleep/wake and notifications still need real-world testing.

## Downloads

Download the app ZIP from the [beta.9 release](https://github.com/xyloshin/codex-meter-releases/releases/tag/v2.2.0-beta.9), unzip it, and move **Codex Meter.app** to Applications. GitHub’s source-code archives contain only this downloads repository.

The app is signed and notarized by Apple. See [all releases](https://github.com/xyloshin/codex-meter-releases/releases) for release notes and downloads.

## Privacy and feedback

Codex handles sign-in. Meter does not store passwords or sign-in tokens and does not start AI tasks to check usage. Account identifiers and usage history are stored locally. Please remove account details from screenshots and do not upload saved history or credentials.

[Report a problem](https://github.com/xyloshin/codex-meter-releases/issues) with your macOS version, what you expected and what happened.

This repository contains the download page and update feed. The app’s source repository is private.

**Independent project, not affiliated with or endorsed by OpenAI.** This tracks Codex usage, not ordinary ChatGPT conversation limits or API billing. Alerts do not pause tasks or limit spending.
