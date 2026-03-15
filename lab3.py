# %%
# CELL 1 | STUDENT CONFIGURATION
LAST_NAME = "DelRosario"
STUDENT_ID = "TUPM-25-0924"

SEED_DIGIT = int(STUDENT_ID[-4])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

print("Student:", LAST_NAME)
print("Seed Digit:", SEED_DIGIT)
print("Digit Sum:", ID_SUM)
print("Surname Length:", NAME_LENGTH)

# %%
# CELL 2 | FUNCTIONAL ENCAPSULATION
def greet():
    print("=" * 40)
    print(f"System Initialized for: {LAST_NAME}")
    print("=" * 40)

def identity_code():
    code = SEED_DIGIT * NAME_LENGTH
    return code

# Run
greet()
print("Identity Code:", identity_code())

# %%
# CELL 3 | LEGB VALIDATION
global_value = ID_SUM

def scope_test():
    global_value = SEED_DIGIT  # local variable
    print("Inside function (local):", global_value)

scope_test()
print("Outside function (global):", global_value)

# %%
# CELL 4 | PARAMETRIC PROCESSING
# Example student info (replace these with your actual values or previous cell variables)
SURNAME = "DelRosario"
STUDENT_ID = "TUPM-25-0924"
SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())

def user_summary(title, scores, **info):
    """Displays a student summary with scores, total, average, and extra info."""
    
    print(f"---- {title} ----")
    
    total = sum(scores)
    average = total / len(scores)
    
    print("Scores:", scores)
    print("Total:", total)
    print("Average:", round(average, 2))
    
    # Print extra info passed as keyword arguments
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")
    
    return average


# Example run
avg = user_summary(
    title=f"{SURNAME} Academic Report",
    scores=[SEED_DIGIT, 10, ID_SUM % 100],
    ID=STUDENT_ID,
    Surname=SURNAME
)
# %%
# CELL 5 | RETURN MECHANISM
def compute_area(radius):
    return 3.1416 * radius**2

area = compute_area(SEED_DIGIT + 2)
print("Computed Area:", round(area, 2))

# %%
# CELL 6 | SAFE CALCULATOR
def safe_calculator(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        result = "UNDEFINED"
    return result

print("Calculation Result:", safe_calculator(ID_SUM, SEED_DIGIT))

# %%
# CELL 7 | RECURSION 
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of SEED_DIGIT:", factorial(SEED_DIGIT))

# %%
# CELL 8 | STRING RECURSION 
def reverse(text):
    if len(text) < 1:
        return text
    return text[-1] + reverse(text[:-1])

# Example run
print("Reversed SURNAME:", reverse(LAST_NAME.upper()))

# %%
# CELL 9 | DECORATOR 
def logger(func):
    def wrapper(*args, **kwargs):
        print("Executing:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logger
def multiply(x, y):
    return x * y

# Example run
print("Multiplication:", multiply(SEED_DIGIT, NAME_LENGTH))

# %%
# CELL 10 | LAMBDA 
data = list(range(1, SEED_DIGIT + 10))
squared = list(map(lambda x: x**2, data))
print("Original Data:", data)
print("Squared Data:", squared)

# %%
# CELL 11 | GENERATOR
def even_squares(limit):
    """
    Generator function that yields squares of even numbers up to `limit`
    """
    for i in range(1, limit + 1):
        if i % 2 == 0:  # only even numbers
            yield i**2

# Example run
for value in even_squares(NAME_LENGTH + SEED_DIGIT):
    print(value)