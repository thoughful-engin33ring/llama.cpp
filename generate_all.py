#!/usr/bin/env python3
"""
Generate all password patterns to a text file.
"""

import itertools
import string

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SPECIALS = "!@#$%^&*()-_=+[]{};:,.?/"
POOL = string.ascii_letters + string.digits + SPECIALS
DIGITS = string.digits

def generate_script1():
    """Generate all Script 1 patterns."""
    # scb + 4 digits
    for i in range(10000):
        yield f"scb{i:04d}"

    # scb@ + 4 digits
    for i in range(10000):
        yield f"scb@{i:04d}"

    # World@ + 4 digits
    for i in range(10000):
        yield f"World@{i:04d}"

    # Linux@ + 3 digits
    for i in range(1000):
        yield f"Linux@{i:03d}"

    # Month@# + 4 digits
    for month in MONTHS:
        for i in range(10000):
            yield f"{month}@{i:04d}#"

    # Rules@ + 4 digits
    for i in range(10000):
        yield f"Rules@{i:04d}"

    # linux + 2 digits
    for i in range(100):
        yield f"linux{i:02d}"

    # Pass@ + 4 digits
    for i in range(10000):
        yield f"Pass@{i:04d}"

    # Hello@ + 4 digits
    for i in range(10000):
        yield f"Hello@{i:04d}"

    # Standard + 4 digits
    for i in range(10000):
        yield f"Standard{i:04d}"

def generate_script2():
    """Generate all Script 2 patterns: Standard + 4-char suffix with >=1 digit AND >=1 special."""
    digits_set = set(DIGITS)
    specials_set = set(SPECIALS)

    for combo in itertools.product(POOL, repeat=4):
        has_digit = any(c in digits_set for c in combo)
        has_special = any(c in specials_set for c in combo)
        if has_digit and has_special:
            yield "Standard" + "".join(combo)

def main():
    output_file = "output_sum.txt"
    count = 0

    with open(output_file, "w") as f:
        # Script 1 passwords
        for pwd in generate_script1():
            f.write(pwd + "\n")
            count += 1
            if count % 1000000 == 0:
                print(f"Generated {count:,} passwords...")

        # Script 2 passwords
        for pwd in generate_script2():
            f.write(pwd + "\n")
            count += 1
            if count % 1000000 == 0:
                print(f"Generated {count:,} passwords...")

    print(f"Done! Total: {count:,} passwords written to {output_file}")

if __name__ == "__main__":
    main()
