## **Day - 04 - Home Assignment:**

---

### **Project 1: Advanced Student Grade Analyzer 🎓**

---

### **Objective:**

In this project, you’ll calculate the **total marks**, **average**, **percentage**, **highest**, and **lowest** marks for 5 subjects. Then, assign a **grade** based on the percentage using **if-else** conditions.

---

### **What You Need to Do:**

1. **Input Marks for 5 Subjects:**

   * Ask the user to enter the marks for 5 subjects.
     *Example:*

     * `Enter marks for Subject 1: 85`
     * `Enter marks for Subject 2: 78`
     * `...`

   *Hint:* You can store the input in variables like `subject1`, `subject2`, etc.

2. **Calculate the Following:**

   * **Total Marks:**
     Add the marks for all 5 subjects.
     `Total Marks = Subject1 + Subject2 + Subject3 + Subject4 + Subject5`

   * **Average Marks:**
     Divide the total marks by 5 to get the average.
     `Average Marks = Total Marks / 5`

   * **Percentage:**
     Calculate the percentage by dividing the total marks by the maximum possible marks (assuming each subject has a max of 100 marks).
     `Percentage = (Total Marks / 500) * 100`

   * **Highest and Lowest Marks:**
     Find the highest and lowest marks.
     *Hint:* Use Python's `max()` and `min()` functions to calculate the highest and lowest.

3. **Assign a Grade Based on Percentage:**

   * Use **if-else** conditions to assign a grade based on the percentage:

     * If **percentage >= 90**, assign **Grade A+**
     * If **percentage >= 75**, assign **Grade A**
     * If **percentage >= 60**, assign **Grade B**
     * If **percentage >= 50**, assign **Grade C**
     * If **percentage < 50**, assign **Fail**

4. **Show the Results:**

   * Display:

     * Total Marks
     * Average Marks
     * Percentage
     * Grade
     * Highest and Lowest Marks

---

### **Example:**

If the user enters the following marks:

```
Enter marks for Subject 1: 85
Enter marks for Subject 2: 78
Enter marks for Subject 3: 92
Enter marks for Subject 4: 60
Enter marks for Subject 5: 75
```

**Output:**

```
Total Marks: 390
Average Marks: 78
Percentage: 78%
Grade: A
Highest Marks: 92
Lowest Marks: 60
```

---

### **Project 2: Grocery Store Shopping System 🛒**

---

### **Objective:**

In this project, you will create a simple **grocery store shopping system** where the user can add items to their shopping cart, calculate the total cost, and apply discounts if necessary.

---

### **What You Need to Do:**

1. **Set Up Prices for Items:**

   * Start by defining the prices for a few grocery items, such as fruits, vegetables, and snacks.
     *Example:*
   * `apple_price = 30`
   * `banana_price = 20`
   * `carrot_price = 15`

2. **Get the Quantity of Each Item:**

   * Ask the user how many of each item they want to buy.
     *Example:*
   * `How many apples do you want to buy?`
   * `How many bananas do you want to buy?`

   *Hint:* Store the quantities in variables like `apples_quantity`, `bananas_quantity`, etc.

3. **Calculate the Total Cost:**

   * Multiply the price of each item by its quantity and add them together to get the total cost.
     *Example:*
     `total_cost = (apple_price * apples_quantity) + (banana_price * bananas_quantity) + (carrot_price * carrots_quantity)`

4. **Apply Discount:**

   * If the total cost is greater than a certain amount (e.g., 100), apply a discount (e.g., 10%).
   * Use an **if-else** statement to check if the total cost is above 100, and if so, apply a discount.
     *Example:*

     * `if total_cost >= 100:`
     * `    total_cost = total_cost * 0.9`  (This applies a 10% discount)

5. **Show the Final Bill:**

   * Display the total cost before and after the discount (if applicable).
   * Also, show the quantity and cost of each item the user bought.

---

### **Example:**

If the user enters the following quantities:

```
How many apples do you want to buy? 3
How many bananas do you want to buy? 5
How many carrots do you want to buy? 2
```

**Output:**

```
Item Prices:
Apple: 30
Banana: 20
Carrot: 15

Total Cost Before Discount: 140
Discount Applied: 10%
Total Cost After Discount: 126

Thank you for shopping with us!
```

---

### **Simplified Explanation of Key Concepts:**

1. **Input/Output:**

   * Use `input()` to take input from the user.
   * Use `print()` to display results to the user.

2. **Conditions (if-else):**

   * Use **if-else** conditions to check whether a discount should be applied, and also to assign the grade in the student grade analyzer.

3. **Variables and Operators:**

   * Use variables to store data (like item prices, quantities, total cost).
   * Perform basic arithmetic operations like multiplication, addition, and subtraction.

4. **Basic Program Structure:**

   * The program executes based on the user’s choices (adding items, applying discounts), and the final results are displayed.

---

### **Conclusion:**

1. **Project 1 (Student Grade Analyzer)** will help practice using variables, basic arithmetic, and **if-else** conditions to calculate and display student marks and grades.
2. **Project 2 (Grocery Store Shopping System)** will help practice using **if-else** conditions to calculate the total cost of items, apply discounts, and display the final bill.

Both projects use **if-else** conditions and basic input/output operations, focusing on simplifying decision-making logic and calculations.

---

