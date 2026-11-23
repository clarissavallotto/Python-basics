import zipfile

with zipfile.ZipFile("code_data.zip", "r") as zip_ref:
    zip_ref.extractall("code_data")

# ==================================================
# INTRO TO PROGRAMMING: ARITHMETIC AND VARIABLES
# ==================================================


# --------------------------------------------------
# 1. PRINTING MESSAGES
# --------------------------------------------------

# Display a message on the screen.

print("Hello, world!")


# --------------------------------------------------
# 2. BASIC ARITHMETIC OPERATIONS
# --------------------------------------------------

# Addition
print(1 + 2)

# Subtraction
print(9 - 5)

# Multiplication
print(2 * 4)

# Division
print(6 / 3)

# Exponentiation
print(3 ** 2)


# --------------------------------------------------
# 3. ORDER OF OPERATIONS
# --------------------------------------------------

# Use parentheses to control calculation order.

result = ((1 + 3) * (9 - 2) / 2) ** 2

print(result)


# --------------------------------------------------
# 4. COMMENTS
# --------------------------------------------------

# Comments describe the purpose of the code.
# They are ignored when Python executes the program.

# Multiply 3 by 2.
print(3 * 2)


# --------------------------------------------------
# 5. CREATING VARIABLES
# --------------------------------------------------

# Assign the result of 4 + 5 to a variable.

test_var = 4 + 5

# Display the variable's value.

print(test_var)


# --------------------------------------------------
# 6. MANIPULATING VARIABLES
# --------------------------------------------------

# Create a variable with an initial value.

my_var = 3

# Display the initial value.

print(my_var)

# Update the variable.

my_var = 100

# Display the updated value.

print(my_var)

# Increase the current value by 3.

my_var = my_var + 3

# Display the final value.

print(my_var)


# --------------------------------------------------
# 7. USING MULTIPLE VARIABLES
# --------------------------------------------------

# Define the input values.

num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# Calculate the total number of seconds.

total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years


# Display the result.

print(total_secs)


# --------------------------------------------------
# 8. ACCOUNTING FOR LEAP YEARS
# --------------------------------------------------

# Update the average number of days per year.

days_per_year = 365.25

# Recalculate the total number of seconds.

total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years

# Display the updated result.

print(total_secs)


# --------------------------------------------------
# 9. DEBUGGING VARIABLES
# --------------------------------------------------

# Use the correct variable name to avoid NameError.

print(hours_per_day)


# ============================================================
# INTRO TO PROGRAMMING: FUNCTIONS
# ============================================================


# ------------------------------------------------------------
# 1. DEFINE A SIMPLE FUNCTION
# ------------------------------------------------------------

# Accept one input, add 3, and return the result.

def add_three(input_var):

    # Add 3 to the input value.
    output_var = input_var + 3

    # Return the calculated result.
    return output_var


# ------------------------------------------------------------
# 2. CALL THE SIMPLE FUNCTION
# ------------------------------------------------------------

# Pass 10 to add_three() and store the returned value.

new_number = add_three(10)

# Display the result.
print(new_number)


# ------------------------------------------------------------
# 3. DEFINE A FUNCTION TO CALCULATE PAY AFTER TAX
# ------------------------------------------------------------

# Calculate weekly take-home pay.
# Assumptions:
# - Hourly wage = $15.
# - Tax rate = 12%.

def get_pay(num_hours):

    # Calculate gross salary before tax.
    pay_pretax = num_hours * 15

    # Calculate take-home salary after 12% tax.
    pay_aftertax = pay_pretax * (1 - 0.12)

    # Return the final salary.
    return pay_aftertax


# ------------------------------------------------------------
# 4. CALCULATE FULL-TIME AND PART-TIME PAY
# ------------------------------------------------------------

# Calculate pay for 40 working hours.
pay_fulltime = get_pay(40)

# Display full-time take-home pay.
print(pay_fulltime)


# Calculate pay for 32 working hours.
pay_parttime = get_pay(32)

# Display part-time take-home pay.
print(pay_parttime)


# ------------------------------------------------------------
# 5. UNDERSTAND VARIABLE SCOPE
# ------------------------------------------------------------

# pay_fulltime and pay_parttime are global variables.
# They were defined outside the functions.
# Therefore, they can be accessed here.

print(pay_fulltime)
print(pay_parttime)


# ------------------------------------------------------------
# 6. DEFINE A FUNCTION WITH MULTIPLE ARGUMENTS
# ------------------------------------------------------------

# This function allows the user to specify:
# - Number of working hours.
# - Hourly wage.
# - Tax percentage.

def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):

    # Calculate gross salary.
    pay_pretax = num_hours * hourly_wage

    # Calculate salary after tax deductions.
    pay_aftertax = pay_pretax * (1 - tax_bracket)

    # Return the take-home salary.
    return pay_aftertax


# ------------------------------------------------------------
# 7. CALL THE FUNCTION WITH DIFFERENT INPUTS
# ------------------------------------------------------------

# Example 1:
# 40 hours, $24 per hour, 22% tax.

higher_pay_aftertax = get_pay_with_more_inputs(40, 24, 0.22)

# Display the result.
print(higher_pay_aftertax)


# Example 2:
# 40 hours, $15 per hour, 12% tax.

same_pay_fulltime = get_pay_with_more_inputs(40, 15, 0.12)

# Display the result.
print(same_pay_fulltime)


# ------------------------------------------------------------
# 8. DEFINE A FUNCTION WITHOUT ARGUMENTS
# ------------------------------------------------------------

# This function does not require any input.
# It simply prints two greeting messages.

def print_hello():

    # Display the first greeting.
    print("Hello, you!")

    # Display the second greeting.
    print("Good morning!")


# ------------------------------------------------------------
# 9. CALL THE FUNCTION
# ------------------------------------------------------------

# Execute print_hello().

print_hello()


# ============================================================
# INTRO TO PROGRAMMING: DATA TYPES
# ============================================================


# ------------------------------------------------------------
# 1. INTEGER DATA TYPE (int)
# ------------------------------------------------------------

# Integers are whole numbers without decimal places.

x = 14

# Display the integer value.
print(x)

# Identify the data type.
print(type(x))


# ------------------------------------------------------------
# 2. FLOAT DATA TYPE (float)
# ------------------------------------------------------------

# Define a floating-point approximation of pi.

nearly_pi = 3.141592653589793238462643383279502884197169399375105820974944

# Display the float.
print(nearly_pi)

# Identify the data type.
print(type(nearly_pi))


# Calculate another approximation of pi using division.

almost_pi = 22 / 7

# Display the result.
print(almost_pi)

# Identify the data type.
print(type(almost_pi))


# ------------------------------------------------------------
# 3. ROUNDING FLOATS
# ------------------------------------------------------------

# Round almost_pi to 5 decimal places.

rounded_pi = round(almost_pi, 5)

# Display the rounded result.
print(rounded_pi)

# Identify the data type.
print(type(rounded_pi))


# A number with a decimal point is a float,
# even if its fractional part is zero.

y_float = 1.

# Display the value and its data type.
print(y_float)
print(type(y_float))


# ------------------------------------------------------------
# 4. BOOLEAN DATA TYPE (bool)
# ------------------------------------------------------------

# Create a boolean with the value True.

z_one = True

print(z_one)
print(type(z_one))


# Create a boolean with the value False.

z_two = False

print(z_two)
print(type(z_two))


# ------------------------------------------------------------
# 5. BOOLEAN VALUES FROM COMPARISONS
# ------------------------------------------------------------

# Check whether 1 is smaller than 2.
# The result is True.

z_three = (1 < 2)

print(z_three)
print(type(z_three))


# Check whether 5 is smaller than 3.
# The result is False.

z_four = (5 < 3)

print(z_four)
print(type(z_four))


# ------------------------------------------------------------
# 6. USING THE NOT OPERATOR
# ------------------------------------------------------------

# Reverse the boolean value stored in z_four.
# False becomes True.

z_five = not z_four

print(z_five)
print(type(z_five))


# ------------------------------------------------------------
# 7. STRING DATA TYPE (str)
# ------------------------------------------------------------

# Create a string containing a text message.

w = "Hello, Python!"

# Display the string.
print(w)

# Identify the data type.
print(type(w))


# ------------------------------------------------------------
# 8. STRING LENGTH
# ------------------------------------------------------------

# Use len() to count all characters in the string.
# Spaces and punctuation marks are included.

print(len(w))


# ------------------------------------------------------------
# 9. EMPTY STRINGS
# ------------------------------------------------------------

# Create a string containing no characters.

shortest_string = ""

# Display its data type.
print(type(shortest_string))

# Display its length.
print(len(shortest_string))


# ------------------------------------------------------------
# 10. NUMBERS STORED AS STRINGS
# ------------------------------------------------------------

# Store a numerical value as text using quotation marks.

my_number = "1.12321"

# Display the value and its data type.
print(my_number)
print(type(my_number))


# ------------------------------------------------------------
# 11. TYPE CONVERSION: STRING TO FLOAT
# ------------------------------------------------------------

# Convert the numerical string into a float.

also_my_number = float(my_number)

# Display the converted value and its data type.
print(also_my_number)
print(type(also_my_number))


# ------------------------------------------------------------
# 12. STRING CONCATENATION
# ------------------------------------------------------------

# Combine two strings using the + operator.

new_string = "abc" + "def"

# Display the combined string and its data type.
print(new_string)
print(type(new_string))


# ------------------------------------------------------------
# 13. STRING REPETITION
# ------------------------------------------------------------

# Repeat a string three times using the * operator.

newest_string = "abc" * 3

# Display the result and its data type.
print(newest_string)
print(type(newest_string))


# ============================================================
# INTRO TO PROGRAMMING: CONDITIONS AND CONDITIONAL STATEMENTS
# ============================================================


# ------------------------------------------------------------
# 1. CONDITIONS AND COMPARISON OPERATORS
# ------------------------------------------------------------

# Compare two numerical values.
print(2 > 3)

# Create two variables.
var_one = 1
var_two = 2

# Check whether var_one is less than 1.
print(var_one < 1)

# Check whether var_two is greater than or equal to var_one.
print(var_two >= var_one)


# ------------------------------------------------------------
# 2. IF STATEMENT
# ------------------------------------------------------------

# Evaluate temperature using a single if statement.

def evaluate_temp(temp):

    # Set the default message.
    message = "Normal temperature."

    # Change the message if temperature exceeds 38°C.
    if temp > 38:
        message = "Fever!"

    # Return the final message.
    return message


# Test the function with two different temperatures.
print(evaluate_temp(37))
print(evaluate_temp(39))


# ------------------------------------------------------------
# 3. IF ... ELSE STATEMENT
# ------------------------------------------------------------

# Evaluate temperature using two possible outcomes.

def evaluate_temp_with_else(temp):

    # Check whether temperature exceeds 38°C.
    if temp > 38:

        message = "Fever!"

    else:

        message = "Normal temperature."

    # Return the selected message.
    return message


# Test the function.
print(evaluate_temp_with_else(37))


# ------------------------------------------------------------
# 4. IF ... ELIF ... ELSE STATEMENT
# ------------------------------------------------------------

# Classify temperature into three categories.

def evaluate_temp_with_elif(temp):

    # Check for a high temperature.
    if temp > 38:

        message = "Fever!"

    # Check for a normal temperature.
    elif temp > 35:

        message = "Normal temperature."

    # Handle temperatures of 35°C or below.
    else:

        message = "Low temperature."

    # Return the temperature classification.
    return message


# Test the function with different temperatures.
print(evaluate_temp_with_elif(36))
print(evaluate_temp_with_elif(34))


# ------------------------------------------------------------
# 5. CALCULATING TAXES USING CONDITIONAL STATEMENTS
# ------------------------------------------------------------

# Calculate tax based on two different tax brackets.

def get_taxes(earnings):

    # Apply a 25% tax rate to earnings below $12,000.
    if earnings < 12000:

        tax_owed = 0.25 * earnings

    # Apply a 30% tax rate to earnings of $12,000 or more.
    else:

        tax_owed = 0.30 * earnings

    # Return the calculated tax.
    return tax_owed


# Calculate tax for a person earning $9,000.
ana_taxes = get_taxes(9000)

# Calculate tax for a person earning $15,000.
bob_taxes = get_taxes(15000)

# Display both tax calculations.
print(ana_taxes)
print(bob_taxes)


# ------------------------------------------------------------
# 6. MULTIPLE ELIF STATEMENTS
# ------------------------------------------------------------

# Calculate a fictional medication dose based on weight.
# This example is for programming practice only.

def get_dose(weight):

    # Weight below 5.2 kg.
    if weight < 5.2:

        dose = 1.25

    # Weight from 5.2 kg to below 7.9 kg.
    elif weight < 7.9:

        dose = 2.5

    # Weight from 7.9 kg to below 10.4 kg.
    elif weight < 10.4:

        dose = 3.75

    # Weight from 10.4 kg to below 15.9 kg.
    elif weight < 15.9:

        dose = 5

    # Weight from 15.9 kg to below 21.2 kg.
    elif weight < 21.2:

        dose = 7.5

    # Weight of 21.2 kg or more.
    else:

        dose = 10

    # Return the selected dosage.
    return dose


# Calculate the fictional dose for a weight of 12 kg.
print(get_dose(12))


