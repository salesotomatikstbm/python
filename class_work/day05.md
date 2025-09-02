---

# **Day - 05 - Class Flow**

---

## **Single-Case Switch Syntax**

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

---

## **3. Example: Day of the Week Message**

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

---

## **4. Example: Check Even or Odd Number**

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

---

## **5. Example: Switch with Strings**

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

---

## **6. Example: Using Switch with Boolean**

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
