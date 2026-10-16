# Simulated Device Monitoring and Alert System

Student Name: Abarquez, Xander B.     
Student ID: 2600406     
Section: 1CPE-A     

# Project Description
This program monitors simulated device temperature readings. It stores the
readings in a list, lets the user add new valid readings, classifies every
reading as NORMAL, WARNING, or CRITICAL, and prints a numerical summary with
the overall device status. The program is built from small, single-purpose
functions controlled by `main()`.

# Features
- View all stored temperature readings
- Add a new reading (whole numbers from 0 to 100 only)
- Classify every reading
- Generate a numerical summary and overall status
- Reject invalid menu choices and invalid readings

# Requirements
- Python 3 (no external packages)

# How to Run
1. Open a terminal inside the Week17 folder.
2. Type: `python device_monitor.py`
   (On macOS or Linux, type: `python3 device_monitor.py`)

# Sample Output
```
SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit
Enter choice: 4
MONITORING SUMMARY
------------------
Number of readings  : 5
Total of readings   : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C
NORMAL   : 2 (40.00%)
WARNING  : 2 (40.00%)
CRITICAL : 1 (20.00%)
Overall Status: ATTENTION REQUIRED
```

# Test Cases
I performed 10 tests. 10 passed and 0 failed.
Full details are in test_cases.md.

# Known Limitations
- Readings are lost when the program closes; nothing is saved to a file.
- The program only accepts whole-number readings from 0 to 100; it cannot
  record decimal temperatures.

# Reflection
The hardest part of this project was working out the computations and the formulas themselves, especially getting the summary's totals, average, and percentages to line up correctly. Along the way I ran into a bug where Python kept saying that a variable like normal_count was undefined, and after tracing through the code I found the real cause was just a simple indentation mistake, not a missing variable at all. Fixing that taught me how much Python relies on indentation to know which lines belong inside a function. If I were to improve this program next, I would try to shorten the code to its leanest possible form, since typing out around 200 lines left me pretty worn out by the end.