# ------------------------------------------------------------
# 7. ADDING THREE OR EIGHT
# ------------------------------------------------------------

# Add 3 when the input is below 10.
# Otherwise, add 8.

def add_three_or_eight(input_number):

    if input_number < 10:

        result = input_number + 3

    else:

        result = input_number + 8

    # Return the calculated result.
    return result


# Test with an input below 10.
print(add_three_or_eight(1))

# Test with an input above 10.
print(add_three_or_eight(11))


# ============================================================
# INTRO TO PROGRAMMING: INTRO TO LISTS
# ============================================================


# ------------------------------------------------------------
# 1. CREATING A STRING
# ------------------------------------------------------------

# Store flower names in one string, separated by commas.
flowers = (
    "pink primrose,hard-leaved pocket orchid,canterbury bells,"
    "sweet pea,english marigold,tiger lily,moon orchid,"
    "bird of paradise,monkshood,globe thistle"
)

# Display the data type and contents.
print(type(flowers))
print(flowers)


# ------------------------------------------------------------
# 2. CREATING A LIST
# ------------------------------------------------------------

# Create a list containing the same flower names.
# Each flower is stored as an individual string.
flowers_list = [
    "pink primrose",
    "hard-leaved pocket orchid",
    "canterbury bells",
    "sweet pea",
    "english marigold",
    "tiger lily",
    "moon orchid",
    "bird of paradise",
    "monkshood",
    "globe thistle"
]

# Display the list's data type and contents.
print(type(flowers_list))
print(flowers_list)


# ------------------------------------------------------------
# 3. FINDING THE LENGTH OF A LIST
# ------------------------------------------------------------

# len() counts the number of items in the list.
print("Number of flowers:", len(flowers_list))


# ------------------------------------------------------------
# 4. ACCESSING ITEMS USING INDEXING
# ------------------------------------------------------------

# Python list indexes start at zero.
print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])

# Index -1 refers to the final item in the list.
print("Last entry:", flowers_list[-1])


# ------------------------------------------------------------
# 5. EXTRACTING ITEMS USING SLICING
# ------------------------------------------------------------

# Extract the first three items.
print("First three entries:", flowers_list[:3])

# Extract the final two items.
print("Final two entries:", flowers_list[-2:])


# ------------------------------------------------------------
# 6. REMOVING AN ITEM
# ------------------------------------------------------------

# Remove "globe thistle" from the list.
flowers_list.remove("globe thistle")

# Display the list after removing the item.
print("After removing a flower:", flowers_list)


# ------------------------------------------------------------
# 7. ADDING AN ITEM
# ------------------------------------------------------------

# Add "snapdragon" to the end of the list.
flowers_list.append("snapdragon")

# Display the list after adding the item.
print("After adding a flower:", flowers_list)


# ------------------------------------------------------------
# 8. CREATING A NUMERICAL LIST
# ------------------------------------------------------------

# Record hardcover book sales for seven days.
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]

# Display the total number of daily sales entries.
print("Length of sales list:", len(hardcover_sales))

# Access the third day's sales (index 2).
print("Sales at index 2:", hardcover_sales[2])


# ------------------------------------------------------------
# 9. FINDING MINIMUM AND MAXIMUM VALUES
# ------------------------------------------------------------

# Find the lowest daily sales figure.
print("Minimum sales:", min(hardcover_sales))

# Find the highest daily sales figure.
print("Maximum sales:", max(hardcover_sales))


# ------------------------------------------------------------
# 10. CALCULATING TOTAL SALES
# ------------------------------------------------------------

# Add all daily sales figures together.
print("Total books sold in one week:", sum(hardcover_sales))


# ------------------------------------------------------------
# 11. CALCULATING AVERAGE SALES
# ------------------------------------------------------------

# Extract the first five daily sales figures.
first_five_days = hardcover_sales[:5]

# Calculate the average for the first five days.
average_sales = sum(first_five_days) / 5

# Display the calculated average.
print("Average books sold in first five days:", average_sales)


# ============================================================
# PYTHON: HELLO, PYTHON
# ============================================================


# ------------------------------------------------------------
# SECTION 1: VARIABLE ASSIGNMENT
# ------------------------------------------------------------

# Create a variable and assign it an integer value.
spam_amount = 0

# Display the initial value.
print(spam_amount)


# ------------------------------------------------------------
# SECTION 2: REASSIGNING VARIABLES
# ------------------------------------------------------------

# Increase the current value of spam_amount by 4.
# Python calculates the right-hand side before assigning the result.
spam_amount = spam_amount + 4


# ------------------------------------------------------------
# SECTION 3: CONDITIONAL STATEMENTS
# ------------------------------------------------------------

# Check whether the number of spam servings is greater than zero.
if spam_amount > 0:
    # This statement executes only when the condition is True.
    print("But I don't want ANY spam!")


# ------------------------------------------------------------
# SECTION 4: STRING MULTIPLICATION
# ------------------------------------------------------------

# Repeat the string "Spam " according to spam_amount.
viking_song = "Spam " * spam_amount

# Display the resulting string.
print(viking_song)


# ------------------------------------------------------------
# SECTION 5: IDENTIFYING DATA TYPES
# ------------------------------------------------------------

# Create an integer variable.
spam_amount = 0

# Display its data type.
print(type(spam_amount))

# Check the data type of a decimal number.
print(type(19.95))


# ------------------------------------------------------------
# SECTION 6: ARITHMETIC OPERATIONS
# ------------------------------------------------------------

# Addition.
print(5 + 2)

# Subtraction.
print(5 - 2)

# Multiplication.
print(5 * 2)

# True division.
print(5 / 2)

# Floor division.
print(5 // 2)

# Modulus (remainder).
print(5 % 2)

# Exponentiation.
print(5 ** 2)

# Negation.
print(-5)


# ------------------------------------------------------------
# SECTION 7: TRUE DIVISION AND FLOOR DIVISION
# ------------------------------------------------------------

# True division returns a float.
print(5 / 2)
print(6 / 2)

# Floor division rounds down to the nearest integer.
print(5 // 2)
print(6 // 2)


# ------------------------------------------------------------
# SECTION 8: ORDER OF OPERATIONS
# ------------------------------------------------------------

# Python evaluates multiplication before addition.
print(8 - 3 + 2)
print(-3 + 4 * 2)


# ------------------------------------------------------------
# SECTION 9: CALCULATING HEIGHT
# ------------------------------------------------------------

# Define the height of the hat in centimetres.
hat_height_cm = 25

# Define the person's height in centimetres.
my_height_cm = 190

# Calculate height without parentheses.
# Division is performed before addition.
total_height_meters = hat_height_cm + my_height_cm / 100

# Display the result of the calculation.
print("Height in meters =", total_height_meters, "?")

# Calculate height correctly using parentheses.
# First add both heights, then divide by 100.
total_height_meters = (hat_height_cm + my_height_cm) / 100

# Display the corrected result.
print("Height in meters =", total_height_meters)


# ------------------------------------------------------------
# SECTION 10: MINIMUM AND MAXIMUM
# ------------------------------------------------------------

# Find and display the smallest value.
print(min(1, 2, 3))

# Find and display the largest value.
print(max(1, 2, 3))


# ------------------------------------------------------------
# SECTION 11: ABSOLUTE VALUE
# ------------------------------------------------------------

# Display the absolute value of a positive number.
print(abs(32))

# Display the absolute value of a negative number.
print(abs(-32))


# ------------------------------------------------------------
# SECTION 12: NUMERIC TYPE CONVERSION
# ------------------------------------------------------------

# Convert an integer into a float.
print(float(10))

# Convert a float into an integer.
# The decimal portion is discarded, not rounded.
print(int(3.33))

# Convert a numeric string into an integer and add 1.
print(int("807") + 1)


# ============================================================
# PYTHON: FUNCTIONS AND GETTING HELP
# ============================================================


# ------------------------------------------------------------
# SECTION 1: GETTING HELP
# ------------------------------------------------------------

# Display documentation for the built-in round() function.
help(round)

# WARNING:
# This calls round() first, producing the integer -2.
# help() then displays documentation for the integer type,
# not the round() function.
help(round(-2.01))

# Display documentation for the print() function.
help(print)


# ------------------------------------------------------------
# SECTION 2: DEFINING A FUNCTION
# ------------------------------------------------------------

def least_difference(a, b, c):
    """
    Return the smallest difference between any two numbers
    among a, b and c.

    Parameters:
        a: First number.
        b: Second number.
        c: Third number.

    Returns:
        The smallest absolute difference between any pair.
    """

    # Calculate the absolute differences between each pair.
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)

    # Return the smallest difference.
    return min(diff1, diff2, diff3)


# Test the function with three different sets of arguments.
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)


# ------------------------------------------------------------
# SECTION 3: GETTING HELP FOR A CUSTOM FUNCTION
# ------------------------------------------------------------

# Display the function signature and docstring.
help(least_difference)


# ------------------------------------------------------------
# SECTION 4: FUNCTIONS WITHOUT RETURN VALUES
# ------------------------------------------------------------

def least_difference_no_return(a, b, c):
    """
    Calculate the smallest difference without returning it.

    This function demonstrates what happens when return
    is omitted.
    """

    # Calculate the absolute differences.
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)

    # Calculate the smallest difference.
    # The result is discarded because there is no return statement.
    min(diff1, diff2, diff3)


# Each function call returns None.
print(
    least_difference_no_return(1, 10, 100),
    least_difference_no_return(1, 10, 10),
    least_difference_no_return(5, 6, 7),
)


# ------------------------------------------------------------
# SECTION 5: UNDERSTANDING NONE
# ------------------------------------------------------------

# print() produces a side effect by displaying output.
# It returns None because it does not return a value.
mystery = print()

# Display the returned value.
print(mystery)


# ------------------------------------------------------------
# SECTION 6: DEFAULT ARGUMENTS
# ------------------------------------------------------------

def greet(who="Colin"):
    """
    Display a greeting.

    Parameters:
        who: Name of the person to greet.
             Defaults to "Colin" if no argument is supplied.
    """

    # Print the greeting.
    print("Hello,", who)


# Use the default argument.
greet()

# Specify the argument by parameter name.
greet(who="Kaggle")

# Specify the argument directly.
greet("world")


# ------------------------------------------------------------
# SECTION 7: HIGHER-ORDER FUNCTIONS
# ------------------------------------------------------------

def mult_by_five(x):
    """
    Multiply a number by five.

    Parameters:
        x: Number to multiply.

    Returns:
        x multiplied by five.
    """

    return 5 * x


def call(fn, arg):
    """
    Execute a supplied function with one argument.

    Parameters:
        fn: Function to execute.
        arg: Argument passed to the function.

    Returns:
        The result of fn(arg).
    """

    return fn(arg)


def squared_call(fn, arg):
    """
    Execute a supplied function twice.

    Parameters:
        fn: Function to execute.
        arg: Initial argument.

    Returns:
        The result of fn(fn(arg)).
    """

    return fn(fn(arg))


# Call mult_by_five() once through call().
# Call mult_by_five() twice through squared_call().
print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep="\n",
)


# ------------------------------------------------------------
# SECTION 8: USING FUNCTIONS WITH max()
# ------------------------------------------------------------

def mod_5(x):
    """
    Return the remainder after dividing a number by five.

    Parameters:
        x: Number to divide.

    Returns:
        The remainder of x divided by 5.
    """

    return x % 5


# Find the largest original number.
print(max(100, 51, 14))

# Find the number with the largest remainder after division by 5.
print(max(100, 51, 14, key=mod_5))


# Display both comparisons with descriptive labels.
print(
    "Which number is biggest?",
    max(100, 51, 14),
    "Which number is the biggest modulo 5?",
    max(100, 51, 14, key=mod_5),
    sep="\n",
)


# ============================================================
# PYTHON: BOOLEANS AND CONDITIONALS
# ============================================================


# ------------------------------------------------------------
# SECTION 1: BOOLEAN VALUES
# ------------------------------------------------------------

# Create a Boolean variable.
x = True

# Display its value and data type.
print(x)
print(type(x))


# ------------------------------------------------------------
# SECTION 2: COMPARISON OPERATORS
# ------------------------------------------------------------

# Equal to.
print(5 == 5)

# Not equal to.
print(5 != 3)

# Less than.
print(3 < 5)

# Greater than.
print(8 > 4)

# Less than or equal to.
print(5 <= 5)

# Greater than or equal to.
print(8 >= 6)

# Compare an integer and a float.
print(3.0 == 3)

# Compare a string and an integer.
print("3" == 3)


# ------------------------------------------------------------
# SECTION 3: PRESIDENTIAL AGE REQUIREMENT
# ------------------------------------------------------------

def can_run_for_president(age):
    """
    Check whether someone meets the minimum presidential
    age requirement in the United States.

    Parameters:
        age: The person's age.

    Returns:
        True if age is at least 35; otherwise False.
    """

    # Check whether the person is at least 35 years old.
    return age >= 35


# Test the function.
print(
    "Can a 19-year-old run for president?",
    can_run_for_president(19)
)

print(
    "Can a 45-year-old run for president?",
    can_run_for_president(45)
)


# ------------------------------------------------------------
# SECTION 4: CHECKING ODD NUMBERS
# ------------------------------------------------------------

