# Codex Usage Meter

**Your Codex allowance, at a glance.**

A small Mac menu-bar app that shows your remaining allowance, reset time and extra credits. Open its window for usage history and low-balance alerts.

**[Download for Mac](https://github.com/xyloshin/codex-usage-meter/releases/download/v2.2.0-beta.9/Codex-Meter-2.2.0-beta.9-macos-universal.zip)** · Public beta · macOS 14+ · Apple Silicon & Intel

<p>
<img src="https://raw.githubusercontent.com/xyloshin/codex-usage-meter/main/assets/beta9-menu-tight.png" alt="In your Mac’s menu bar: normal, warning and low allowance, shown beside Wi-Fi and battery icons. Changes colour as your allowance runs low." width="600"><br>
<img src="https://raw.githubusercontent.com/xyloshin/codex-usage-meter/main/assets/beta8-allowance-reset-chart.png" alt="Allowance history with varied usage, exhaustion and a reset to 100%" width="337" height="238" align="top"><img src="https://raw.githubusercontent.com/xyloshin/codex-usage-meter/main/assets/beta9-usage-forecast-compact.png" alt="Remaining allowance, extra credits and forecast timeline before reset" width="263" height="238" align="top">
</p>

*Demo data. Click an image to see it larger.*

## What you get

- **Allowance and extra credits**, shown separately.
- **Usage history** over 24 hours, 7 days and 30 days.
- **Low-balance and fast-usage alerts**, plus built-in updates.
- **History kept on your Mac**, with no separate analytics account.

## Get started

Download the ZIP, unzip it, and move **Codex Meter.app** to Applications. You’ll need a compatible Codex client signed in with your ChatGPT account.

<details>
<summary>Compatibility and beta testing</summary>

Beta 2.2.0-beta.9 supports Apple Silicon and Intel, with a macOS 14 minimum. Node is bundled, so there’s nothing extra to install for that.

In addition to local macOS 26 testing, the exact release passed automated download, Gatekeeper, bundled-runtime and native-startup checks on clean macOS 14.8.9 Apple Silicon and macOS 15.7.9 Intel runners. [Test results](https://github.com/xyloshin/codex-usage-meter/actions/runs/39235191489).

Interactive use and signed-in usage on those older systems, plus physical-device sleep/wake and notifications, still need real-world testing.

The app is signed and notarized by Apple. Use the app ZIP rather than GitHub’s source-code archives, which contain only this downloads repository. See [all releases](https://github.com/xyloshin/codex-usage-meter/releases) for release notes and downloads.

</details>

<details>
<summary>Privacy and how it works</summary>

Codex handles sign-in. Meter does not store passwords or sign-in tokens and does not start AI tasks to check usage. Account identifiers and usage history stay on your Mac, with no cloud history sync.

Meter tracks Codex usage, not ordinary ChatGPT conversation limits or API billing. Purchased-credit usage is shown when your allowance runs out. Alerts do not pause tasks or limit spending.

Updates are available through Check for Updates, with signed downloads. This repository contains the download page and update feed; the app’s source repository is private.

</details>

[Report a problem](https://github.com/xyloshin/codex-usage-meter/issues) with your macOS version and what happened. Please leave out account details, saved history and credentials.

**Independent project, not affiliated with or endorsed by OpenAI.**
