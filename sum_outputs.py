#!/usr/bin/env python3
"""
Optimized computation of password pattern counts.
Instead of generating all strings, we calculate counts mathematically.
"""

def compute_script1_total():
    """
    Script 1 patterns and their counts:
    - scb + 4 digits: 10^4
    - scb@ + 4 digits: 10^4
    - World@ + 4 digits: 10^4
    - Linux@ + 3 digits: 10^3
    - Month@# (12 months × 4 digits): 12 × 10^4
    - Rules@ + 4 digits: 10^4
    - linux + 2 digits: 10^2
    - Pass@ + 4 digits: 10^4
    - Hello@ + 4 digits: 10^4
    - Standard + 4 digits: 10^4
    """
    patterns = [
        ("scb", 4),        # 10^4
        ("scb@", 4),       # 10^4
        ("World@", 4),     # 10^4
        ("Linux@", 3),     # 10^3
        ("Month@#", 4),    # 12 × 10^4 (12 months)
        ("Rules@", 4),     # 10^4
        ("linux", 2),      # 10^2
        ("Pass@", 4),      # 10^4
        ("Hello@", 4),     # 10^4
        ("Standard", 4),   # 10^4
    ]

    total = 0
    for pattern_name, num_length in patterns:
        count = 10 ** num_length
        if pattern_name == "Month@#":
            count *= 12  # 12 months
        total += count

    return total

def compute_script2_total():
    """
    Script 2 pattern: "Standard" + 4-char suffix
    Suffix must contain at least 1 digit AND at least 1 special.

    POOL = ascii_letters (52) + digits (10) + specials (24) = 86 chars
    DIGITS = 10 chars
    SPECIALS = 24 chars

    Using inclusion-exclusion:
    Total with at least 1 digit AND at least 1 special =
        Total - (no digits) - (no specials) + (no digits AND no specials)
    """
    pool_size = 52 + 10 + 24  # 86: letters + digits + specials
    digits_count = 10
    specials_count = 24
    suffix_len = 4

    total = pool_size ** suffix_len
    no_digits = (pool_size - digits_count) ** suffix_len
    no_specials = (pool_size - specials_count) ** suffix_len
    no_digits_no_specials = (pool_size - digits_count - specials_count) ** suffix_len

    # Inclusion-exclusion
    return total - no_digits - no_specials + no_digits_no_specials

def main():
    script1_count = compute_script1_total()
    script2_count = compute_script2_total()
    total_sum = script1_count + script2_count

    print(f"Script 1 output count: {script1_count}")
    print(f"Script 2 output count: {script2_count}")
    print(f"Sum of outputs: {total_sum}")

    # Write result to file
    with open("output_sum.txt", "w") as f:
        f.write(f"{total_sum}\n")

    print(f"\nResult written to output_sum.txt")

if __name__ == "__main__":
    main()
