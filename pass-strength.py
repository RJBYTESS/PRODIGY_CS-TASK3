#!/usr/bin/env python3
import re

def check_password_strength(password):
    length = len(password)
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.match('[!@#$%^&*()_+{}:<>?/.,;]', password))

    strength = 0

    if length >= 8:
        strength += 1
    if has_uppercase and has_lowercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    return strength

def assess_strength(strength):
    if strength == 0:
        return "Very Weak"
    elif strength == 1:
        return "Weak"
    elif strength == 2:
        return "Moderate"
    elif strength == 3:
        return "Strong"
    elif strength == 4:
        return "Very Strong"

def main():
    print("**************************************")
    print("*    Check Your Password Strength    *")
    print("**************************************")
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print("Password strength:", assess_strength(strength))

if __name__ == "__main__":
    main()

