"""
Password Strength Checker
Educational, local-only password strength estimator.
Passwords are analyzed in memory and are never saved or transmitted.
"""
import getpass
import math
import re
import string

COMMON_PASSWORDS = {
    "password", "password123", "123456", "123456789", "qwerty",
    "admin", "letmein", "welcome", "iloveyou", "abc123",
}

def estimate_entropy(password: str) -> float:
    """Rough character-pool estimate; predictable patterns can make it misleading."""
    pool = 0
    if any(c in string.ascii_lowercase for c in password): pool += 26
    if any(c in string.ascii_uppercase for c in password): pool += 26
    if any(c in string.digits for c in password): pool += 10
    if any(c in string.punctuation for c in password): pool += len(string.punctuation)
    return len(password) * math.log2(pool) if pool else 0.0

def analyze_password(password: str) -> dict:
    checks = {
        "At least 12 characters": len(password) >= 12,
        "Contains lowercase letters": any(c.islower() for c in password),
        "Contains uppercase letters": any(c.isupper() for c in password),
        "Contains numbers": any(c.isdigit() for c in password),
        "Contains special characters": any(c in string.punctuation for c in password),
    }
    common = password.lower() in COMMON_PASSWORDS
    suggestions = []
    if len(password) < 12:
        suggestions.append("Use at least 12 characters; longer passphrases are usually better.")
    if not checks["Contains lowercase letters"]:
        suggestions.append("Add lowercase letters.")
    if not checks["Contains uppercase letters"]:
        suggestions.append("Add uppercase letters.")
    if not checks["Contains numbers"]:
        suggestions.append("Consider adding numbers.")
    if not checks["Contains special characters"]:
        suggestions.append("Consider adding a special character.")
    if common:
        suggestions.append("Avoid common or predictable passwords.")
    if re.search(r"(.)\1{2,}", password):
        suggestions.append("Avoid repeating the same character several times in a row.")
    if re.search(r"1234|abcd|qwerty", password.lower()):
        suggestions.append("Avoid common sequences such as 1234, abcd, or qwerty.")
    if not password:
        suggestions = ["Enter a password to analyze."]

    score = sum(checks.values())
    if common or len(password) < 8:
        rating = "Weak"
    elif score == len(checks) and len(password) >= 12:
        rating = "Strong"
    else:
        rating = "Medium"

    return {
        "length": len(password),
        "checks": checks,
        "score": score,
        "rating": rating,
        "estimated_entropy_bits": round(estimate_entropy(password), 1),
        "suggestions": suggestions,
    }

def print_report(result: dict) -> None:
    print("\n=== Password Strength Report ===")
    print(f"Length: {result['length']} characters")
    print(f"Rating: {result['rating']}")
    print(f"Criteria met: {result['score']}/{len(result['checks'])}")
    print(f"Rough entropy estimate: {result['estimated_entropy_bits']} bits")
    print("\nChecks:")
    for label, passed in result["checks"].items():
        print(f"  [{'✓' if passed else ' '}] {label}")
    if result["suggestions"]:
        print("\nSuggestions:")
        for suggestion in result["suggestions"]:
            print(f"  - {suggestion}")
    else:
        print("\nNo basic improvement suggestions from these checks.")
    print("\nNote: This educational estimate does not guarantee password security.")

def main() -> None:
    print("Password Strength Checker (local only)")
    print("Use an invented test password, not a real account password.")
    password = getpass.getpass("Enter a test password: ")
    print_report(analyze_password(password))

if __name__ == "__main__":
    main()
