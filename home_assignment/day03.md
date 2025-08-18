Here's a structured **if-else homework assignment** following the same style as your previous assignments:

---

# **Homework: Decision-Making with If-Else Statements**  
**Objective:**  
Practice using `if`, `elif`, and `else` to create programs that make decisions based on conditions.  

---

### **Task 1: Fruit Ripeness Checker** 🍏→🍎  
Write a program that checks the ripeness of a fruit based on its color and gives advice.  

#### **Requirements:**  
1. Use `input()` to ask for the fruit's **color** (e.g., "green", "yellow", "red").  
2. Use `if-elif-else` to:  
   - If **green** → "Not ripe yet! Wait a few days."  
   - If **yellow** → "Almost ripe! Eat soon."  
   - If **red** → "Perfectly ripe! Enjoy now."  
   - For any other color → "Unknown ripeness. Be careful!"  

#### **Example Code:**  
```python
color = input("What color is the fruit? ").lower()  

if color == "green":  
    print("Not ripe yet! Wait a few days.")  
elif color == "yellow":  
    print("Almost ripe! Eat soon.")  
elif color == "red":  
    print("Perfectly ripe! Enjoy now.")  
else:  
    print("Unknown ripeness. Be careful!")  
```

#### **Expected Output:**  
```text
What color is the fruit? yellow  
Almost ripe! Eat soon.  
```

---

### **Task 2: Apple Discount Calculator** 🛒💰  
Calculate the final price of apples with discounts based on quantity.  

#### **Requirements:**  
1. Use `input()` to ask for **quantity_kg** (e.g., `3`, `7`, `12`).  
2. Use `if-elif-else` to apply discounts:  
   - **>10kg**: 20% discount  
   - **>5kg**: 10% discount  
   - **≤5kg**: No discount  
3. Print the **final price** (e.g., "Total: ₹96.40").  

#### **Example Code:**  
```python
quantity = int(input("How many kg of apples? "))  
price_per_kg = 120.5  

if quantity > 10:  
    discount = 0.20  
elif quantity > 5:  
    discount = 0.10  
else:  
    discount = 0  

total = quantity * price_per_kg * (1 - discount)  
print(f"Total: ₹{total:.2f}")  
```

#### **Expected Output:**  
```text
How many kg of apples? 7  
Total: ₹759.15  
```

---

### **Task 3: Healthy Fruit Advisor** 🥗  
Advise whether a fruit is healthy based on its sugar content (grams per 100g).  

#### **Requirements:**  
1. Use `input()` to ask for **sugar_per_100g** (e.g., `5`, `15`, `25`).  
2. Use `if-elif-else` to categorize:  
   - **<10g**: "Very healthy! Great choice."  
   - **10-20g**: "Moderate sugar. Enjoy in moderation."  
   - **>20g**: "High sugar! Eat occasionally."  

#### **Example Code:**  
```python
sugar = float(input("Sugar content (g per 100g): "))  

if sugar < 10:  
    print("Very healthy! Great choice.")  
elif 10 <= sugar <= 20:  
    print("Moderate sugar. Enjoy in moderation.")  
else:  
    print("High sugar! Eat occasionally.")  
```

#### **Expected Output:**  
```text
Sugar content (g per 100g): 12  
Moderate sugar. Enjoy in moderation.  
```

---

### **Bonus Challenge: Fruit Mystery Game** 🎲  
Create a guessing game where the user tries to guess a secret fruit (e.g., "apple").  

#### **Requirements:**  
1. Set a `secret_fruit = "apple"`.  
2. Use `input()` to ask for guesses.  
3. Use `if-else` to respond:  
   - If correct → "You win! 🎉"  
   - If wrong → "Try again! Hint: It's red."  

#### **Example Code:**  
```python
secret_fruit = "apple"  
guess = input("Guess the fruit: ").lower()  

if guess == secret_fruit:  
    print("You win! 🎉")  
else:  
    print("Try again! Hint: It's red.")  
```

---

### **Submission Guidelines:**  
1. Save your code as `fruit_decisions.py`.  
2. Test all scenarios (e.g., try different colors/quantities).  
3. **Stretch Goal**: Add more conditions (e.g., check if the fruit is organic).  

**Tip:** Use comments (`#`) to explain your logic!  

--- 

This follows the same **interactive, variable-driven** style as your previous assignments while focusing on **conditional logic**. Let me know if you'd like any modifications!