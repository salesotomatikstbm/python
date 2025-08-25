**Day - 04 - Class Flow** :

## **Question 01: School Supplies Adventure 📚✏️**

### **Objective:**

In this assignment, you will organize your school supplies and practice using basic math in Python.

---

### **Step 1: Organize Your School Supplies**

1. **How many notebooks do you have?**
   *Hint:* Use `input()` to get the number from the user and convert it to an integer using `int()`.

2. **How many pens do you have?**
   *Hint:* Again, use `input()` and convert it to an integer.

---

### **Step 2: Fun with Numbers!**

Let’s do some math with the items you have:

1. **How many total items do you have?**
   *Hint:* Add the number of notebooks and pens together using the `+` operator.

2. **Do you have more notebooks than pens?**
   *Hint:* Use an `if` statement to check if the number of notebooks is greater than the number of pens. Print `"Yes"` or `"No"` based on the comparison.

3. **Are the notebooks more than twice the number of pens?**
   *Hint:* Check if the number of notebooks is greater than two times the number of pens using the condition `notebooks > 2 * pens`.

4. **Sharing Time!**
   If you share all your items with **5 friends**, how many items will each friend get?
   *Hint:* Use integer division (`//`) to divide the total number of items by 5.

5. **Leftovers!**
   After sharing with 5 friends, how many items will be left?
   *Hint:* Use the modulus operator (`%`) to find the remainder when dividing the total items by 5.

---

### **Step 3: Think About This**

1. **Why do we have leftover items after sharing?**
   *Hint:* Think about how division works when it doesn’t divide evenly. The remainder is what’s left over.

2. **What should we do with leftover items?**
   *Hint:* Decide whether to keep them for yourself or share them with others. This can be a fun discussion!

---

## **Question 02: Pocket Money Shopper 💰📓**

### **Objective:**

This time, you’ll use your pocket money to buy school supplies and practice simple money math.

---

### **Step 1: Pocket Money Challenge**

Let’s figure out how much money you have and what things cost.

1. **How much money do you have?**
   *Hint:* Use `input()` to get the total money you have and convert it into an integer.

2. **How much does one notebook cost?**
   *Hint:* Use `input()` to ask for the price of one notebook and convert it to an integer.

3. **How much does one pen cost?**
   *Hint:* Similarly, ask for the price of one pen using `input()` and convert it to an integer.

---

### **Step 2: Time to Go Shopping!**

Let’s see what you can buy with your money.

1. **Can you afford at least 1 notebook?**
   *Hint:* Compare the price of one notebook with the money you have using an `if` statement: `if money >= notebook_price`.

2. **Can you buy 5 notebooks?**
   *Hint:* Multiply the price of 1 notebook by 5. If your money is greater than or equal to that, you can afford 5 notebooks.

3. **Big Spender!**
   If you can buy more than 10 notebooks, you’re a **Big Spender!** 🎉
   *Hint:* Use a simple condition to check: `if money >= 10 * notebook_price`.

4. **Save More Money!**
   If you can’t buy even 1 notebook, don’t worry. Try saving more money!
   *Hint:* Check if the money is less than the price of one notebook and print a message encouraging saving.

---

### **Step 3: Think About This**

1. **What happens if the price goes up?**
   *Hint:* Think about how an increase in price will affect the number of notebooks and pens you can buy. It will decrease the number you can afford.

2. **If you want both notebooks and pens, how will that change your money?**
   *Hint:* First calculate the total cost for both notebooks and pens by adding their prices together, then compare it to your money to see if you can afford both.

---

## **📓 Big School Supplies Game: Buying Notebooks & Pens 🛒✏️**

### **Objective:**

This game allows you to buy notebooks and pens. You get discounts if you’re a member, and discounts for buying multiple items. We’ll use simple **if-else logic** for discounts.

---

### **Python Code Example:**

```python
# 📓 Kids School Shopping Game

# Step 1: Get Prices and Money
notebook_price = int(input("How much is one notebook? "))
pen_price = int(input("How much is one pen? "))
membership = input("Do you have a membership? (yes/no): ").lower()
money = int(input("How much pocket money do you have? "))

# Step 2: Get the Quantity of Items
notebooks = int(input("How many notebooks do you want to buy? "))
pens = int(input("How many pens do you want to buy? "))

# Step 3: Calculate Total Cost
total_cost = (notebook_price * notebooks) + (pen_price * pens)

# Step 4: Apply Discounts
if notebooks + pens >= 10:
    total_cost -= 5  # Discount for 10+ items
if membership == "yes":
    total_cost -= 2  # Discount for membership

# Step 5: Show Final Bill
print("\n🧾 Final Bill:", total_cost)

# Step 6: Can You Pay?
if money > total_cost:
    print("✅ You’ve got enough! Money left:", money - total_cost)
elif money == total_cost:
    print("✅ You’ve spent all your money! Well done!")
else:
    print("❌ Oh no! You need:", total_cost - money)
```

---

### **Full Output Examples**

---

#### **Example 1:**

**Inputs:**

* Price of one notebook: 20
* Price of one pen: 5
* Membership: yes
* Pocket money: 50
* Number of notebooks: 2
* Number of pens: 3

**Output:**

```
How much is one notebook? 20
How much is one pen? 5
Do you have a membership? (yes/no): yes
How much pocket money do you have? 50
How many notebooks do you want to buy? 2
How many pens do you want to buy? 3

🧾 Final Bill: 55
❌ Oh no! You need: 5
```

---

#### **Example 2:**

**Inputs:**

* Price of one notebook: 15
* Price of one pen: 2
* Membership: no
* Pocket money: 30
* Number of notebooks: 5
* Number of pens: 4

**Output:**

```
How much is one notebook? 15
How much is one pen? 2
Do you have a membership? (yes/no): no
How much pocket money do you have? 30
How many notebooks do you want to buy? 5
How many pens do you want to buy? 4

🧾 Final Bill: 83
❌ Oh no! You need: 53
```

---


---

