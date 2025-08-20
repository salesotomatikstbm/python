# **Day - 04 - Class Flow**

## ⚡ On-Spot Advanced Questions 

### **Assignment 01: Fruit Basket Challenge** 🍎🍊

1. Create two variables:

   * `apples = 15`
   * `oranges = 6`

2. Solve the following:

   * Find the **total fruits**.
   * Check if there are **more apples than oranges**.
   * Check if apples are **at least double** the oranges.
   * If the fruits are shared among **4 kids**, how many each gets?
   * Are any fruits left after sharing equally? (use `%`).

**Think About:**

* When fruits are shared, why do we get remainders?
* If the remainder is not 0, what do we do with the leftover fruits?

---

### **Assignment 02: Pocket Money Buyer** 💰

1. Ask the user for two inputs:

   * `pocket_money`
   * `apple_price`

2. Using if-elif-else:

   * Check if the pocket money is **enough to buy at least 1 apple**.
   * Check if the pocket money is **enough to buy 5 apples**.
   * If money is **more than 10 apples worth**, print “Big Spender 🎉”.
   * If not enough even for 1 apple, print “Save more money 🐷💰”.

**Think About:**

* What changes if apple price increases?
* What happens if the child wants mangoes also?

---

## 🚀 Big Project of the Day

# **🍎 Kids Fruit Shop Billing Game** 🛒🎮

A **fun project** where kids can buy apples and bananas with discounts and membership.

```python
# 🍎 Kids Fruit Shop Billing Game

apple_price = 20
banana_price = 10

apples = int(input("How many apples do you want? "))
bananas = int(input("How many bananas do you want? "))
membership = input("Do you have a membership card? (yes/no): ").lower()
money = int(input("Enter your pocket money: "))

# Step 1: Calculate total cost
total_cost = (apple_price * apples) + (banana_price * bananas)

# Step 2: Special discount if buying more fruits
if apples + bananas >= 10:
    total_cost -= total_cost * 0.10   # 10% off

# Step 3: Extra discount for membership
if membership == "yes":
    total_cost -= total_cost * 0.05   # 5% off

print("\n🧾 Final Bill:", total_cost)

# Step 4: Payment check
if money > total_cost:
    print("✅ Purchase successful! Balance left:", money - total_cost)
elif money == total_cost:
    print("✅ Purchase successful! You spent all your money.")
else:
    print("❌ Not enough pocket money. You need:", total_cost - money)
```

---

## 📝 Step-by-Step Thinking

1. Apples = ₹20 each, Bananas = ₹10 each.
2. Ask how many apples & bananas the child wants.
3. Add up cost = apples + bananas.
4. If total fruits ≥ 10 → give **10% discount**.
5. If membership card = yes → extra **5% discount**.
6. Show final bill.
7. Check if pocket money is enough → success/failure.

---
