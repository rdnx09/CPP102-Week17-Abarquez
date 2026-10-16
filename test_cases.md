# Test Cases – Simulated Device Monitoring and Alert System

Tested by: Abarquez, Xander B.    
Date of Testing: October 16, 2026        

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|-----------|-----------------|-----------------|---------------|-----------|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | Displayed "Reading 1: 28 °C" through "Reading 5: 29 °C" | Pass |
| TC02 | Choose 2, enter 33 | "Reading added successfully." | "Reading added successfully."; 33 appended to the list | Pass |
| TC03 | Choose 2, enter abc | Rejected; list unchanged | "Invalid input. Enter a whole number only."; list unchanged | Pass |
| TC04 | Choose 2, enter -5 | Rejected; list unchanged | "Invalid reading. Enter a value from 0 to 100."; list unchanged | Pass |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged | "Invalid reading. Enter a value from 0 to 100."; list unchanged | Pass |
| TC06 | Add 30, then choose 3 | 30 °C -> WARNING | "30 °C -> WARNING" | Pass |
| TC07 | Choose 3 | 35 °C -> WARNING | "35 °C -> WARNING" | Pass |
| TC08 | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | "Total of readings : 160", "Average temperature : 32.00 °C", "Minimum temperature : 28 °C", "Maximum temperature : 37 °C", "Overall Status: ATTENTION REQUIRED" | Pass |
| TC09 | Enter 9 | Error message; menu shown again | "Invalid choice. Please enter a number from 1 to 5."; menu reprinted | Pass |
| TC10 | Choose 5 | Exit message; program ends | "Thank you for using the Device Monitoring System."; program ended | Pass |

# Bugs Found and Fixed
While first drafting `find_minimum()` and `find_maximum()`, I started the
`minimum`/`maximum` variable at `0` instead of at `readings[0]`. Because every
sample reading is greater than 0, the minimum always came back as `0`, which
is the exact mistake shown in the Guided Practice "Clinic 1" example. I fixed
it by initializing both variables with the first element of the list
(`readings[0]`) and then comparing every other reading against it, and I
retested all boundary and initial-data cases afterward to confirm the fix.