def is_odd(n):
    """
    Check whether an integer is odd.

    Parameters:
        n: Integer to evaluate.

    Returns:
        True if n is odd; otherwise False.
    """

    # Odd numbers have a remainder of 1 when divided by 2.
    return (n % 2) == 1


# Test the function.
print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))


# ------------------------------------------------------------
# SECTION 5: COMBINING BOOLEAN VALUES
# ------------------------------------------------------------

# AND requires both conditions to be True.
print(True and True)
print(True and False)

# OR requires at least one condition to be True.
print(True or False)
print(False or False)

# NOT reverses a Boolean value.
print(not True)
print(not False)


# ------------------------------------------------------------
# SECTION 6: COMBINING CONDITIONS IN A FUNCTION
# ------------------------------------------------------------

def can_run_for_president_with_citizenship(
    age,
    is_natural_born_citizen
):
    """
    Check presidential eligibility using age and citizenship.

    Parameters:
        age: The person's age.
        is_natural_born_citizen: Citizenship qualification.

    Returns:
        True if both conditions are satisfied.
    """

    # Both conditions must be True.
    return is_natural_born_citizen and (age >= 35)


# Test different combinations of conditions.
print(can_run_for_president_with_citizenship(19, True))
print(can_run_for_president_with_citizenship(55, False))
print(can_run_for_president_with_citizenship(55, True))


# ------------------------------------------------------------
# SECTION 7: BOOLEAN OPERATOR PRECEDENCE
# ------------------------------------------------------------

# AND is evaluated before OR.
print(True or True and False)


# ------------------------------------------------------------
# SECTION 8: WEATHER CONDITIONS
# ------------------------------------------------------------

# Define the weather-related variables.
have_umbrella = True
rain_level = 3
have_hood = True
is_workday = True

# Determine whether we are prepared for the weather.
# Parentheses make the logical conditions easier to understand.
prepared_for_weather = (
    have_umbrella
    or (rain_level < 5 and have_hood)
    or not (rain_level > 0 and is_workday)
)

# Display the result.
print("Prepared for weather:", prepared_for_weather)


# ------------------------------------------------------------
# SECTION 9: CONDITIONAL STATEMENTS
# ------------------------------------------------------------

def inspect(x):
    """
    Identify whether a number is zero, positive or negative.

    Parameters:
        x: Number to inspect.
    """

    # Check whether x is zero.
    if x == 0:
        print(x, "is zero")

    # Check whether x is positive.
    elif x > 0:
        print(x, "is positive")

    # Check whether x is negative.
    elif x < 0:
        print(x, "is negative")

    # Fallback block if none of the conditions are satisfied.
    else:
        print(x, "is unlike anything I've ever seen...")


# Test the inspect() function.
inspect(0)
inspect(-15)


# ------------------------------------------------------------
# SECTION 10: INDENTATION AND CONDITIONAL EXECUTION
# ------------------------------------------------------------

def f(x):
    """
    Demonstrate conditional execution using indentation.

    Parameters:
        x: Number to evaluate.
    """

    # Execute this block only if x is greater than zero.
    if x > 0:
        print("Only printed when x is positive; x =", x)
        print("Also only printed when x is positive; x =", x)

    # This statement is outside the conditional block.
    # It always executes.
    print("Always printed, regardless of x's value; x =", x)


# Test with a positive number and zero.
f(1)
f(0)


# ------------------------------------------------------------
# SECTION 11: BOOLEAN CONVERSION
# ------------------------------------------------------------

# Convert non-zero and zero numbers into Boolean values.
print(bool(1))
print(bool(0))

# Convert non-empty and empty strings into Boolean values.
print(bool("asf"))
print(bool(""))


# ------------------------------------------------------------
# SECTION 12: TRUTHY AND FALSEY VALUES IN CONDITIONS
# ------------------------------------------------------------

# Zero is falsey, so the first block is skipped.
if 0:
    print(0)

# A non-empty string is truthy, so this block executes.
elif "spam":
    print("spam")


# ============================================================
# PYTHON: LISTS
# ============================================================


# ============================================================
# 1. CREATING LISTS
# ============================================================

# A list stores an ordered collection of elements.
primes = [2, 3, 5, 7]

# Lists can contain strings.
planets = [
    'Mercury', 'Venus', 'Earth', 'Mars',
    'Jupiter', 'Saturn', 'Uranus', 'Neptune'
]

# Lists can contain other lists (nested lists).
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K']
]

# Lists can contain different data types.
my_favourite_things = [32, 'raindrops on roses', help]


# ============================================================
# 2. INDEXING
# ============================================================

# Access elements using their positions.
print(planets[0])    # First element: Mercury
print(planets[1])    # Second element: Venus

# Negative indices count backwards from the end.
print(planets[-1])   # Last element: Neptune
print(planets[-2])   # Second-to-last element: Uranus


# ============================================================
# 3. SLICING
# ============================================================

# Extract a portion of the list.
print(planets[0:3])  # First three planets

# Omitting the start index begins at index 0.
print(planets[:3])

# Omitting the end index continues to the end.
print(planets[3:])

# Negative indices can be used in slices.
print(planets[1:-1])  # All except the first and last
print(planets[-3:])   # Last three planets


# ============================================================
# 4. MODIFYING LISTS
# ============================================================

# Lists are mutable, so individual elements can be replaced.
planets[3] = 'Malacandra'

# Slice assignment replaces multiple elements.
planets[:3] = ['Mur', 'Vee', 'Ur']

# Restore the original planet names.
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars']

print(planets)


# ============================================================
# 5. BUILT-IN LIST FUNCTIONS
# ============================================================

print(len(planets))       # Number of elements
print(sorted(planets))    # Alphabetically sorted copy

print(sum(primes))        # Sum of numeric elements
print(max(primes))        # Largest element
print(min(primes))        # Smallest element


# ============================================================
# 6. OBJECTS, ATTRIBUTES AND METHODS
# ============================================================

# An attribute stores information associated with an object.
x = 12
print(x.imag)             # Imaginary part of the integer: 0

# A complex number has a real and imaginary part.
c = 12 + 3j
print(c.imag)             # Imaginary part: 3.0

# bit_length() is a method belonging to integer objects.
print(x.bit_length())     # Number of bits needed to represent 12


# ============================================================
# 7. LIST METHODS
# ============================================================

# append() adds an item to the end of the list.
planets.append('Pluto')
print(planets)

# pop() removes and returns the last element.
removed_planet = planets.pop()
print(removed_planet)     # Pluto
print(planets)

# index() finds the position of an element.
print(planets.index('Earth'))  # 2

# The 'in' operator checks whether an element exists.
print('Earth' in planets)          # True
print('Calbefraques' in planets)   # False

# count() counts occurrences of a value.
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))            # 3

# extend() adds elements from another iterable.
numbers.extend([4, 5])
print(numbers)

# insert() adds an element at a specified position.
numbers.insert(0, 100)
print(numbers)

# remove() removes the first matching element.
numbers.remove(2)
print(numbers)

# reverse() reverses the list in place.
numbers.reverse()
print(numbers)

# sort() sorts the list in place.
numbers.sort()
print(numbers)


# ============================================================
# 8. TUPLES
# ============================================================

# Tuples are ordered collections that cannot be modified.
t = (1, 2, 3)

# Parentheses are optional when creating a tuple.
t = 1, 2, 3

print(t)

# Tuples support indexing, but not item assignment.
print(t[0])


# ============================================================
# 9. TUPLE UNPACKING
# ============================================================

# as_integer_ratio() returns a tuple containing two values.
x = 0.125

numerator, denominator = x.as_integer_ratio()

# Assign each tuple element to its own variable.
print(numerator)
print(denominator)

# Reconstruct the original floating-point value.
print(numerator / denominator)


# ============================================================
# 10. SWAPPING VARIABLES
# ============================================================

a = 1
b = 0

# Swap the values without using a temporary variable.
a, b = b, a

print(a, b)  # Output: 0 1



# ============================================================
# PYTHON: LOOPS AND LIST COMPREHENSIONS
# ============================================================


# ------------------------------------------------------------
# 1. FOR LOOPS
# ------------------------------------------------------------

# Create a list of planets.
planets = [
    'Mercury', 'Venus', 'Earth', 'Mars',
    'Jupiter', 'Saturn', 'Uranus', 'Neptune'
]

# Iterate through the list and print each planet.
for planet in planets:
    print(planet, end=' ')

print()  # Move to a new line after printing the planets.


# ------------------------------------------------------------
# 2. ITERATING OVER A TUPLE
# ------------------------------------------------------------

# Multiply all numbers in the tuple together.
multiplicands = (2, 2, 2, 3, 3, 5)

product = 1

for mult in multiplicands:
    product = product * mult

print("Product:", product)  # 360


# ------------------------------------------------------------
# 3. ITERATING OVER A STRING
# ------------------------------------------------------------

# Examine every character and print only uppercase letters.
s = (
    'steganograpHy is the practicE of conceaLing a file, '
    'message, image, or video within another fiLe, '
    'message, image, Or video.'
)

for char in s:
    if char.isupper():
        print(char, end='')

print()  # Move to a new line after printing HELLO.


# ------------------------------------------------------------
# 4. RANGE()
# ------------------------------------------------------------

# Repeat an action five times.
for i in range(5):
    print("Doing important work. i =", i)


# ------------------------------------------------------------
# 5. WHILE LOOPS
# ------------------------------------------------------------

# Print numbers from 0 to 9.
i = 0

while i < 10:
    print(i, end=' ')
    i += 1

print()


# ------------------------------------------------------------
# 6. LIST COMPREHENSIONS
# ------------------------------------------------------------

# Create a list of squares for numbers from 0 to 9.
squares = [n**2 for n in range(10)]

print("Squares:", squares)


# ------------------------------------------------------------
# 7. LIST COMPREHENSION USING A FOR LOOP
# ------------------------------------------------------------

# The same operation can be performed using a traditional loop.
squares = []

for n in range(10):
    squares.append(n**2)

print("Squares using a loop:", squares)


# ------------------------------------------------------------
# 8. FILTERING WITH A CONDITION
# ------------------------------------------------------------

# Select planets with names shorter than 6 characters.
short_planets = [
    planet
    for planet in planets
    if len(planet) < 6
]

print("Short planet names:", short_planets)


# ------------------------------------------------------------
# 9. FILTERING AND TRANSFORMING
# ------------------------------------------------------------

# Convert selected planet names to uppercase and add '!'.
loud_short_planets = [
    planet.upper() + '!'
    for planet in planets
    if len(planet) < 6
]

print("Loud short planet names:", loud_short_planets)


# ------------------------------------------------------------
# 10. LIST COMPREHENSION WITHOUT USING THE LOOP VARIABLE
# ------------------------------------------------------------

# Generate one 32 for every planet in the list.
repeated_numbers = [32 for planet in planets]

print("Repeated numbers:", repeated_numbers)


# ------------------------------------------------------------
# 11. COUNTING NEGATIVE NUMBERS WITH A FOR LOOP
# ------------------------------------------------------------

def count_negatives_loop(nums):
    """Count negative numbers using a traditional for loop."""

    n_negative = 0

    for num in nums:
        if num < 0:
            n_negative += 1

    return n_negative


# ------------------------------------------------------------
# 12. COUNTING NEGATIVE NUMBERS WITH A LIST COMPREHENSION
# ------------------------------------------------------------

def count_negatives_list(nums):
    """Count negative numbers using len() and a list comprehension."""

    return len([
        num
        for num in nums
        if num < 0
    ])


# ------------------------------------------------------------
# 13. COUNTING NEGATIVE NUMBERS WITH SUM()
# ------------------------------------------------------------

def count_negatives_sum(nums):
    """Count negative numbers by summing Boolean comparison results."""

    return sum([
        num < 0
        for num in nums
    ])


# ------------------------------------------------------------
# 14. TESTING THE THREE FUNCTIONS
# ------------------------------------------------------------

# Create a sample list containing positive, negative and zero values.
test_numbers = [5, -1, -2, 0, 3]

# All three approaches should return the same result.
print("Using a for loop:", count_negatives_loop(test_numbers))
print("Using a list comprehension:", count_negatives_list(test_numbers))
print("Using sum():", count_negatives_sum(test_numbers))

# Expected output:
# Using a for loop: 2
# Using a list comprehension: 2
# Using sum(): 2



# ============================================================
# PYTHON: STRINGS AND DICTIONARIES
# ============================================================


# ------------------------------------------------------------
# 1. CREATING STRINGS
# ------------------------------------------------------------

# Single and double quotes are interchangeable.
x = 'Pluto is a planet'
y = "Pluto is a planet"

print(x == y)  # True

# Quotes can be included by choosing the opposite quote style.
print("Pluto's a planet!")
print('My dog is named "Pluto"')

# Escape characters allow quotes and special characters in strings.
print('Pluto\'s a planet!')
print("That's \"cool\"")
print("Look, a mountain: /\\")

# \n creates a new line.
hello = "hello\nworld"
print(hello)

# Triple quotes allow strings to span multiple lines.
triplequoted_hello = """hello
world"""

print(triplequoted_hello)
print(triplequoted_hello == hello)  # True


# ------------------------------------------------------------
# 2. PRINTING STRINGS
# ------------------------------------------------------------

