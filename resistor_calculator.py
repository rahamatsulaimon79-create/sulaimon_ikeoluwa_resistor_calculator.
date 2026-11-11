
# SULAIMON IKEOLUWA PROJECT
# RESISTOR COMBINATION CALCULATOR
# Mechatronics Engineering, Yaba College of Technology

# Function to calculate total resistance in series
def calculate_series(resistors):
    total = 0

    for resistance in resistors:
        total = total + resistance

    return total


# Function to calculate total resistance in parallel
def calculate_parallel(resistors):
    total = 0

    for resistance in resistors:
        total = total + (1 / resistance)

    return 1 / total


# Function to collect resistor values
def get_resistors():
    resistors = []

    try:
        number = int(input("Enter the number of resistors: "))

        if number < 1:
            print("Please enter at least one resistor.")
            return []

        for i in range(number):
            value = float(input("Enter resistor " + str(i + 1) + " value in ohms: "))

            if value <= 0:
                print("Resistance must be greater than zero.")
                return []

            resistors.append(value)

        return resistors

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return []


# Main program
print("===================================")
print(" SULAIMON IKEOLUWA PROJECT")
print(" RESISTOR COMBINATION CALCULATOR")
print("===================================")

print("This program calculates resistance")
print("in series and parallel connections.")

resistors = get_resistors()

if len(resistors) > 0:

    # Calculate series and parallel resistance
    series = calculate_series(resistors)
    parallel = calculate_parallel(resistors)

    # Display resistor values
    print("\nResistors entered:", resistors)

    print("\nTotal resistance in series:",
          round(series, 2), "ohms")

    print("Total resistance in parallel:",
          round(parallel, 2), "ohms")

    # Extra feature: Compare both connections
    print("\n===== COMPARISON =====")

    if series > parallel:
        print("Series resistance is greater.")
    elif series < parallel:
        print("Parallel resistance is greater.")
    else:
        print("Both resistance values are equal.")

    # Extra feature: Display the difference
    difference = series - parallel

    print("Difference between both values:",
          round(difference, 2), "ohms")

    print("\nCalculation completed successfully!")

else:
    print("Program ended. Please try again.")

print("\nThank you for using my calculator!")
print("Designed by Sulaimon Ikeoluwa.")
