# **Apple Decision Maker: Using If-Else Statements**

## **1. Basic Apple Checker** 🍎
```python
apple_color = "red"

if apple_color == "red":
    print("This is a red apple! 🍎")
else:
    print("This apple isn't red.")
```

## **2. Price Discount Calculator** 💰
```python
quantity = 6
price_per_kg = 120.5

if quantity > 10:
    discount = 0.20  # 20% discount
elif quantity > 5:
    discount = 0.10  # 10% discount
else:
    discount = 0

total = quantity * price_per_kg * (1 - discount)
print(f"Final price: ₹{total:.2f}")
```

## **3. Health Checker** ❤️
```python
is_healthy = True

if is_healthy:
    print("This apple is good for you! 👍")
else:
    print("Maybe choose a different fruit. 👎")
```

## **4. Apple Type Classifier** 🔍
```python
apple_type = input("What color is the apple? ")

if apple_type.lower() == "red":
    print("Classic red apple")
elif apple_type.lower() == "green":
    print("Tangy green apple") 
elif apple_type.lower() == "yellow":
    print("Sweet golden apple")
else:
    print("Unknown apple variety")
```

## **5. Shopping Decision Maker** 🛒
```python
budget = 200
apple_price = 120.5

if budget >= apple_price:
    print("You can buy this apple! 🛍️")
    change = budget - apple_price
    print(f"You'll get ₹{change:.2f} back")
else:
    print("You need more money to buy this apple. 💸")
    needed = apple_price - budget
    print(f"You need ₹{needed:.2f} more")
```

## **6. Apple Ripeness Checker** 🟢🟡🔴
```python
ripeness = input("Is the apple (g)reen, (y)ellow, or (r)ed? ")

if ripeness.lower() == "g":
    print("Not ripe yet - wait a few days! ⏳")
elif ripeness.lower() == "y":
    print("Almost ripe - eat soon! ⌛") 
elif ripeness.lower() == "r":
    print("Perfectly ripe - enjoy now! 🍽️")
else:
    print("Invalid selection - try again! ❌")
```

## **Key Takeaways:**
✅ Use `if` for the first condition  
✅ Add `elif` for additional conditions  
✅ Finish with `else` for all other cases  
✅ Remember colons `:` and indentation  
✅ Test with different inputs to see all possibilities  

Try modifying these examples with different values to see how the outputs change!