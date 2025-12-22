 HEAD
# Password Policy Enforcer (Python)

This project is a simple password policy enforcement tool written in Python. It checks user-entered passwords against common security rules and logs failed attempts for security review.

## 🔐 Features
 Minimum password length enforcement
 Uppercase and lowercase character checks
 Numeric character requirement
 Special character validation
 Logs failed password attempts to a file

## 🧪 How It Works
1. The user enters a password.
2. The script validates the password against security rules.
3. If the password fails, feedback is provided.
4. Failed attempts are logged for monitoring purposes.

## 🛠 Tools & Technologies
 Python
 Linux (Kali / Ubuntu)
 Regular Expressions (Regex)
 File logging

## 📌 Why This Project Matters
Weak passwords are a common attack vector. This project demonstrates:
 Password security fundamentals
 Secure input validation
 Logging concepts used in SOC environments

 How to Run
 bash
python3 password_check.py

 Password Policy Enforcer

 Description
A Python script that checks password strength based on common security rules.

 Security Problem
Weak passwords allow attackers to gain unauthorized access through brute-force and credential-stuffing attacks.

 Rules Enforced
 Minimum length of 8 characters
 Uppercase letter
 Lowercase letter
 Number
 Special character

 Outcome
The script accepts strong passwords and rejects weak ones with clear explanations.
 Security Logging
Failed password attempts are logged with timestamps to help detect brute-force or weak password patterns.

 Defensive Value
Logs allow security teams to:
 Detect repeated failures
 Investigate suspicious behavior
 Correlate authentication issues with other security events
 518f2a3 (Initial commit: password policy enforcer with logging