# print() adds a newline by default.
print("hello")
print("world")

# end='' prevents print() from adding a newline.
print("hello", end='')
print("pluto", end='')
print()


# ------------------------------------------------------------
# 3. STRINGS AS SEQUENCES
# ------------------------------------------------------------

planet = 'Pluto'

print(planet[0])       # P
print(planet[-3:])     # uto
print(len(planet))     # 5

# Loop through the characters using a list comprehension.
character_list = [char + '! ' for char in planet]
print(character_list)


# ------------------------------------------------------------
# 4. STRING METHODS
# ------------------------------------------------------------

claim = "Pluto is a planet!"

print(claim.upper())
print(claim.lower())
print(claim.index('plan'))
print(claim.startswith(planet))
print(claim.endswith('planet'))


# ------------------------------------------------------------
# 5. SPLITTING STRINGS
# ------------------------------------------------------------

# split() converts a string into a list of smaller strings.
words = claim.split()
print(words)

# Split a date using hyphens.
datestr = '1956-01-31'

year, month, day = datestr.split('-')

print(year, month, day)


# ------------------------------------------------------------
# 6. JOINING STRINGS
# ------------------------------------------------------------

# join() combines strings using a chosen separator.
date = '/'.join([month, day, year])
print(date)

# Convert words to uppercase and join them with an emoji.
celebration = ' 👏 '.join([word.upper() for word in words])
print(celebration)


# ------------------------------------------------------------
# 7. STRING CONCATENATION
# ------------------------------------------------------------

# The + operator combines strings.
planet = 'Pluto'
print(planet + ', we miss you.')

# Convert numbers to strings before concatenating.
position = 9

message = (
    planet
    + ", you'll always be the "
    + str(position)
    + "th planet to me."
)

print(message)


# ------------------------------------------------------------
# 8. STRING FORMATTING
# ------------------------------------------------------------

# format() inserts values into {} placeholders.
message = "{}, you'll always be the {}th planet to me.".format(
    planet,
    position
)

print(message)

# Format numbers using precision, percentages and commas.
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390

message = (
    "{} weighs about {:.2} kilograms "
    "({:.3%} of Earth's mass). "
    "It is home to {:,} Plutonians."
).format(
    planet,
    pluto_mass,
    pluto_mass / earth_mass,
    population
)

print(message)

# Use numbered placeholders to reuse formatting arguments.
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')

print(s)


# ------------------------------------------------------------
# 9. CREATING DICTIONARIES
# ------------------------------------------------------------

# Dictionaries store key-value pairs.
numbers = {
    'one': 1,
    'two': 2,
    'three': 3
}

# Retrieve a value using its key.
print(numbers['one'])

# Add a new key-value pair.
numbers['eleven'] = 11

# Change the value associated with an existing key.
numbers['one'] = 'Pluto'

print(numbers)


# ------------------------------------------------------------
# 10. DICTIONARY COMPREHENSIONS
# ------------------------------------------------------------

planets = [
    'Mercury', 'Venus', 'Earth', 'Mars',
    'Jupiter', 'Saturn', 'Uranus', 'Neptune'
]

# Create a dictionary mapping each planet to its first letter.
planet_to_initial = {
    planet: planet[0]
    for planet in planets
}

print(planet_to_initial)


# ------------------------------------------------------------
# 11. CHECKING DICTIONARY KEYS
# ------------------------------------------------------------

# The 'in' operator checks dictionary keys.
print('Saturn' in planet_to_initial)       # True
print('Betelgeuse' in planet_to_initial)   # False


# ------------------------------------------------------------
# 12. LOOPING THROUGH DICTIONARIES
# ------------------------------------------------------------

# Loop through dictionary keys and retrieve their values.
for k in numbers:
    print("{} = {}".format(k, numbers[k]))


# ------------------------------------------------------------
# 13. ACCESSING KEYS AND VALUES
# ------------------------------------------------------------

# Retrieve all keys.
print(numbers.keys())

# Retrieve all values.
print(numbers.values())

# Sort the planet initials and join them into one string.
initials = ' '.join(sorted(planet_to_initial.values()))

print(initials)


# ------------------------------------------------------------
# 14. LOOPING THROUGH KEY-VALUE PAIRS
# ------------------------------------------------------------

# items() returns key-value pairs.
for planet, initial in planet_to_initial.items():

    # rjust(10) right-aligns the planet name.
    print('{} begins with "{}"'.format(planet.rjust(10), initial))


# ------------------------------------------------------------
# 15. DOCUMENTATION
# ------------------------------------------------------------

# Display the built-in documentation for dictionaries.
# Uncomment this line when you want to inspect the full help page.
# help(dict)



# ============================================================
# PYTHON: WORKING WITH EXTERNAL LIBRARIES
# ============================================================


# ------------------------------------------------------------
# 1. IMPORTING MODULES
# ------------------------------------------------------------

# Import Python's built-in math module.
import math

# Inspect the module.
print(type(math))
print(dir(math))

# Access a constant and call a function from math.
print("Pi:", math.pi)
print("Logarithm:", math.log(32, 2))

# Get documentation for a function.
help(math.log)


# ------------------------------------------------------------
# 2. IMPORT ALIASES AND SPECIFIC NAMES
# ------------------------------------------------------------

# Import math using a shorter name.
import math as mt

print(mt.pi)

# Import only the specific names needed.
from math import log, pi

print(pi)
print(log(32, 2))


# ------------------------------------------------------------
# 3. IMPORTING NUMPY AND USING SUBMODULES
# ------------------------------------------------------------

import numpy

# Inspect the random submodule.
print(type(numpy.random))
print(dir(numpy.random)[-15:])

# Generate 10 random integers from 1 to 5.
rolls = numpy.random.randint(low=1, high=6, size=10)

print(rolls)


# ------------------------------------------------------------
# 4. INVESTIGATING UNFAMILIAR OBJECTS
# ------------------------------------------------------------

# Identify the type of the NumPy array.
print(type(rolls))

# Inspect its available methods and attributes.
print(dir(rolls))

# Calculate the average.
print(rolls.mean())

# Convert the array into a Python list.
print(rolls.tolist())

# Get documentation for a particular method.
help(rolls.ravel)


# ------------------------------------------------------------
# 5. OPERATOR OVERLOADING
# ------------------------------------------------------------

# NumPy allows arithmetic operations to be applied to every
# element in an array.
print(rolls + 10)

# Compare every element with 3.
print(rolls <= 3)


# ------------------------------------------------------------
# 6. MULTIDIMENSIONAL ARRAYS
# ------------------------------------------------------------

# Create a nested Python list.
xlist = [[1, 2, 3], [2, 4, 6]]

# Convert the list into a two-dimensional NumPy array.
x = numpy.asarray(xlist)

print("xlist = {}\nx =\n{}".format(xlist, x))

# Access the last element of the second row.
print(x[1, -1])

# Regular nested lists use two indexing operations.
print(xlist[1][-1])


# ------------------------------------------------------------
# 7. SPECIAL METHODS
# ------------------------------------------------------------

# Inspect the methods available on Python's list type.
print(dir(list))

# The 'in' operator uses the __contains__ special method.
value = 2

print(value in [1, 2, 3])
print([1, 2, 3].__contains__(value))


# ------------------------------------------------------------
# 8. TENSORFLOW EXAMPLE (OPTIONAL)
# ------------------------------------------------------------

# Uncomment these lines if TensorFlow is installed.
#
# import tensorflow as tf
#
# a = tf.constant(1)
# b = tf.constant(1)
#
# # Addition produces a Tensor object.
# print(a + b)


# ==================================================
# PANDAS: CREATING, READING AND WRITING
# ==================================================


# ==========================================
# 1. IMPORT PANDAS
# ==========================================

# Import pandas using its conventional alias.
import pandas as pd


# ==========================================
# 2. CREATE DATAFRAMES
# ==========================================

# Create a DataFrame using a dictionary.
# Dictionary keys are column names.
# Dictionary values are lists containing column data.
df1 = pd.DataFrame({
    'Yes': [50, 21],
    'No': [131, 2]
})

# Create a DataFrame containing text.
df2 = pd.DataFrame({
    'Bob': ['I liked it.', 'It was awful.'],
    'Sue': ['Pretty good.', 'Bland.']
})

# Create a DataFrame with custom row indexes.
df3 = pd.DataFrame(
    {
        'Bob': ['I liked it.', 'It was awful.'],
        'Sue': ['Pretty good.', 'Bland.']
    },
    index=['Product A', 'Product B']
)


# ==========================================
# 3. CREATE SERIES
# ==========================================

# Create a Series from a list.
series1 = pd.Series([1, 2, 3, 4, 5])

# Create a Series with custom indexes and a name.
series2 = pd.Series(
    [30, 35, 40],
    index=['2015 Sales', '2016 Sales', '2017 Sales'],
    name='Product A'
)


# ==========================================
# 4. READ A CSV FILE
# ==========================================

# Read the wine reviews CSV file into a DataFrame.
wine_reviews = pd.read_csv("/content/code_data/code_data/winemag-data-130k-v2.csv")


# ==========================================
# 5. EXPLORE THE DATAFRAME
# ==========================================

# Get the number of rows and columns.
print(wine_reviews.shape)

# Display the first five rows.
print(wine_reviews.head())


# ==========================================
# 6. READ A CSV WITH A CUSTOM INDEX
# ==========================================

# Use the first CSV column as the DataFrame index.
wine_reviews = pd.read_csv("/content/code_data/code_data/winemag-data-130k-v2.csv", index_col=0)

# Display the first five rows.
print(wine_reviews.head())


# ==================================================
# PANDAS: INDEXING, SELECTING & ASSIGNING
# ==================================================


# ==========================================
# 1. IMPORT PANDAS AND LOAD DATA
# ==========================================

import pandas as pd

# Load the wine reviews dataset.
# Use the first CSV column as the DataFrame index.
reviews = pd.read_csv("/content/code_data/code_data/winemag-data-130k-v2.csv", index_col=0)

# Display a maximum of five rows in pandas output.
pd.set_option('display.max_rows', 5)


# ==========================================
# 2. SELECT COLUMNS AND INDIVIDUAL VALUES
# ==========================================

# Select the country column using attribute notation.
reviews.country

# Select the country column using bracket notation.
reviews['country']

# Select the first country value.
reviews['country'][0]


# ==========================================
# 3. INDEX-BASED SELECTION: ILOC
# ==========================================

# Select the first row.
reviews.iloc[0]

# Select all rows from the first column.
reviews.iloc[:, 0]

# Select the first three rows from the first column.
reviews.iloc[:3, 0]

# Select the second and third rows from the first column.
reviews.iloc[1:3, 0]

# Select specific row positions from the first column.
reviews.iloc[[0, 1, 2], 0]

# Select the last five rows.
reviews.iloc[-5:]


# ==========================================
# 4. LABEL-BASED SELECTION: LOC
# ==========================================

# Select the country value at row label 0.
reviews.loc[0, 'country']

# Select three specific columns from all rows.
reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]


# ==========================================
# 5. LOC VS ILOC
# ==========================================

# iloc excludes the ending position.
reviews.iloc[0:10]

# loc includes the ending label.
reviews.loc[0:10]


# ==========================================
# 6. CHANGE THE DATAFRAME INDEX
# ==========================================

# Use the wine title as the row index.
reviews.set_index("title")


# ==========================================
# 7. CONDITIONAL SELECTION
# ==========================================

# Find wines produced in Italy.
reviews.country == 'Italy'

# Select Italian wines.
reviews.loc[reviews.country == 'Italy']

# Select Italian wines rated at least 90 points.
reviews.loc[
    (reviews.country == 'Italy') &
    (reviews.points >= 90)
]

# Select wines produced in Italy OR rated at least 90.
reviews.loc[
    (reviews.country == 'Italy') |
    (reviews.points >= 90)
]


# ==========================================
# 8. SELECT VALUES USING ISIN()
# ==========================================

# Select wines from Italy or France.
reviews.loc[
    reviews.country.isin(['Italy', 'France'])
]


# ==========================================
# 9. SELECT MISSING OR NON-MISSING VALUES
# ==========================================

# Select wines with a recorded price.
reviews.loc[reviews.price.notnull()]

# Select wines without a recorded price.
reviews.loc[reviews.price.isnull()]


# ==========================================
# 10. ASSIGN NEW COLUMNS
# ==========================================

# Add a column containing the same value in every row.
reviews['critic'] = 'everyone'

# Add a column with descending numbers.
reviews['index_backwards'] = range(len(reviews), 0, -1)

# Display the new columns.
reviews[['critic', 'index_backwards']]


# ==================================================
# PANDAS: SUMMARY FUNCTIONS AND MAPS
# ==================================================


# ==========================================
# 1. IMPORT LIBRARIES AND LOAD DATA
# ==========================================

# Import pandas and NumPy.
import pandas as pd
import numpy as np

# Limit displayed rows.
pd.set_option('display.max_rows', 5)

# Load the wine reviews dataset.
reviews = pd.read_csv("/content/code_data/code_data/winemag-data-130k-v2.csv", index_col=0)


# ==========================================
# 2. SUMMARY FUNCTIONS
# ==========================================

# Generate summary statistics for numerical data.
reviews.points.describe()

