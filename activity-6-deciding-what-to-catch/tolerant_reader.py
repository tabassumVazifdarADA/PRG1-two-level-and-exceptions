"""
Reading a file that is not perfect

Yesterday's rainfall reader, given a file with two bad lines in it.
This version already copes. Your job is to work out how, and to
decide whether coping is the right thing to do.
"""

WET_THRESHOLD = 100

with open("rainfall.txt", "r") as f:
    lines = f.readlines()

total = 0
count = 0
rejected = []
last_error_index = None  # Tracks the line index of the previous error

for line_index, line in enumerate(lines):
    try:
        station, millimetres_text = line.strip().split(",")
        millimetres = int(millimetres_text)
        total += millimetres
        count += 1
    except ValueError as problem:
        rejected.append(f"{line.strip()} ({problem})")

        # Check if the previous error happened within 5 lines
        if last_error_index is not None and (line_index - last_error_index) < 5:
            print(
                f"Stopping execution: Two errors found within 5 lines (lines {last_error_index + 1} and {line_index + 1})."
            )
            break

        # Update the index of the last seen error
        last_error_index = line_index
        continue


    total = total + millimetres
    count = count + 1
    status = "Wet" if millimetres >= WET_THRESHOLD else "Dry"
    print(f"{station}: {millimetres} mm ({status})")

print("---")
print(f"{count} stations read, {len(rejected)} rejected")
print(f"Average of the readings that worked: {total / count:.1f} mm")

if rejected:
    print("Rejected lines:")
    for line in rejected:
        print(f"  {line}")
