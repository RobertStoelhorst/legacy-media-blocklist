import os
from datetime import datetime


def remove_duplicate_lines(input_file, output_file, duplicates_file):
    seen = set()
    duplicates = set()
    with open(input_file, 'r', encoding='utf-8') as infile, \
            open(output_file, 'w', encoding='utf-8') as outfile, \
            open(duplicates_file, 'w', encoding='utf-8') as dupfile:

        for line in infile:
            if line in seen:
                duplicates.add(line)
            else:
                outfile.write(line)
                seen.add(line)

        for dup in duplicates:
            dupfile.write(dup)


def overwrite_blocklist(sanitised_file, blocklist_file):
    with open(sanitised_file, 'r', encoding='utf-8') as sfile:
        lines = sorted(sfile.readlines())

    unique_domain_count = len(lines)
    todays_date = datetime.today().strftime('%d %B %Y')

    header = f"""# Title: Legacy Media Propaganda Blocklist
#
# This blocklist is for all western aired Mainstream Mass (Legacy) Media outlets
# Created: 17 February 2025
# Last updated: {todays_date}
# Number of unique domains: {unique_domain_count}
#
# Project home page: https://github.com/RobertStoelhorst/legacy-media-blocklist
# ===============================================================
# THIS FILE IS READ ONLY, DO NOT TRY TO MODIFY THIS FILE DIRECTLY.
# PLEASE SEE THE REPO README.MD FOR INSTRUCTIONS ON UPDATING THIS FILE.
# ===============================================================\n\n"""

    # Temporarily make the file writable if it exists
    if os.path.exists(blocklist_file):
        os.chmod(blocklist_file, 0o644)

    with open(blocklist_file, 'w', encoding='utf-8') as bfile:
        bfile.write(header)
        bfile.writelines(lines)

    # Set file back to read-only
    os.chmod(blocklist_file, 0o444)


if __name__ == "__main__":
    input_filename = "dirty.txt"
    output_filename = "sanitised.txt"
    duplicates_filename = "duplicates.txt"
    blocklist_filename = "Lists/blocklist.txt"

    remove_duplicate_lines(
        input_filename, output_filename, duplicates_filename)
    print(f"Duplicates removed. Cleaned list saved to {output_filename}.")
    print(f"Duplicates saved to {duplicates_filename}.")

    overwrite_blocklist(output_filename, blocklist_filename)
    print(
        f"Sanitised list saved to {blocklist_filename} with header, sorted order, and domain count.")