# Generate summary statistics for text data.
reviews.taster_name.describe()

# Calculate the average wine rating.
reviews.points.mean()

# Find all unique taster names.
reviews.taster_name.unique()

# Count the occurrences of each taster name.
reviews.taster_name.value_counts()


# ==========================================
# 3. MAP()
# ==========================================

# Calculate the average points value.
review_points_mean = reviews.points.mean()

# Subtract the average from each wine score.
# map() applies the lambda function to each Series value.
reviews.points.map(lambda p: p - review_points_mean)


# ==========================================
# 4. APPLY()
# ==========================================

# Define a function that modifies a row's points value.
def remean_points(row):
    row.points = row.points - review_points_mean
    return row


# Apply the function to every row.
# axis='columns' processes rows individually.
reviews.apply(remean_points, axis='columns')


# ==========================================
# 5. CHECK THE ORIGINAL DATA
# ==========================================

# Display the first row.
# The original DataFrame remains unchanged by map() and apply()
# unless their results are assigned back to it.
reviews.head(1)


# ==========================================
# 6. BUILT-IN ARITHMETIC OPERATIONS
# ==========================================

# Subtract the mean from every points value.
reviews.points - review_points_mean

# Combine country and region information.
reviews.country + " - " + reviews.region_1


# ==================================================
# PANDAS: GROUPING AND SORTING
# ==================================================


# ==========================================
# 1. IMPORT PANDAS AND LOAD DATA
# ==========================================

import pandas as pd

# Load the wine reviews dataset.
reviews = pd.read_csv("/content/code_data/code_data/winemag-data-130k-v2.csv", index_col=0)

# Limit displayed rows.
pd.set_option("display.max_rows", 5)


# ==========================================
# 2. GROUPING DATA
# ==========================================

# Count the number of wines in each points category.
reviews.groupby('points').points.count()

# Find the minimum price for each points category.
reviews.groupby('points').price.min()


# ==========================================
# 3. GROUPBY() WITH APPLY()
# ==========================================

# Get the first wine title from each winery.
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])

# Find the highest-rated wine for each country and province combination.
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])


# ==========================================
# 4. GROUPBY() WITH AGG()
# ==========================================

# Calculate the number of wines, minimum price and maximum price for each country.
reviews.groupby(['country']).price.agg([len, min, max])


# ==========================================
# 5. MULTI-INDEX
# ==========================================

# Group by country and province.
# Count the number of reviews in each group.
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])

# Inspect the MultiIndex.
mi = countries_reviewed.index
type(mi)

# Convert the MultiIndex into regular columns.
countries_reviewed = countries_reviewed.reset_index()


# ==========================================
# 6. SORTING
# ==========================================

# Sort by number of reviews, smallest first.
countries_reviewed.sort_values(by='len')

# Sort by number of reviews, largest first.
countries_reviewed.sort_values(by='len', ascending=False)

# Sort by index labels.
countries_reviewed.sort_index()

# Sort by country and then number of reviews.
countries_reviewed.sort_values(by=['country', 'len'])


# ==================================================
# PANDAS: DATA TYPES AND MISSING VALUES
# ==================================================


# ============================================================
# 1. IMPORT PANDAS AND LOAD THE DATASET
# ============================================================

import pandas as pd

# Load the wine reviews dataset
# index_col=0 uses the first column as the DataFrame index
reviews = pd.read_csv("/content/code_data/code_data/winemag-data-130k-v2.csv", index_col=0)

# Limit displayed rows
pd.set_option('display.max_rows', 5)


# ============================================================
# 2. DATA TYPES
# ============================================================

# Get the data type of the 'price' column
reviews.price.dtype

# Get the data types of all DataFrame columns
reviews.dtypes

# Convert the 'points' column to float64
reviews.points.astype('float64')

# Get the data type of the DataFrame index
reviews.index.dtype


# ============================================================
# 3. FIND MISSING VALUES
# ============================================================

# Select rows where 'country' has missing values
reviews[pd.isnull(reviews.country)]

# Select rows where 'country' does not have missing values
reviews[pd.notnull(reviews.country)]


# ============================================================
# 4. REPLACE MISSING VALUES
# ============================================================

# Replace missing values in 'region_2' with "Unknown"
reviews.region_2.fillna("Unknown")

# Fill missing values using the next available non-null value
# This is the backfill strategy
reviews.region_2.fillna(method='bfill')


# ============================================================
# 5. REPLACE EXISTING VALUES
# ============================================================

# Replace the old Twitter handle with the new one
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")


# ==================================================
# PANDAS: RENAMING AND COMBINING
# ==================================================


# ============================================================
# 1. IMPORT PANDAS AND LOAD THE WINE REVIEWS DATASET
# ============================================================

import pandas as pd

# Limit the number of rows displayed
pd.set_option('display.max_rows', 5)

# Load the wine reviews dataset
# Use the first column as the DataFrame index
reviews = pd.read_csv("/content/code_data/code_data/winemag-data-130k-v2.csv", index_col=0)


# ============================================================
# 2. RENAME COLUMNS
# ============================================================

# Rename the 'points' column to 'score'
reviews.rename(columns={'points': 'score'})


# ============================================================
# 3. RENAME INDEX VALUES
# ============================================================

# Rename selected index values
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})


# ============================================================
# 4. RENAME INDEX AND COLUMN AXIS NAMES
# ============================================================

# Rename the row index axis to 'wines'
# Rename the column axis to 'fields'
reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')


# ============================================================
# 5. LOAD AND COMBINE DATAFRAMES USING CONCAT
# ============================================================

# Load Canadian YouTube trending videos
canadian_youtube = pd.read_csv("/content/code_data/code_data/CAvideos.csv")

# Load British YouTube trending videos
british_youtube = pd.read_csv("/content/code_data/code_data/GBvideos.csv")

# Combine the two DataFrames vertically
youtube_combined = pd.concat([canadian_youtube, british_youtube])


# ============================================================
# 6. COMBINE DATAFRAMES USING JOIN
# ============================================================

# Create a multi-level index for the Canadian dataset
left = canadian_youtube.set_index(['title', 'trending_date'])

# Create the same multi-level index for the British dataset
right = british_youtube.set_index(['title', 'trending_date'])

# Join the DataFrames using their shared index
# Add suffixes to distinguish columns with identical names
youtube_joined = left.join(right, lsuffix='_CAN', rsuffix='_UK')


# pip install fuzzywuzzy


# ==================================================
# DATA CLEANING: HANDLING MISSING VALUES
# ==================================================


# ============================================================
# 1. IMPORT LIBRARIES AND LOAD THE DATASET
# ============================================================

import pandas as pd
import numpy as np

# Load the NFL play-by-play dataset
nfl_data = pd.read_csv(
    "/content/code_data/code_data/NFL Play by Play 2009-2017 (v4).csv"
)

# Set a random seed for reproducibility
np.random.seed(0)


# ============================================================
# 2. INSPECT THE DATASET
# ============================================================

# Display the first five rows
nfl_data.head()


# ============================================================
# 3. COUNT MISSING VALUES
# ============================================================

# Count missing values in each column
missing_values_count = nfl_data.isnull().sum()

# Display counts for the first ten columns
missing_values_count[0:10]


# ============================================================
# 4. CALCULATE THE PERCENTAGE OF MISSING DATA
# ============================================================

# Calculate the total number of cells
total_cells = nfl_data.size

# Calculate the total number of missing values
total_missing = missing_values_count.sum()

# Calculate the percentage of missing values
percent_missing = (total_missing / total_cells) * 100

# Print the result
print(percent_missing)


# ============================================================
# 5. INVESTIGATE MISSING VALUES
# ============================================================

# Inspect missing-value counts in the first ten columns
missing_values_count[0:10]

# Find rows where 'down' is missing
nfl_data[nfl_data['down'].isnull()]

# Find rows where 'PenalizedTeam' is missing
nfl_data[nfl_data['PenalizedTeam'].isnull()]


# ============================================================
# 6. DROP ROWS WITH MISSING VALUES
# ============================================================

# Remove rows containing at least one missing value
nfl_data.dropna()


# ============================================================
# 7. DROP COLUMNS WITH MISSING VALUES
# ============================================================

# Remove columns containing at least one missing value
columns_with_na_dropped = nfl_data.dropna(axis=1)

# Display the first five rows
columns_with_na_dropped.head()

# Compare the number of columns before and after dropping
print("Columns in original dataset: %d \n" % nfl_data.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])


# ============================================================
# 8. SELECT A SUBSET OF THE DATASET
# ============================================================

# Select columns from 'EPA' to 'Season'
# Keep only the first five rows
subset_nfl_data = nfl_data.loc[:, 'EPA':'Season'].head()

# Display the subset
subset_nfl_data


# ============================================================
# 9. FILL MISSING VALUES WITH ZERO
# ============================================================

# Replace all missing values with 0
subset_nfl_data.fillna(0)


# ============================================================
# 10. FILL MISSING VALUES USING BACKFILL
# ============================================================

# Fill missing values with the next non-null value below them
# Fill any remaining missing values with 0
subset_nfl_data.fillna(method='bfill', axis=0).fillna(0)


# ==================================================
# DATA CLEANING: SCALING AND NORMALIZATION
# ==================================================



# ============================================================
# 1. IMPORT LIBRARIES AND SET UP THE ENVIRONMENT
# ============================================================

# Data manipulation
import pandas as pd

# Numerical operations
import numpy as np

# Box-Cox statistical transformation
from scipy import stats

# Min-Max scaling
from mlxtend.preprocessing import minmax_scaling

# Data visualisation
import seaborn as sns
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(0)


# ============================================================
# 2. GENERATE SAMPLE DATA
# ============================================================

# Generate 1,000 random values from an exponential distribution
original_data = np.random.exponential(size=1000)


# ============================================================
# 3. SCALE DATA USING MIN-MAX SCALING
# ============================================================

# Transform the data to a range between 0 and 1
scaled_data = minmax_scaling(original_data, columns=[0])


# ============================================================
# 4. VISUALISE ORIGINAL AND SCALED DATA
# ============================================================

# Create two plots side by side
fig, ax = plt.subplots(1, 2, figsize=(15, 3))

# Plot original data
sns.histplot(original_data, ax=ax[0], kde=True, legend=False)
ax[0].set_title("Original Data")

# Plot scaled data
sns.histplot(scaled_data, ax=ax[1], kde=True, legend=False)
ax[1].set_title("Scaled data")

# Display the plots
plt.show()


# ============================================================
# 5. NORMALIZE DATA USING BOX-COX TRANSFORMATION
# ============================================================

# Apply the Box-Cox transformation
# The result contains the transformed data and the estimated lambda
normalized_data = stats.boxcox(original_data)


# ============================================================
# 6. VISUALISE ORIGINAL AND NORMALIZED DATA
# ============================================================

# Create two plots side by side
fig, ax = plt.subplots(1, 2, figsize=(15, 3))

# Plot original data
sns.histplot(original_data, ax=ax[0], kde=True, legend=False)
ax[0].set_title("Original Data")

# Plot normalized data
# Index [0] selects the transformed values
sns.histplot(normalized_data[0], ax=ax[1], kde=True, legend=False)
ax[1].set_title("Normalized data")

# Display the plots
plt.show()


# ==================================================
# DATA CLEANING: PARSING DATES
# ==================================================


# ============================================================
# 1. IMPORT LIBRARIES AND LOAD THE DATASET
# ============================================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# Load the landslides dataset
landslides = pd.read_csv("/content/code_data/code_data/catalog.csv")

# Set a random seed for reproducibility
np.random.seed(0)


# ============================================================
# 2. INSPECT THE DATASET
# ============================================================

# Display the first five rows
landslides.head()

# Display the first five dates
print(landslides['date'].head())

# Check the data type of the date column
landslides['date'].dtype


# ============================================================
# 3. PARSE DATES
# ============================================================

# Convert the date column from strings to datetime objects
# %m = month, %d = day, %y = two-digit year
landslides['date_parsed'] = pd.to_datetime(landslides['date'], format="%m/%d/%y")

# Display the first five parsed dates
landslides['date_parsed'].head()


# ============================================================
# 4. ALTERNATIVE: AUTOMATIC DATE FORMAT INFERENCE
# ============================================================

# Let pandas attempt to infer the date format
# Use this alternative when the format is not known
# This replaces the previously parsed date column
# landslides['date_parsed'] = pd.to_datetime(
#     landslides['date'],
#     infer_datetime_format=True
# )


# ============================================================
# 5. EXTRACT THE DAY OF THE MONTH
# ============================================================

# Extract the day from each parsed date
day_of_month_landslides = landslides['date_parsed'].dt.day

# Display the first five values
day_of_month_landslides.head()


# ============================================================
# 6. REMOVE MISSING VALUES
# ============================================================

# Remove missing values from the extracted days
day_of_month_landslides = day_of_month_landslides.dropna()


# ============================================================
# 7. VISUALISE THE DISTRIBUTION
# ============================================================

# Plot a histogram of the days of the month
sns.histplot(day_of_month_landslides, bins=31, kde=False)

# Display the histogram
plt.show()



# ============================================================
# DATA CLEANING: CHARACTER ENCODINGS
# ============================================================


# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import numpy as np
import charset_normalizer

# Set seed for reproducibility
np.random.seed(0)


