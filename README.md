# Password Strength Checker

A beginner-friendly Python project that checks password length and character variety, flags a small set of common passwords and predictable patterns, and suggests improvements.

## Features
- Checks length, lowercase, uppercase, digits, and special characters.
- Classifies a password as Weak, Medium, or Strong using simple educational rules.
- Gives improvement suggestions.
- Hides password input in the terminal with Python's `getpass`.
- Does not save or transmit the password.

## Requirements
- Python 3.10 or newer. Uses only the Python standard library.

## Run on Windows
Open this folder in VS Code, select **Terminal → New Terminal**, and run:

```powershell
python password_checker.py
```

If `python` is not recognized, try `py password_checker.py`. Enter a made-up test password; it will not appear while typing.

## Run tests
```powershell
python -m unittest -v
```

## How it works
1. `getpass` reads input without echoing it to the terminal.
2. `analyze_password()` checks length and character groups.
3. It flags a small list of common passwords and simple predictable patterns.
4. Simple rules produce a Weak, Medium, or Strong label.
5. `print_report()` displays the results without printing the password.

## Limitations
- This is an educational heuristic, not a professional password audit.
- Character variety alone does not guarantee a password is difficult to guess.
- The common-password list is small and incomplete.
- The entropy figure is a rough estimate and can overstate the strength of predictable passwords.
- Use invented test passwords only, never real account passwords.

## Safe use
Run locally. Never share real passwords in screenshots, issues, or source control.
