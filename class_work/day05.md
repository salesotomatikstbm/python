# **Day - 05 - Class Flow **
---

Certainly! Here's the shortened comparison table between **if-else** and **switch-case**:

| **Aspect**      | **if-else**              | **switch-case**             |
| --------------- | ------------------------ | --------------------------- |
| **Expression**  | Evaluated per condition  | Evaluated once              |
| **Conditions**  | Multiple `if` statements | Grouped in cases            |
| **Default**     | Requires `else`          | `default` is optional       |
| **Code Blocks** | Separate for each `if`   | Case blocks without `break` |
| **Performance** | Slower for many checks   | More efficient              |

This simplified table highlights the key differences between **if-else** and **switch-case** in Go.


### **Explanation of `package main` and `import "fmt"`:**

* **`package main`**: In Go, every program must declare a **package**. The `main` package is special because it defines an executable program. A program in Go must have a `main` function, and it must reside inside the `main` package to be executed. Essentially, the `main` package is where the entry point of the program resides.

* **`import "fmt"`**: The `fmt` package is a standard Go library used for formatted I/O operations, such as printing to the console or reading input. `fmt.Println()` is commonly used to print output to the screen. Without importing `fmt`, you wouldn't be able to use its functions, such as `fmt.Println()`.

---

# **The Switch Statement in Go**

## **Single-Case Switch Syntax**

The `switch` statement in Go helps to select one of many code blocks to execute based on a given expression. It's an efficient way to handle multiple conditions without using numerous `if-else` statements. Here's the syntax for a single-case switch:

```go
switch expression {
case x:
    // code block
case y:
    // code block
case z:
    // code block
default:
    // code block
}
```

### **How It Works:**

1. **Expression Evaluation**: The expression after the `switch` keyword is evaluated.
2. **Case Matching**: The value of the switch expression is compared with each case.
3. **Execution**: If a case matches, the corresponding code block runs. If no case matches, the `default` block (if present) will execute.
4. **No Need for `break`**: In Go, each `case` automatically ends the switch when matched. You don't need to use a `break` statement like in other languages such as C or Java.

---

## **1. Example: Month Name from Month Number**

This example uses a switch statement to print the name of the month based on its number (1-12).

```go
package main
import "fmt"

func main() {
    month := 8

    switch month {
    case 1:
        fmt.Println("January")
    case 2:
        fmt.Println("February")
    case 3:
        fmt.Println("March")
    case 4:
        fmt.Println("April")
    case 5:
        fmt.Println("May")
    case 6:
        fmt.Println("June")
    case 7:
        fmt.Println("July")
    case 8:
        fmt.Println("August")
    case 9:
        fmt.Println("September")
    case 10:
        fmt.Println("October")
    case 11:
        fmt.Println("November")
    case 12:
        fmt.Println("December")
    default:
        fmt.Println("Invalid month number")
    }
}
```

**Output:**

```
August
```

---

## **2. Example: Grading System**

This example checks the score and assigns a grade based on the score using the switch-case logic.

```go
package main
import "fmt"

func main() {
    score := 85

    switch {
    case score >= 90:
        fmt.Println("Grade: A")
    case score >= 80:
        fmt.Println("Grade: B")
    case score >= 70:
        fmt.Println("Grade: C")
    case score >= 60:
        fmt.Println("Grade: D")
    default:
        fmt.Println("Grade: F")
    }
}
```

**Output:**

```
Grade: B
```

### **Explanation**:

* The expression is left empty, and we simply evaluate the conditions inside the `case` blocks. This allows us to group conditions and handle ranges, such as checking if the score is greater than or equal to certain thresholds.

---

## **3. Example: Day of the Week Message**

This example uses a switch to print a specific message depending on the day of the week.

```go
package main
import "fmt"

func main() {
    day := "Wednesday"

    switch day {
    case "Monday":
        fmt.Println("Start of the work week!")
    case "Wednesday":
        fmt.Println("Mid-week! Keep going!")
    case "Friday":
        fmt.Println("Almost the weekend!")
    case "Saturday", "Sunday":
        fmt.Println("Weekend! Time to relax!")
    default:
        fmt.Println("Keep working hard!")
    }
}
```

**Output:**

```
Mid-week! Keep going!
```

### **Explanation**:

* The switch checks the `day` variable, and when it matches `"Wednesday"`, the corresponding message is printed.
* The switch also includes multiple cases for `Saturday` and `Sunday` using a comma, which works like a logical OR.

---

## **4. Example: Check Even or Odd Number**

This example uses a switch statement to determine if a number is even or odd.

```go
package main
import "fmt"

func main() {
    number := 42

    switch {
    case number%2 == 0:
        fmt.Println("The number is even.")
    case number%2 != 0:
        fmt.Println("The number is odd.")
    }
}
```

**Output:**

```
The number is even.
```

### **Explanation**:

* The expression in the `switch` is empty, and the `case` checks if the number is divisible by 2 (i.e., even or odd).
* This structure is often used when you want to evaluate conditions directly inside the `case` statements.

---

## **5. Example: Switch with Strings**

This example demonstrates how to use strings with a switch-case statement to perform different actions based on a user's input.

```go
package main
import "fmt"

func main() {
    choice := "coffee"

    switch choice {
    case "coffee":
        fmt.Println("Preparing your coffee...")
    case "tea":
        fmt.Println("Preparing your tea...")
    case "juice":
        fmt.Println("Preparing your juice...")
    default:
        fmt.Println("Invalid choice! Please select a valid drink.")
    }
}
```

**Output:**

```
Preparing your coffee...
```

### **Explanation**:

* Here, the `switch` is used to choose between different types of drinks based on the string `choice`.
* If the user enters a drink that's not listed, the `default` case will be triggered.

---

## **6. Example: Using Switch with Boolean**

Here’s an example where we use a switch to handle a boolean value and perform different actions.

```go
package main
import "fmt"

func main() {
    isRaining := true

    switch isRaining {
    case true:
        fmt.Println("Don't forget your umbrella!")
    case false:
        fmt.Println("Enjoy the sunshine!")
    }
}
```

**Output:**

```
Don't forget your umbrella!
```

---