# 2. STRINGS AND BYTES
# ------------------------------------------------------------

# Create a string containing a euro symbol
before = "This is the euro symbol: €"

# Check the data type
print(type(before))  # str

# Encode the string using UTF-8
after = before.encode("utf-8", errors="replace")

# Check the resulting data type
print(type(after))  # bytes

# Inspect the encoded bytes
print(after)

# Decode the bytes using the correct encoding
print(after.decode("utf-8"))


# 3. WRONG ENCODING EXAMPLE
# ------------------------------------------------------------

# ASCII cannot decode the UTF-8 bytes for the euro symbol.
# Uncomment to see the UnicodeDecodeError.

# print(after.decode("ascii"))


# 4. CHARACTER LOSS EXAMPLE
# ------------------------------------------------------------

before = "This is the euro symbol: €"

# ASCII cannot represent the euro symbol.
# The replacement character '?' is used instead.
after = before.encode("ascii", errors="replace")

# The original euro symbol cannot be recovered.
print(after.decode("ascii"))


# 5. DETECT FILE ENCODING
# ------------------------------------------------------------

file_path = "/content/code_data/code_data/ks-projects-201612.csv"

# Open the file in binary mode and inspect its first 10,000 bytes
with open(file_path, "rb") as rawdata:
    result = charset_normalizer.detect(rawdata.read(10000))

# Display the estimated encoding
print(result)


# 6. READ THE FILE WITH THE DETECTED ENCODING
# ------------------------------------------------------------

# Use the likely encoding identified by charset_normalizer.
# The lesson's example reports Windows-1252.
kickstarter_2016 = pd.read_csv(file_path, encoding="Windows-1252")

# Inspect the first five rows
print(kickstarter_2016.head())


# 7. SAVE THE DATA USING UTF-8
# ------------------------------------------------------------

kickstarter_2016.to_csv("ks-projects-201801-utf8.csv", encoding="utf-8", index=False)


# ============================================================
# DATA CLEANING: INCONSISTENT DATA ENTRY
# ============================================================

# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import numpy as np

import fuzzywuzzy
from fuzzywuzzy import process

import charset_normalizer

# Set seed for reproducibility
np.random.seed(0)


# 2. LOAD THE DATASET
# ------------------------------------------------------------

professors = pd.read_csv("/content/code_data/code_data/pakistan_intellectual_capital.csv")

# Inspect the first five rows
print(professors.head())


# 3. INSPECT UNIQUE COUNTRY VALUES
# ------------------------------------------------------------

countries = professors["Country"].unique()

# Sort and display unique values
countries.sort()
print(countries)


# 4. STANDARDISE TEXT
# ------------------------------------------------------------

# Convert country names to lowercase
professors["Country"] = professors["Country"].str.lower()

# Remove leading and trailing whitespace
professors["Country"] = professors["Country"].str.strip()

# Inspect the cleaned unique values
countries = professors["Country"].unique()
countries.sort()

print(countries)


# 5. FIND SIMILAR STRINGS
# ------------------------------------------------------------

# Find the 10 closest matches to "south korea"
matches = fuzzywuzzy.process.extract("south korea", countries, limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

# Display matching strings and similarity scores
print(matches)


# 6. CREATE A REUSABLE FUZZY-MATCHING FUNCTION
# ------------------------------------------------------------

def replace_matches_in_column(df, column, string_to_match, min_ratio=47):

    # Get unique strings from the selected column
    strings = df[column].unique()

    # Find the closest matches
    matches = fuzzywuzzy.process.extract(string_to_match, strings, limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # Filter matches using the minimum similarity threshold
    close_matches = [match[0] for match in matches if match[1] >= min_ratio]

    # Identify rows containing the matching values
    rows_with_matches = df[column].isin(close_matches)

    # Replace matching values with the standard value
    df.loc[rows_with_matches, column] = string_to_match

    print("All done!")


# 7. APPLY FUZZY MATCHING
# ------------------------------------------------------------

replace_matches_in_column(df=professors, column="Country", string_to_match="south korea")


# 8. VERIFY THE RESULTS
# ------------------------------------------------------------

countries = professors["Country"].unique()

# Sort the cleaned country names
countries.sort()

# Display the final unique values
print(countries)


# ============================================================
# DATA VISUALIZATION: HELLO, SEABORN
# ============================================================


# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

# Pandas: data manipulation
import pandas as pd

# Register date converters for matplotlib
pd.plotting.register_matplotlib_converters()

# Matplotlib: chart creation and customisation
import matplotlib.pyplot as plt

# Display charts inside Jupyter notebooks
%matplotlib inline

# Seaborn: statistical data visualisation
import seaborn as sns

print("Setup Complete")


# 2. LOAD THE DATASET
# ------------------------------------------------------------

# Specify the location of the CSV file
fifa_filepath = "/content/code_data/code_data/fifa.csv"

# Read the CSV file into a DataFrame
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)


# 3. EXAMINE THE DATA
# ------------------------------------------------------------

# Display the first five rows
print(fifa_data.head())


# 4. CREATE A LINE CHART
# ------------------------------------------------------------

# Set the figure dimensions (width, height)
plt.figure(figsize=(16, 6))

# Create a line chart showing rankings over time
sns.lineplot(data=fifa_data)

# Display the chart
plt.show()


# ============================================================
# DATA VISUALIZATION: LINE CHARTS
# ============================================================


# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd

# Register date converters for matplotlib
pd.plotting.register_matplotlib_converters()

import matplotlib.pyplot as plt

# Display plots inside Jupyter notebooks
%matplotlib inline

import seaborn as sns

print("Setup Complete")


# 2. LOAD THE DATASET
# ------------------------------------------------------------

# Specify the CSV file path
spotify_filepath = "/content/code_data/code_data/spotify.csv"

# Load the dataset
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)


# 3. EXAMINE THE DATA
# ------------------------------------------------------------

# Display the first five rows
print(spotify_data.head())

# Display the last five rows
print(spotify_data.tail())

# Display all column names
print(list(spotify_data.columns))


# 4. PLOT ALL SONGS
# ------------------------------------------------------------

# Set chart dimensions
plt.figure(figsize=(14, 6))

# Create a line chart for every song
sns.lineplot(data=spotify_data)

# Add chart title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

# Display chart
plt.show()


# 5. PLOT SELECTED SONGS
# ------------------------------------------------------------

# Create a new figure
plt.figure(figsize=(14, 6))

# Add chart title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

# Plot Shape of You
sns.lineplot(data=spotify_data["Shape of You"], label="Shape of You")

# Plot Despacito
sns.lineplot(data=spotify_data["Despacito"], label="Despacito")

# Label the horizontal axis
plt.xlabel("Date")

# Label the vertical axis
plt.ylabel("Daily Streams")

# Display chart
plt.show()


# ============================================================
# DATA VISUALIZATION: BAR CHARTS AND HEATMAPS
# ============================================================


# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Register Matplotlib date converters
pd.plotting.register_matplotlib_converters()

# Jupyter Notebook only
%matplotlib inline


# 2. LOAD THE DATASET
# ------------------------------------------------------------

# Path to the flight delays CSV file
flight_filepath = "/content/code_data/code_data/flight_delays.csv"

# Load the dataset and use Month as the index
flight_data = pd.read_csv(flight_filepath, index_col="Month")


# 3. EXPLORE THE DATASET
# ------------------------------------------------------------

# Display the first five rows
print(flight_data.head())

# Display the last five rows
print(flight_data.tail())

# Display airline column names
print(list(flight_data.columns))

# Display the complete dataset
print(flight_data)


# 4. BAR CHART: SPIRIT AIRLINES
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

sns.barplot(x=flight_data.index, y=flight_data["NK"])

plt.ylabel("Arrival delay (in minutes)")

plt.show()


# 5. HEATMAP: ALL AIRLINES
# ------------------------------------------------------------

plt.figure(figsize=(14, 7))

plt.title("Average Arrival Delay for Each Airline, by Month")

sns.heatmap(data=flight_data, annot=True)

plt.xlabel("Airline")

plt.show()


# ============================================================
# DATA VISUALIZATION: SCATTER PLOTS
# ============================================================


# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Register Matplotlib date converters
pd.plotting.register_matplotlib_converters()

# Jupyter Notebook only
%matplotlib inline


# 2. LOAD THE DATASET
# ------------------------------------------------------------

insurance_filepath = "/content/code_data/code_data/insurance.csv"

insurance_data = pd.read_csv(insurance_filepath)


# 3. EXAMINE THE DATA
# ------------------------------------------------------------

# Display the first five rows
print(insurance_data.head())


# 4. SIMPLE SCATTER PLOT
# ------------------------------------------------------------

# Investigate the relationship between BMI and charges
sns.scatterplot(x=insurance_data["bmi"], y=insurance_data["charges"])

plt.title("BMI vs Insurance Charges")
plt.show()


# 5. SCATTER PLOT WITH REGRESSION LINE
# ------------------------------------------------------------

sns.regplot(x=insurance_data["bmi"], y=insurance_data["charges"])

plt.title("BMI vs Insurance Charges with Regression Line")
plt.show()


# 6. COLOUR-CODED SCATTER PLOT
# ------------------------------------------------------------

# Use smoking status to distinguish customers
sns.scatterplot(x=insurance_data["bmi"], y=insurance_data["charges"], hue=insurance_data["smoker"])

plt.title("BMI vs Insurance Charges by Smoking Status")
plt.show()


# 7. SEPARATE REGRESSION LINES
# ------------------------------------------------------------

# Create a regression line for each smoking group
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)

plt.show()


# 8. CATEGORICAL SCATTER PLOT
# ------------------------------------------------------------

# Compare charges between smokers and non-smokers
sns.swarmplot(x=insurance_data["smoker"], y=insurance_data["charges"])

plt.title("Insurance Charges: Smokers vs Non-Smokers")
plt.show()


# 9. ALTERNATIVE: STRIP PLOT
# ------------------------------------------------------------

# Useful when a swarm plot is too crowded
sns.stripplot(x=insurance_data["smoker"], y=insurance_data["charges"], alpha=0.5, jitter=True)

plt.title("Insurance Charges: Smokers vs Non-Smokers")
plt.show()



# ============================================================
# DATA VISUALIZATION: DISTRIBUTIONS
# ============================================================


# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Register Matplotlib date converters
pd.plotting.register_matplotlib_converters()

# Jupyter Notebook only
%matplotlib inline


# 2. LOAD THE DATASET
# ------------------------------------------------------------

# Path to the CSV file
iris_filepath = "/content/code_data/code_data/iris.csv"

# Load the dataset using Id as the index
iris_data = pd.read_csv(iris_filepath, index_col="Id")


# 3. EXAMINE THE DATA
# ------------------------------------------------------------

# Display the first five rows
print(iris_data.head())


# 4. HISTOGRAM
# ------------------------------------------------------------

# Visualise the distribution of petal lengths
sns.histplot(iris_data["Petal Length (cm)"])

plt.title("Distribution of Iris Petal Lengths")
plt.show()


# 5. KDE PLOT
# ------------------------------------------------------------

# Create a smoothed distribution curve
sns.kdeplot(data=iris_data["Petal Length (cm)"], fill=True)

plt.title("KDE Distribution of Iris Petal Lengths")
plt.show()


# 6. TWO-DIMENSIONAL KDE PLOT
# ------------------------------------------------------------

# Compare petal length and sepal width
sns.jointplot(x=iris_data["Petal Length (cm)"], y=iris_data["Sepal Width (cm)"], kind="kde")

plt.show()


# 7. HISTOGRAMS BY SPECIES
# ------------------------------------------------------------

# Compare petal length distributions across species
sns.histplot(data=iris_data, x="Petal Length (cm)", hue="Species")

plt.title("Histogram of Petal Lengths, by Species")
plt.show()


# 8. KDE PLOTS BY SPECIES
# ------------------------------------------------------------

# Compare smoothed distributions across species
sns.kdeplot(data=iris_data, x="Petal Length (cm)", hue="Species", fill=True)

plt.title("Distribution of Petal Lengths, by Species")
plt.show()


# ============================================================
# DATA VISUALIZATION: CHOOSING PLOT TYPES AND CUSTOM STYLES
# ============================================================


# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Register Matplotlib date converters
pd.plotting.register_matplotlib_converters()

# Jupyter Notebook only
%matplotlib inline


# 2. LOAD THE SPOTIFY DATASET
# ------------------------------------------------------------

spotify_filepath = "/content/code_data/code_data/spotify.csv"

spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# Examine the dataset
print(spotify_data.head())


# 3. LINE CHART: DEFAULT STYLE
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

sns.lineplot(data=spotify_data)

plt.title("Spotify Streams Over Time")
plt.xlabel("Date")
plt.show()


# 4. CHANGE THE STYLE TO DARK
# ------------------------------------------------------------

sns.set_style("dark")

plt.figure(figsize=(12, 6))

sns.lineplot(data=spotify_data)

plt.title("Spotify Streams Over Time - Dark Theme")
plt.xlabel("Date")
plt.show()


# 5. EXPERIMENT WITH OTHER THEMES
# ------------------------------------------------------------

# Dark background with gridlines
sns.set_style("darkgrid")

