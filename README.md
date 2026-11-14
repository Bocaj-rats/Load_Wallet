# Cellphone Load Wallet (Python OOP)

A menu-driven Python program for managing prepaid load. It demonstrates **classes, objects, attributes, methods, encapsulation**, and input validation.

## Features
- Create a wallet using a name, 11-digit Philippine mobile number, network, and starting balance.
- Top up prepaid load.
- Send load to another number on the same network (no fee).
- Send load to a number on a different network (fixed **PHP 5.00** fee).
- Check wallet balance.
- Handle invalid menu choices, numbers, amounts, and insufficient load without crashing.

> **Note:** Networks are selected manually (Globe, Smart, or DITO). The project does not connect to telecom providers or send real mobile load; it simulates transactions by deducting the balance. The PHP 5.00 cross-network fee is an example for this school activity, not an official telco rate.

## Files
- `load_wallet.py` — `LoadWallet` class and wallet methods.
- `main.py` — interactive console menu and inputs.

## Run in VS Code
1. Install Python 3 and the Python extension in VS Code.
2. Open this folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Run:
   ```powershell
   python main.py
   ```
   If `python` is not recognized on Windows, install Python from https://www.python.org/downloads/ and select **Add python.exe to PATH**, then reopen VS Code. You can also try `py main.py` if the Python Launcher is available.

**Go Live is for websites (HTML/JS); it does not run this Python console program.**

## Example
```text
Owner          : AJ
Mobile Number  : 09123456789
Network        : Globe
Load Balance   : PHP 100.00
```

## GitHub Submission
1. Create a **public** GitHub repository named `cellphone-load-wallet`.
2. Upload `main.py`, `load_wallet.py`, and `README.md`.
3. Confirm all files appear in the repository.
4. Share the repository URL in your class submission form.
