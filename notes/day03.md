# **Control Statements in Python: Making Decisions with Code!**  

## **What Are Control Statements?**  
Control statements help computers make **decisions** based on conditions. Just like in real life:  

- **If** it's raining, **then** take an umbrella. ☔  
- **Else**, enjoy the sunshine! ☀️  

In Python, we use **`if`**, **`else`**, and **`elif`** (short for "else if") to make these decisions.  

---

## **Example: The Ice Cream Decision 🍦**  
Let’s write a simple program that decides whether you can eat ice cream based on your homework status.  

### **Code Example:**  
```python
homework_done = True  # Change to False and see what happens!

if homework_done:  
    print("🎉 Yay! You can have ice cream! 🍦")  
else:  
    print("😢 Finish your homework first! 📚")  
```

### **How It Works:**  
1. The computer checks **`if homework_done is True`**.  
2. If **YES**, it prints the happy message.  
3. If **NO**, it prints the sad message.  

---

## **Another Example: The Pet Checker 🐶🐱**  
What if we have more options? Let’s use **`elif`**!  

### **Code Example:**  
```python
pet = "dog"  # Try changing to "cat", "fish", or "dragon"!

if pet == "dog":  
    print("🐶 Woof! You have a dog!")  
elif pet == "cat":  
    print("🐱 Meow! You have a cat!")  
elif pet == "fish":  
    print("🐟 Blub blub! You have a fish!")  
else:  
    print("🤖 Hmm, I don’t know that pet!")  
```

### **How It Works:**  
1. The computer checks **each condition in order**.  
2. If one is **True**, it runs that block and **skips the rest**.  
3. If **none match**, it runs the **`else`** block.  

---

## **Key Takeaways:**  
✅ **`if`** → Checks a condition (must be **True** to run).  
✅ **`elif`** → Adds more conditions (like "else if").  
✅ **`else`** → Runs if **no other condition is True**.  

🔹 **Try It Yourself!** Change the values and see what happens!  

---

## **Homework Challenge 🏆**  
Write a program that:  
1. Asks the user for their **age** (`input()`).  
2. If age is **less than 13**, print: "You're a kid! 🧒"  
3. If age is **13-19**, print: "You're a teenager! 🎸"  
4. Otherwise, print: "You're an adult! 👔"  

**Example Answer:**  
```python
age = int(input("How old are you? "))  

if age < 13:  
    print("You're a kid! 🧒")  
elif age <= 19:  
    print("You're a teenager! 🎸")  
else:  
    print("You're an adult! 👔")  
```

---

### **Next Class:**  
We’ll learn about **loops** (`while` and `for`) to repeat actions! 🔄  

🚀 **Remember:** Coding is like giving instructions to a robot—be clear and have fun!