plt.figure(figsize=(12, 6))
sns.lineplot(data=spotify_data)
plt.title("Dark Grid Theme")
plt.show()


# White background with gridlines
sns.set_style("whitegrid")

plt.figure(figsize=(12, 6))
sns.lineplot(data=spotify_data)
plt.title("White Grid Theme")
plt.show()


# Dark background without prominent gridlines
sns.set_style("dark")

plt.figure(figsize=(12, 6))
sns.lineplot(data=spotify_data)
plt.title("Dark Theme")
plt.show()


# Plain white background
sns.set_style("white")

plt.figure(figsize=(12, 6))
sns.lineplot(data=spotify_data)
plt.title("White Theme")
plt.show()


# White background with axis tick marks
sns.set_style("ticks")

plt.figure(figsize=(12, 6))
sns.lineplot(data=spotify_data)
plt.title("Ticks Theme")
plt.show()


# ============================================================
# DATA VISUALIZATION: FINAL PROJECT
# ============================================================


# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the default visualisation style
sns.set_style("whitegrid")


# 2. LOAD YOUR DATASET
# ------------------------------------------------------------

# Replace this path with your actual dataset path
file_path = "/content/code_data/code_data/spotify.csv"
# Read the CSV file
data = pd.read_csv(file_path)


# 3. EXPLORE THE DATA
# ------------------------------------------------------------

# Display the first five rows
print(data.head())

# Display the dataset dimensions
print("Dataset shape:", data.shape)

# Display column names
print("Columns:", list(data.columns))

# Display data types and missing values
data.info()

# Generate summary statistics
print(data.describe())

# Count missing values
print(data.isnull().sum())


# 4. DATA CLEANING
# ------------------------------------------------------------

# Optional: remove duplicate rows
data = data.drop_duplicates()

# Optional: inspect missing values
print("Missing values after inspection:")
print(data.isnull().sum())

# Add any necessary cleaning operations here.
# Do not remove or replace missing values without
# considering what they represent.


# 5. VISUALISATION 1: LINE CHART
# ------------------------------------------------------------

# Replace these column names with your own
# sns.lineplot(data=data, x="date", y="value")

# plt.title("Trend Over Time")
# plt.xlabel("Date")
# plt.ylabel("Value")
# plt.show()


# 6. VISUALISATION 2: BAR CHART
# ------------------------------------------------------------

# sns.barplot(data=data, x="category", y="value")

# plt.title("Comparison Between Categories")
# plt.xlabel("Category")
# plt.ylabel("Value")
# plt.show()


# 7. VISUALISATION 3: SCATTER PLOT
# ------------------------------------------------------------

# sns.scatterplot(data=data, x="variable_1", y="variable_2")

# plt.title("Relationship Between Variables")
# plt.xlabel("Variable 1")
# plt.ylabel("Variable 2")
# plt.show()


# 8. VISUALISATION 4: HISTOGRAM
# ------------------------------------------------------------

# sns.histplot(data=data, x="numerical_column")

# plt.title("Distribution of Values")
# plt.xlabel("Value")
# plt.show()


# 9. VISUALISATION 5: HEATMAP
# ------------------------------------------------------------

# Select numerical columns
# numeric_data = data.select_dtypes(include="number")

# Calculate correlations
# correlation = numeric_data.corr()

# Create the heatmap
# sns.heatmap(
#     data=correlation,
#     annot=True,
#     cmap="coolwarm"
# )

# plt.title("Correlation Heatmap")
# plt.show()


# ============================================================
# DATA VISUALIZATION: CREATING YOUR OWN NOTEBOOKS
# ============================================================


# ==========================================
# 1. IMPORT LIBRARIES
# ==========================================

import pandas as pd

# Register matplotlib date converters
pd.plotting.register_matplotlib_converters()

# Import plotting libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Display charts inside the notebook
%matplotlib inline


# ==========================================
# 2. CONFIRM SETUP
# ==========================================

print("Setup Complete")


# ==========================================
# 3. LOAD DATASET
# ==========================================

# Replace this path with your Kaggle dataset path
data = pd.read_csv("/content/code_data/code_data/spotify.csv")

# Inspect the dataset
print(data.head())

# Check columns and data types
print(data.info())


# ==========================================
# 4. CREATE VISUALISATION
# ==========================================

# Replace column names with your dataset columns
sns.scatterplot(data=data, x="Date", y="Despacito")

plt.title("My Data Visualisation")
plt.show()


# ==========================================
# 5. SAVE VISUALISATION
# ==========================================

# Save the figure as an image
plt.savefig("my_visualization.png", bbox_inches="tight")


# ============================================================
# ADDITIONAL CODE
# ============================================================


# ============================================================
# 1. PANDAS: LOADING AND EXPLORING A REAL DATASET
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.float_format = '{:,.2f}'.format

# Load the retail transactions dataset
datafile_name = "/content/code_data/code_data/urban_wear_transactions.csv"
abt = pd.read_csv(datafile_name, index_col=0)

# Explore the DataFrame
print(abt.shape)
print(abt.head(10))
print(abt.info())
print(abt.describe())

# Access rows and columns using loc and iloc
print(abt.loc["T_ID_579441"])
print(abt.iloc[0])
print(abt.iloc[0:5, 0:4])

# Access a specific value
print(abt.loc["T_ID_579441", "Prod_Cat"])

# Modify a specific value
# Example:
# abt.loc["T_ID_579441", "Discount"] = 5.00


# ============================================================
# 2. FREQUENCY TABLES AND CROSS-TABULATIONS
# ============================================================

# Frequency of each product category
print(abt["Prod_Cat"].value_counts())

# Frequency of marketing campaigns
print(abt["Campaign"].value_counts())

# Cross-tabulation: product category and campaign
category_campaign = pd.crosstab(
    abt["Prod_Cat"],
    abt["Campaign"]
)

print(category_campaign)

# Cross-tabulation with percentages
category_campaign_percentage = pd.crosstab(
    abt["Prod_Cat"],
    abt["Campaign"],
    normalize="all"
)

print(category_campaign_percentage)

# Include row and column totals
category_campaign_totals = pd.crosstab(
    abt["Prod_Cat"],
    abt["Campaign"],
    margins=True
)

print(category_campaign_totals)


# ============================================================
# 3. PIVOT TABLES
# ============================================================

# Average total profit by product category
pivot_profit = pd.pivot_table(
    abt,
    values="Total_Profit",
    index="Prod_Cat",
    aggfunc="mean"
)

print(pivot_profit)

# Average total profit by product category and campaign
pivot_campaign = pd.pivot_table(
    abt,
    values="Total_Profit",
    index="Prod_Cat",
    columns="Campaign",
    aggfunc="mean"
)

print(pivot_campaign)

# Multiple aggregation functions
pivot_summary = pd.pivot_table(
    abt,
    values="Total_Profit",
    index="Prod_Cat",
    aggfunc=["mean", "min", "max", "median"]
)

print(pivot_summary)

# Multiple values and aggregation functions
pivot_multiple = pd.pivot_table(
    abt,
    values=["Total_Profit", "Total_Product_Sale"],
    index="Prod_Cat",
    aggfunc=["mean", "sum"]
)

print(pivot_multiple)


# ============================================================
# 4. FILTERING AND SAMPLING DATA
# ============================================================

# Filter transactions belonging to the Women category
women_transactions = abt[abt["Prod_Cat"] == "Women"]

print(women_transactions.head())

# Filter transactions with a total profit greater than 50
high_profit = abt[abt["Total_Profit"] > 50]

print(high_profit.head())

# Combine multiple filtering conditions
high_profit_women = abt[
    (abt["Prod_Cat"] == "Women") &
    (abt["Total_Profit"] > 50)
]

print(high_profit_women.head())

# Filter transactions using isin()
selected_categories = abt[
    abt["Prod_Cat"].isin(["Women", "Men"])
]

print(selected_categories.head())

# Random sample of 10 transactions
print(abt.sample(n=10, random_state=42))

# Random sample containing 20% of the transactions
print(abt.sample(frac=0.20, random_state=42))


# ============================================================
# 5. CREATING AND RECODING VARIABLES
# ============================================================

# Create a new variable representing total revenue
abt["Revenue"] = abt["Price_Per_Unit"] * abt["Quant"]

# Create a Boolean variable
abt["High_Profit"] = abt["Total_Profit"] > 25

# Create a categorical variable using np.where()
abt["Profit_Category"] = np.where(
    abt["Total_Profit"] > 25,
    "High Profit",
    "Low Profit"
)

# Replace existing values
abt["Campaign"] = abt["Campaign"].replace({
    "No Campaign": "None",
    "New Customer Offer": "New Customer"
})

# Check the new variables
print(abt[[
    "Total_Profit",
    "Revenue",
    "High_Profit",
    "Profit_Category"
]].head())


# ============================================================
# 6. GROUPING AND AGGREGATION
# ============================================================

# Group by marketing campaign and calculate average profit
abt_grp1 = abt.groupby(["Campaign"])

print(
    abt_grp1["Total_Profit"].agg(["mean"])
)

# Group by sale status and calculate summary statistics
abt_grp2 = abt.groupby(["On_Sale"])

print(
    abt_grp2["Total_Profit"].agg(["min", "max", "median"])
)

# Group by product category and calculate total profit
abt_grp3 = abt.groupby(["Prod_Cat"])

category_profit = abt_grp3["Total_Profit"].sum()

print(category_profit)

# Display the results using a bar chart
category_profit.plot(
    kind="bar",
    figsize=(7, 4),
    ylabel="Overall Total Profit",
    xlabel="Product Category",
    rot=0
)

plt.show()

# Multiple aggregation functions for several columns
group_summary = abt.groupby("Prod_Cat").agg({
    "Total_Profit": ["mean", "sum", "min", "max"],
    "Total_Product_Sale": ["mean", "sum"],
    "Quant": ["sum", "mean"]
})

print(group_summary)

# Count transactions by date and product category
daily_category_counts = (
    abt.groupby("Transaction_Date")["Prod_Cat"]
    .value_counts()
    .reset_index()
)

print(daily_category_counts)


# ============================================================
# 7. RESHAPING DATA: PIVOT AND MELT
# ============================================================

# Create a wide-format table showing transaction counts
short_wide_counts = pd.crosstab(
    abt["Transaction_Date"],
    abt["Prod_Cat"]
)

# Replace missing values with zero
short_wide_counts = short_wide_counts.fillna(0)

print(short_wide_counts.head(10))

# Reset the index to restore Transaction_Date as a column
short_wide_counts = short_wide_counts.reset_index()

# Convert wide-format data into long-format data
long_skinny_counts = pd.melt(
    short_wide_counts,
    id_vars=["Transaction_Date"],
    value_vars=["Children", "Homeware", "Men", "Women"],
    var_name="Prod_Cat",
    value_name="Count"
)

print(long_skinny_counts.head(10))

# Convert long-format data back into wide format
wide_counts_again = long_skinny_counts.pivot(
    index="Transaction_Date",
    columns="Prod_Cat",
    values="Count"
)

print(wide_counts_again.head(10))


# ============================================================
# 8. COMBINING DATAFRAMES
# ============================================================

# Concatenate DataFrames vertically
# dataframe1 and dataframe2 must already exist.
#
# combined_data = pd.concat(
#     [dataframe1, dataframe2],
#     axis=0
# )

# Concatenate DataFrames horizontally
#
# combined_columns = pd.concat(
#     [dataframe1, dataframe2],
#     axis=1
# )

# Join DataFrames using their index
#
# joined_data = dataframe1.join(
#     dataframe2,
#     how="left"
# )


# ============================================================
# 9. ADVANCED DATA VISUALISATION WITH SEABORN
# ============================================================

# Load the cleaned retail transactions dataset
datafile_name = "/content/code_data/code_data/urban_wear_transactions_clean.csv"
abt = pd.read_csv(datafile_name, index_col=0)

# Parallel box plots: total product sales by category
plt.figure(figsize=(8, 4.5))

sns.boxplot(
    data=abt,
    y="Total_Product_Sale",
    x="Prod_Cat"
)

plt.show()

# Box plots with different colours
plt.figure(figsize=(8, 4.5))

sns.boxplot(
    data=abt,
    y="Total_Product_Sale",
    x="Prod_Cat",
    hue="Prod_Cat",
    palette="Set2",
    width=0.7
)

plt.show()

# Total profit by product category
sns.boxplot(
    data=abt,
    y="Total_Profit",
    x="Prod_Cat",
    hue="Prod_Cat",
    palette="Set3"
)

plt.show()

# Total profit by campaign and product category
sns.boxplot(
    data=abt,
    y="Total_Profit",
    x="Campaign",
    hue="Prod_Cat",
    palette="Set3"
)

plt.show()


# ============================================================
# 10. SMALL MULTIPLE HISTOGRAMS
# ============================================================

# Distribution of total product sales by product category
sns.displot(
    data=abt,
    x="Total_Product_Sale",
    col="Prod_Cat",
    height=3
)

plt.show()

# Histograms with multiple plots per row
sns.displot(
    data=abt,
    x="Total_Product_Sale",
    col="Prod_Cat",
    hue="Prod_Cat",
    bins=10,
    legend=False,
    col_wrap=2,
    height=2.8,
    aspect=1.5
)

plt.show()

