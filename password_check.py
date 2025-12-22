import re
from datetime import datetime

LOG_FILE = "password_attempts.log"

password = input("Enter a password to check: ")

errors = []

if len(password) < 8:
    errors.append("Minimum length not met")

if not re.search(r"[A-Z]", password):
    errors.append("Missing uppercase letter")

if not re.search(r"[a-z]", password):
    errors.append("Missing lowercase letter")

if not re.search(r"[0-9]", password):
    errors.append("Missing number")

if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    errors.append("Missing special character")

if errors:
    print("\n❌ Password rejected:")
    for error in errors:
        print("-", error)

    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - FAILED - {', '.join(errors)}\n")

    exit(1)
else:
    print("\n✅ Password accepted. Strong password.")
    exit(0)
