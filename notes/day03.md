# **Day 03 - Class Script**

## Table of Contents

1. [Warm-up & Recap](#warm-up--recap)
2. [Introducing Operators](#introducing-operators)
3. [Hands-On: Apple Operator Playground](#hands-on-apple-operator-playground)
4. [Decision Making in Python](#decision-making-in-python)
5. [Activity 1: Basic Apple Checker](#activity-1-basic-apple-checker)
6. [Activity 2: Health Checker](#activity-2-health-checker)
7. [Activity 3: Apple Type Classifier](#activity-3-apple-type-classifier)
8. [Activity 4: Shopping Decision Maker](#activity-4-shopping-decision-maker)
9. [Activity 5: Apple Ripeness Checker](#activity-5-apple-ripeness-checker)
10. [Review & Reflection](#review--reflection)
11. [Homework & Practice](#homework--practice)
12. [Next Steps](#next-steps)

---

## Warm-up & Recap

**Highlights**

* Quick recap of variables & formatted printing (from Day 2).
* Ask students: *“What did we learn about fruits and variables last time?”*
* Smoothly transition: *“Today, we will learn how computers compare things and make decisions using operators and if-else.”*

---

## Introducing Operators

**Highlights**

* Explain what operators are (symbols to compare values).
* Focus on: `==`, `!=`, `>`, `<`, `>=`, `<=`.
* Real-world analogy: *“Is the apple red? Is the price higher than my money?”*

---

## Hands-On: Apple Operator Playground

```python
# Equal to (==)
print("Is the apple red?", "red" == "red")   # True

# Not equal (!=)
print("Is the apple not green?", "red" != "green")   # True

# Greater than (>)
print("Is apple price greater than budget?", 60 > 50)   # True

# Less than (<)
print("Is apple price less than budget?", 40 < 50)   # True

# Greater than or equal (>=)
print("Do you have enough money?", 50 >= 50)   # True

# Less than or equal (<=)
print("Is apple weight small?", 150 <= 200)   # True
```

👉 Students should run each line and observe the output (`True` / `False`).

---

## Decision Making in Python

**Highlights**

* Introduce `if`, `elif`, and `else`.
* Explain: *“This is how Python makes choices, just like we do in real life.”*
* Flow: Condition → If True → Action → Else → Another Action.

---

## Activity 1: Basic Apple Checker 🍎

```python
apple_color = "red"

if apple_color == "red":
    print("This is a red apple! 🍎")
else:
    print("This apple isn't red.")
```

* Ask: *“What will happen if I change `apple_color` to green?”*

---

## Activity 2: Health Checker ❤️

```python
is_healthy = True

if is_healthy:
    print("This apple is good for you! 👍")
else:
    print("Maybe choose a different fruit. 👎")
```

👉 Show how boolean (`True` / `False`) controls decisions.

---

## Activity 3: Apple Type Classifier 🔍

```python
apple_type = input("What color is the apple? ").lower()

if apple_type == "red":
    print("Classic red apple")
elif apple_type == "green":
    print("Tangy green apple")
elif apple_type == "yellow":
    print("Sweet golden apple")
else:
    print("Unknown apple variety")
```

👉 Students type color, Python replies with apple type.

---

## Activity 4: Shopping Decision Maker 🛒

```python
budget = int(input("What is your budget? "))
apple_price = int(input("What is the apple price? "))

if budget >= apple_price:
    print("You can buy the apple! 🛍️")
else:
    print("You don’t have enough money. 💸")
```

* Connect to real life: *“If I have ₹50 and the apple costs ₹60, can I buy it?”*

---

## Activity 5: Apple Ripeness Checker 🟢🔴

```python
color = input("Apple color (green / red): ")

if color.lower() == "green":
    print("Not ready yet, wait! ⏳")
elif color.lower() == "red":
    print("Ripe and ready to eat! 🍎")
else:
    print("I don’t know this color. ❓")
```

* Show multiple outcomes with `elif`.

---

## Review & Reflection

**Highlights**

* Ask: *“What did we learn today?”*
* Students should summarize:

  1. Operators (`==`, `!=`, `>`, `<`, `>=`, `<=`).
  2. If-Else statements.
  3. User input with decision making.
* Encourage peer explanation: one student explains, others listen.

---

## Homework & Practice

**Assignments:**

1. Write a program to check if a number is even or odd using `if-else`.
2. Create a fruit shop program:

   * Ask user for budget.
   * Ask fruit price.
   * If enough money → print “You can buy”. Otherwise → print “Not enough money”.
3. Make your own version of *Apple Type Classifier* with at least 3 fruit colors.

---

## Next Steps

**Plan for Next Class (Day 04):**

* Deeper dive into **elif chains** with more conditions.
* Explore **nested if statements** (if inside if).
* More real-world decision-making examples (e.g., grading system, ticket prices).

---