# Distribution of total profit by product category
sns.displot(
    data=abt,
    x="Total_Profit",
    col="Prod_Cat",
    hue="Prod_Cat",
    bins=10,
    col_wrap=2,
    height=2.8,
    aspect=1.5
)

plt.show()

# Distribution of total profit by campaign
sns.displot(
    data=abt,
    x="Total_Profit",
    col="Campaign",
    hue="Campaign",
    bins=10,
    height=2.8,
    aspect=1.5
)

plt.show()


# ============================================================
# 11. SCATTER PLOTS AND PAIR PLOTS
# ============================================================

# Compare cost per unit and total product sales
plt.figure(figsize=(5.5, 4.5))

sns.scatterplot(
    data=abt,
    x="Cost_Per_Unit",
    y="Total_Product_Sale"
)

plt.show()

# Add product category as the colour variable
plt.figure(figsize=(5.5, 4.5))

sns.scatterplot(
    data=abt,
    x="Cost_Per_Unit",
    y="Total_Product_Sale",
    hue="Prod_Cat"
)

plt.show()

# Compare price and profit per unit
plt.figure(figsize=(5.5, 4.5))

sns.scatterplot(
    data=abt,
    x="Price_Per_Unit",
    y="Profit_Per_Unit"
)

plt.show()

# Add product category to the scatter plot
plt.figure(figsize=(5.5, 4.5))

sns.scatterplot(
    data=abt,
    x="Price_Per_Unit",
    y="Profit_Per_Unit",
    hue="Prod_Cat"
)

plt.show()

# Pair plot: compare several numerical variables
sns.pairplot(
    data=abt,
    vars=[
        "Total_Cost",
        "Total_Product_Sale",
        "Total_Profit"
    ],
    hue="Prod_Cat"
)

plt.show()

# Pair plot with additional numerical variables
sns.pairplot(
    data=abt,
    vars=[
        "Price_Per_Unit",
        "Profit_Per_Unit",
        "Total_Cost",
        "Total_Product_Sale",
        "Total_Profit"
    ],
    hue="Prod_Cat"
)

plt.show()


# ============================================================
# 12. SMALL MULTIPLE BAR PLOTS
# ============================================================

# Count transactions by product category and campaign
sns.catplot(
    data=abt,
    x="Prod_Cat",
    col="Campaign",
    kind="count",
    height=4,
    aspect=1.2
)

plt.show()

# Examine On_Sale and product sub-categories
sns.catplot(
    data=abt,
    x="On_Sale",
    col="Prod_Sub_Cat",
    kind="count",
    col_wrap=2,
    height=2,
    aspect=1.2
)

plt.show()

# Equivalent cross-tabulation
print(
    pd.crosstab(
        abt["Prod_Cat"],
        abt["Campaign"]
    )
)


# ============================================================
# 13. NUMPY ARRAYS: ONE-DIMENSIONAL ARRAYS
# ============================================================

# Create a one-dimensional array
a = np.array([12, 18, 4, 12, 20, 0, 37, 87])

print(a)

# Array attributes
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)

# Create an array containing floating-point values
b = np.array([0.3, 0.12, 1.4, 2.3, 4.5])

print(b)
print(b.dtype)

# Access individual elements
print(a[1])
print(a[-1])

# Modify an element
a[1] = 42

print(a)

# Slicing
print(a[3:6])
print(a[2:])
print(a[:5])

# Modify a segment of an array
a[2:] = 42

print(a)


# ============================================================
# 14. NUMPY ARRAYS: ARGMAX AND ARRAY OPERATIONS
# ============================================================

# Weekly sales
weekly_sales = np.array([
    4567, 2341, 1987, 2345, 9876, 1021, 871
])

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# Find the index of the maximum sales value
max_sales_day = weekly_sales.argmax()

print("Most sales are on", weekdays[max_sales_day])

# Sales in the second week
week_2_sales = np.array([
    3456, 1234, 908, 9762, 2134, 8643, 103
])

# Add the two arrays
combined_sales = weekly_sales + week_2_sales

print(combined_sales)

# Find the day with the highest combined sales
max_sales_day = combined_sales.argmax()

print("Most sales are on", weekdays[max_sales_day])


# ============================================================
# 15. NUMPY ARRAYS: TWO-DIMENSIONAL ARRAYS
# ============================================================

# Create a two-dimensional array
m = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(m)

# Array attributes
print(m.dtype)
print(m.ndim)
print(m.shape)
print(m.size)

# Access individual elements
print(m[0, 1])
print(m[2, 1])

# Slicing
print(m[1:3, 0:2])
print(m[1:, :2])
print(m[1, :])
print(m[:, 2])


# ============================================================
# 16. CREATING NUMPY ARRAYS WITH ZEROS AND ONES
# ============================================================

# Create an array filled with zeros
all_zeros = np.zeros((100, 100))

print(all_zeros)

# Create an array filled with ones
all_ones = np.ones((20, 100))

print(all_ones)

# Create a 9 x 9 array
pattern = np.zeros((9, 9))

print(pattern)

# Fill the middle square with 1
pattern[1:8, 1:8] = 1

print(pattern)

# Fill a smaller square with 2
pattern[2:7, 2:7] = 2

print(pattern)

# Fill an even smaller square with 3
pattern[3:6, 3:6] = 3

print(pattern)

# Change the central element to 4
pattern[4, 4] = 4

print(pattern)

# Visualise the array
plt.imshow(pattern)
plt.show()


# ============================================================
# 17. NUMPY AND PRIME NUMBERS
# ============================================================

import math

# Function to check whether a number is prime
def isPrime(n):

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n < 2:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        if n % i == 0:
            return False

    return True


# Create a 10 x 10 array
primes = np.zeros((10, 10))

counter = 1

# Check the integers from 1 to 100
for i in range(primes.shape[0]):

    for j in range(primes.shape[1]):

        if isPrime(counter):
            primes[i, j] = 1

        counter = counter + 1

print(primes)

# Visualise the prime number pattern
plt.imshow(primes)
plt.show()


# ============================================================
# 18. CONFIDENCE INTERVALS
# ============================================================

import scipy.stats as st

# Load the Titanic dataset
datafile_name = "/content/code_data/code_data/Titanic.csv"
dataset = pd.read_csv(datafile_name)

print(dataset.head(10))

# Confidence interval for the mean Age
confidenceLevel = 0.95

sampleMean = dataset["Age"].mean()
sampleStandardError = dataset["Age"].sem()

age_confidence_interval = st.norm.interval(
    confidence=confidenceLevel,
    loc=sampleMean,
    scale=sampleStandardError
)

print("95% confidence interval for Age:")
print(age_confidence_interval)

# Confidence interval for the mean Fare
confidenceLevel = 0.95

sampleMean = dataset["Fare"].mean()
sampleStandardError = dataset["Fare"].sem()

fare_confidence_interval = st.norm.interval(
    confidence=confidenceLevel,
    loc=sampleMean,
    scale=sampleStandardError
)

print("95% confidence interval for Fare:")
print(fare_confidence_interval)


# ============================================================
# 19. HYPOTHESIS TESTING: CROSS-TABULATIONS
# ============================================================

from scipy.stats import chi2_contingency

# Relationship between survival and passenger class
contingency = pd.crosstab(
    dataset["Survived"],
    dataset["Pclass"]
)

print(contingency)

# Normalised cross-tabulation
print(
    pd.crosstab(
        dataset["Survived"],
        dataset["Pclass"],
        normalize="all"
    )
)

# Cross-tabulation with totals
print(
    pd.crosstab(
        dataset["Survived"],
        dataset["Pclass"],
        margins=True
    )
)

# Normalise by rows
print(
    pd.crosstab(
        dataset["Survived"],
        dataset["Pclass"],
        margins=True,
        normalize="index"
    )
)

# Normalise by columns
print(
    pd.crosstab(
        dataset["Survived"],
        dataset["Pclass"],
        margins=True,
        normalize="columns"
    )
)

# Visualise the contingency table
plt.figure(figsize=(12, 8))

sns.heatmap(
    contingency,
    annot=True,
    cmap="Blues",
    fmt="d"
)

plt.show()


# ============================================================
# 20. CHI-SQUARE TEST OF INDEPENDENCE
# ============================================================

# H0: Survival and passenger class are independent.
# H1: Survival and passenger class are associated.

chi2_statistic, p_value, degrees_freedom, expected = (
    chi2_contingency(contingency)
)

print("The Chi-Squared Statistic is:", chi2_statistic)
print("The p-value for the test is:", p_value)
print("The Degrees of Freedom are:", degrees_freedom)

print("The expected frequencies table is:")
print(expected)

# Decision using a significance level of 0.05
alpha = 0.05

if p_value < alpha:
    print("Reject H0: there is evidence of an association.")
else:
    print("Do not reject H0: there is insufficient evidence of an association.")


# ============================================================
# 21. CHI-SQUARE TEST: SURVIVAL AND SEX
# ============================================================

contingency_sex_survived = pd.crosstab(
    dataset["Survived"],
    dataset["Sex"]
)

print(contingency_sex_survived)

# Visualise the contingency table
plt.figure(figsize=(12, 8))

sns.heatmap(
    contingency_sex_survived,
    annot=True,
    cmap="Blues",
    fmt="d"
)

plt.show()

# Normalise by columns
print(
    pd.crosstab(
        dataset["Survived"],
        dataset["Sex"],
        margins=True,
        normalize="columns"
    )
)

# Chi-square test of independence
chi2_statistic, p_value, degrees_freedom, expected = (
    chi2_contingency(contingency_sex_survived)
)

print("The Chi-Squared Statistic is:", chi2_statistic)
print("The p-value for the test is:", p_value)
print("The Degrees of Freedom are:", degrees_freedom)

print("The expected frequencies table is:")
print(expected)

# Decision
if p_value < 0.05:
    print("Reject H0: survival and sex are associated.")
else:
    print("Do not reject H0: insufficient evidence of an association.")


# ============================================================
# 22. HYPOTHESIS TESTING USING ANOVA
# ============================================================

import statsmodels.api as sm
from statsmodels.formula.api import ols

# Examine Age according to survival status
grouped_data = dataset.groupby("Survived")

print(
    grouped_data[["Age"]].describe()
)

# Visualise Age according to survival status
sns.boxplot(
    data=dataset,
    x="Survived",
    y="Age"
)

plt.show()

# H0: Mean Age is equal for the two survival groups.
# H1: Mean Age is different for the two survival groups.

# Fit an ordinary least squares model
model = ols(
    "Age ~ C(Survived)",
    data=dataset
).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(
    model,
    typ=2
)

print(anova_table)


# ============================================================
# 23. ANOVA: PASSENGER CLASS AND FARE
# ============================================================

# Examine Fare according to passenger class
grouped_data = dataset.groupby("Pclass")

print(
    grouped_data[["Fare"]].describe()
)

# Visualise Fare according to passenger class
sns.boxplot(
    data=dataset,
    x="Pclass",
    y="Fare"
)

plt.show()

# H0: Mean Fare is equal across passenger classes.
# H1: At least one passenger class has a different mean Fare.

# Fit an ordinary least squares model
model = ols(
    "Fare ~ C(Pclass)",
    data=dataset
).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(
    model,
    typ=2
)

print(anova_table)

# ============================================================
# MERGING DATAFRAMES WITH pd.merge()
# ============================================================

# Create two example DataFrames
customers = pd.DataFrame({
    "Customer_ID": [1, 2, 3, 4],
    "Customer_Name": ["Alice", "Bob", "Charlie", "David"]
})

orders = pd.DataFrame({
    "Customer_ID": [1, 2, 2, 5],
    "Order_ID": [101, 102, 103, 104],
    "Amount": [250, 150, 300, 400]
})

# 1. INNER MERGE
# Keep only rows with matching keys in both DataFrames.

inner_merge = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="inner"
)

print(inner_merge)


# 2. LEFT MERGE
# Keep all rows from the left DataFrame (customers).
# Add matching information from the right DataFrame (orders).

left_merge = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="left"
)

print(left_merge)


# 3. RIGHT MERGE
# Keep all rows from the right DataFrame (orders).

right_merge = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="right"
)

print(right_merge)


# 4. OUTER MERGE
# Keep all rows from both DataFrames.
# Unmatched values are filled with NaN.

outer_merge = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="outer"
)

print(outer_merge)


# 5. MERGE USING DIFFERENT COLUMN NAMES
# left_on and right_on specify the matching columns.

# Example:
# merged_data = pd.merge(
#     dataframe1,
#     dataframe2,
#     left_on="Customer_ID",
#     right_on="Client_ID",
#     how="inner"
# )


# 6. MERGE USING MULTIPLE KEYS

# Example:
# merged_data = pd.merge(
#     dataframe1,
#     dataframe2,
#     on=["Customer_ID", "Transaction_Date"],
#     how="inner"
# )


# 7. MERGE WITH INDICATOR
# Shows whether each row came from the left DataFrame,
# the right DataFrame, or both.

indicator_merge = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="outer",
    indicator=True
)

print(indicator_merge)


# 8. MERGE WITH SUFFIXES
# Useful when both DataFrames contain columns with the same name.

# Example:
# merged_data = pd.merge(
#     dataframe1,
#     dataframe2,
#     on="Customer_ID",
#     how="inner",
#     suffixes=("_left", "_right")
# )
