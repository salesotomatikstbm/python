# Python Homework

This week’s assignment: practice Python to improve your typing and coding skills. Use VS Code and create the files below. Run each program and check the output.

## Program 1: Variables (Save as `story.py`)
Create the storyline to explain the variables (like you did in class for the self-introduction)

```markdown
# Python Variables: The Naming Game 🏷️

## Program 2: Naming Variables (Save as `variables1.py`)
```python
# 🟢 GOOD Variables (They follow rules!)
student_name = "Ramesh"    # Like a proper nametag
school = "ABC School"      # Simple and clear
math_score = 95           # Says what it stores
MAX_MARKS = 100           # Constants are SHOUTY (uppercase)

# 🔴 BAD Variables (They break rules!)
2nd_name = "Kumar"        # ❌ Numbers can't start names
school name = "ABC"       # ❌ Spaces make Python confused
$address = "Madambakkam"  # ❌ Symbols aren't allowed
for = "loop word"         # ❌ "for" is a Python keyword

print("Good variables work perfectly:")
print(f"Student: {student_name}")
print(f"Score: {math_score}/{MAX_MARKS}")

# The bad variables will CRASH your program!
# Try uncommenting them one by one to see errors
```

**💡 Try It!**  
1. Run the program - only good variables work  
2. Uncomment each bad variable and see different error messages  
3. Write 2 more GOOD and 2 more BAD variables yourself  

---

## Program 3: Assignment Rules (Save as `variables2.py`)
```python
# 🟢 GOOD Assignments
name = "Ramesh"     # Text in "quotes" 
age = 12            # Whole number
height = 4.11       # Decimal number
has_dog = True      # Yes/No value

# 🔴 BAD Assignments
name = Ramesh       # ❌ Missing quotes = ERROR
age = twelve        # ❌ Words aren't numbers
height = 4 feet 11  # ❌ Units confuse Python
has_dog = "True"    # 🤔 Works but WRONG (now text)

print("Let's check types:")
print(f"name is {type(name)}")
print(f"age is {type(age)}")
print(f"height is {type(height)}")
print(f"has_dog is {type(has_dog)}")
```

**💡 Experiment Time**  
1. Fix the bad assignments one by one  
2. Change values and predict the type before running  
3. Make a variable called `my_pet` with correct assignment  

---

## Program 4: Using Variables (Save as `variables3.py`)
```python
# 🟢 GOOD Usage
first_name = "Ramesh"
last_name = "Kumar"
full_name = first_name + " " + last_name  # Text joining
age = 12
next_age = age + 1                       # Math works!

# 🔴 BAD Usage
print(First_Name)     # ❌ Capital F? Python is case-sensitive!
full name = full_name # ❌ Space in variable name = CRASH
age = "12"            # 🤔 Now text not number...
total = age + 5       # ❌ Can't add text + number!

print("About Me:")
print(f"Name: {full_name}")
print(f"Next age: {next_age}")
```

