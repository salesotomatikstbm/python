# Python Homework 

Learn Python variables through clear "Do's and Don'ts" examples. Create each program file and observe how proper variable usage affects your code.

---
## Program 1: 
Create the storyline to explain the variables (like you did in class for the self-introduction)




## Program 2: Naming Variables Correctly
Create `variables1.py` with:

```python
# DO's - Proper variable naming
student_name = "Ramesh"    # Descriptive, lowercase with underscore
school = "ABC School"      # Simple and clear
math_score = 95           # Relates to what it stores
MAX_MARKS = 100           # Constants in uppercase

# DON'Ts - Problematic naming
2nd_name = "Kumar"        # Error: Starts with number
school name = "ABC"       # Error: Contains space
$address = "Madambakkam"  # Error: Special character
for = "loop word"         # Error: Python keyword

print("Good variables work:")
print(student_name)
print(math_score)

# The bad variables will cause errors before reaching these lines

Learning Point:
✓ Use lowercase_with_underscores
✓ Start with letters
✓ Be descriptive
✗ No spaces/special chars
✗ Don't use Python keywords





## Program 3: Variable Assignment Rules
Create variables2.py with:

# DO's - Proper assignment
name = "Ramesh"           # String
age = 12                  # Integer
height = 4.11            # Float
has_dog = True           # Boolean

# DON'Ts - Problematic assignment
name = Ramesh            # Error: Missing quotes for string
age = twelve             # Error: Word instead of number
height = 4 feet 11       # Error: Mixed units in number
has_dog = "True"         # Legal but misleading (now a string)

print("Proper assignments work:")
print(f"{name} is {age} years old")

# The bad assignments will fail before these lines

Learning Point:
✓ Strings need quotes
✓ Numbers without units
✓ Booleans are True/False (no quotes)
✗ Don't mix types accidentally





## Program 4: Variable Usage Examples
Create variables3.py with:

# DO's - Good practices
first_name = "Ramesh"
last_name = "Kumar"
full_name = first_name + " " + last_name  # Combining variables
age = 12
next_age = age + 1                        # Math operations

# DON'Ts - Common mistakes
print(First_Name)        # Error: Case-sensitive (not first_name)
full name = full_name    # Error: Space in variable name
age = "12"               # Legal but...
total = age + 5          # Error: Can't add string + number

print("Good usage results:")
print(f"Hello {full_name}")
print(f"Next year you'll be {next_age}")

# The mistakes will prevent these from running

Learning Point:
✓ Remember case sensitivity
✓ No spaces in names
✓ Watch your types (str vs int)
✗ Don't reuse names carelessly


## If you need help
Post in the group with any of these problems:
- VS Code not opening  
- Can't create a file  
- My file is not running

Good luck and have fun coding!
