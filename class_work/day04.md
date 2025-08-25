
## ⚡ ** Python Day 04: Class Flow** 🎒📚

### **Assignment 01: School Supplies Adventure** 📚✏️

1. **Let’s organize your school supplies!**

   * **How many notebooks do you have?** (Enter a number)
   * **How many pens do you have?** (Enter a number)

2. **Now, let’s have some fun with numbers:**

   * **How many items** do you have in total? (Add up your notebooks and pens)
   * **Do you have more notebooks than pens**? (Let’s see!)
   * **Are the notebooks more than twice** the number of pens? (Let’s check!)
   * **Sharing Time!** If we share all the items with **5 friends**, how many items will each friend get?
   * **Leftover Time:** After sharing with 5 friends, how many items will be left?

3. **Things to Think About:**

   * Why do we have leftover items after sharing?
   * What should we do with the leftover items? Should we keep them or give them to others?

---

### **Assignment 02: Pocket Money Shopper** 💰📓

1. **Let’s pretend you have some pocket money!**

   * **How much money do you have?**
   * **How much does one notebook cost?**
   * **How much does one pen cost?**

2. **Time to go shopping for school supplies:**

   * **Can you afford at least 1 notebook** with your pocket money?
   * **Can you buy 5 notebooks** with your money?
   * **If you can buy more than 10 notebooks**, you’re a **Big Spender! 🎉**
   * **If you can’t even buy 1 notebook**, I’ll say: **“Save more money 🐷💰”** – but don’t worry, we’ll help you save!

3. **Things to Think About:**

   * What happens if the price of **notebooks** or **pens** goes up?
   * If you want to buy both **notebooks and pens**, how will that change your pocket money?

---

### **📓 Big School Supplies Game: Buying Notebooks & Pens** 🛒✏️

**Let’s create a fun school shopping game!** Let’s create a fun school shopping game! You can buy notebooks and pens, and if you're a member, you can even get discounts! This time, we will use if-else logic for the discounts instead of flat reductions.

```python
# 📓 Kids School Shopping Game

# Step 1: Get prices and user information
notebook_price = int(input("How much is one notebook? "))
pen_price = int(input("How much is one pen? "))
membership = input("Do you have a membership card? (yes/no): ").lower()
money = int(input("How much pocket money do you have? "))

# Step 2: Get the quantity of items
notebooks = int(input("How many notebooks do you want to buy? "))
pens = int(input("How many pens do you want to buy? "))

# Step 3: Calculate total cost before discounts
total_cost = (notebook_price * notebooks) + (pen_price * pens)

# Step 4: Apply discount logic
if notebooks + pens >= 10:
    print("🎉 You get a 10% discount for buying 10 or more items!")
    total_cost = total_cost - (total_cost * 0.10)  # 10% off
else:
    print("No discount for buying less than 10 items.")

if membership == "yes":
    print("🎉 You get a 5% discount for being a member!")
    total_cost = total_cost - (total_cost * 0.05)  # 5% off
else:
    print("No membership discount.")

# Step 5: Display Final Bill
print("\n🧾 Final Bill:", total_cost)

# Step 6: Payment Check
if money > total_cost:
    print("✅ You’ve got enough! You still have money left:", money - total_cost)
elif money == total_cost:
    print("✅ You’ve spent all your money! Good job!")
else:
    print("❌ Oh no! You don’t have enough. You need:", total_cost - money)

```

---

### **Step-by-Step Fun Learning for the Big Project:**

1. **Price Inputs:** How much do notebooks and pens cost? You’ll tell me!
2. **Items to Buy:** How many notebooks and pens do you want to buy? (Let me know!)
3. **Cost Calculation:** We’ll figure out how much everything will cost.
4. **Discounts!**

   * If you buy **10 or more items** (notebooks + pens), you get a **10% discount!**
   * If you have a **membership**, you get an **extra 5% off!** 🎉
5. **Final Bill:** After the discounts, we’ll see the final bill.
6. **Payment Check:** Do you have enough pocket money? We’ll see if you have money left or if you need more.
7. **Leftovers:** After sharing with 5 friends, we check how many **leftover items** you have.

---

### **Extra Fun Challenges for You!**

* Add more **cool discounts** if you buy different combinations of notebooks and pens.
* Add other **school supplies** like **erasers** or **pencils**, each with different prices.
* Make up **new membership levels** with even bigger discounts.
* Think about **special school sales** like **back-to-school discounts**.

---

This version now avoids using the `%` operator and uses a simple calculation for leftover items after sharing. The concept is still fun and easy to follow. Let me know if you'd like any other changes!
