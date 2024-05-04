import csv
import os

def count_consecutive_non_empty(entries):
    count = 0
    max_count = 0

    for entry in entries:
        if entry:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count

def main():
    # List all .csv files in the current directory starting with '5' or '6'
    files = [f for f in os.listdir() if (f.startswith('5') or f.startswith('6')) and f.endswith('.csv')]

    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            total_count_for_file = 0

            # Extract the 'click_action.keys' column and count if it exists
            if 'click_action.keys' in reader.fieldnames:
                entries = [row['click_action.keys'] for row in reader]
                total_count_for_file += count_consecutive_non_empty(entries)
            else:
                print(f"'click_action.keys' column not found in {file}")

            # Reset file pointer to the beginning and recreate the reader to read it again
            f.seek(0)
            reader = csv.DictReader(f)

            # Extract the 'click_action_2.keys' column and count if it exists
            if 'click_action_2.keys' in reader.fieldnames:
                entries = [row['click_action_2.keys'] for row in reader]
                total_count_for_file += count_consecutive_non_empty(entries)
            else:
                print(f"'click_action_2.keys' column not found in {file}")

            print(f"File: {file}, Total consecutive non-empty rows: {total_count_for_file}")

if __name__ == "__main__":
    main()
