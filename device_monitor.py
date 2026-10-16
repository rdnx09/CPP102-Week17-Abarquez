WARNING_LIMIT = 30
CRITICAL_LIMIT = 35
MIN_VALID_READING = 0
MAX_VALID_READING = 100


def get_initial_readings():
    """Return the starting list of device-temperature readings."""
    return [28, 31, 35, 37, 29]


def is_whole_number(text):
    """Return True if text represents a whole number (a minus sign is
    allowed only as the first character); return False otherwise."""
    if text == "":
        return False
    for index, char in enumerate(text):
        if char == "-" and index == 0:
            continue
        if not char.isdigit():
            return False
    if text == "-":
        return False
    return True


def display_menu():
    """Print the main menu."""
    print("SIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def display_readings(readings):
    """Display every reading currently in the list with its position number."""
    print("CURRENT READINGS")
    print("----------------")
    for index, reading in enumerate(readings):
        print("Reading " + str(index + 1) + ": " + str(reading) + " \u00b0C")


def add_reading(readings):
    """Ask the user for one new reading and add it to readings if, and
    only if, it is a valid whole number from 0 to 100 inclusive."""
    text = input("Enter new reading: ")

    if text == "":
        print("Invalid input. The reading cannot be empty.")
        return

    if not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
        return

    value = int(text)

    if value < MIN_VALID_READING or value > MAX_VALID_READING:
        print("Invalid reading. Enter a value from 0 to 100.")
        return

    readings.append(value)
    print("Reading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
    """Return the classification label (NORMAL, WARNING, or CRITICAL)
    for one reading."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def display_classified_readings(readings, warning_limit, critical_limit):
    """Display every reading together with its classification."""
    print("READING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        label = classify_reading(reading, warning_limit, critical_limit)
        print(str(reading) + " \u00b0C -> " + label)


def compute_total(readings):
    """Return the sum of all readings, computed with a manual loop."""
    total = 0
    for reading in readings:
        total = total + reading
    return total


def compute_average(readings):
    """Return the average of all readings."""
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Return the smallest reading, found with a manual loop."""
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    """Return the largest reading, found with a manual loop."""
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    """Return how many readings fall under the given category label."""
    count = 0
    for reading in readings:
        if classify_reading(reading, warning_limit, critical_limit) == category:
            count = count + 1
    return count


def determine_overall_status(warning_count, critical_count):
    """Return the overall monitoring status based on the counts."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings):
    """Compute and display the full monitoring summary."""
    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)
    count = len(readings)

    normal_count = count_category(readings, WARNING_LIMIT, CRITICAL_LIMIT, "NORMAL")
    warning_count = count_category(readings, WARNING_LIMIT, CRITICAL_LIMIT, "WARNING")
    critical_count = count_category(readings, WARNING_LIMIT, CRITICAL_LIMIT, "CRITICAL")

    normal_pct = normal_count / count * 100
    warning_pct = warning_count / count * 100
    critical_pct = critical_count / count * 100

    status = determine_overall_status(warning_count, critical_count)

    print("MONITORING SUMMARY")
    print("------------------")
    print("Number of readings  : " + str(count))
    print("Total of readings   : " + str(total))
    print("Average temperature : " + format(average, ".2f") + " \u00b0C")
    print("Minimum temperature : " + str(minimum) + " \u00b0C")
    print("Maximum temperature : " + str(maximum) + " \u00b0C")
    print("NORMAL   : " + str(normal_count) + " (" + format(normal_pct, ".2f") + "%)")
    print("WARNING  : " + str(warning_count) + " (" + format(warning_pct, ".2f") + "%)")
    print("CRITICAL : " + str(critical_count) + " (" + format(critical_pct, ".2f") + "%)")
    print("Overall Status: " + status)


def main():
    """Run the menu loop and call the other functions in order."""
    readings = get_initial_readings()

    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings)
        elif choice == "3":
            display_classified_readings(readings, WARNING_LIMIT, CRITICAL_LIMIT)
        elif choice == "4":
            display_summary(readings)
        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()