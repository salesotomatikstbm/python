---

# **Day - 05 - Class Flow**

---

## **1. Example: Month Name from Month Number**

```go
package main

func main() {
    month := 8

    switch month {
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    default:
        print("Invalid month number")
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

func main() {
    score := 85

    switch {
    case score >= 90:
        print("Grade: A")
    case score >= 80:
        print("Grade: B")
    case score >= 70:
        print("Grade: C")
    case score >= 60:
        print("Grade: D")
    default:
        print("Grade: F")
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

func main() {
    day := "Wednesday"

    switch day {
    case "Monday":
        print("Start of the work week!")
    case "Wednesday":
        print("Mid-week! Keep going!")
    case "Friday":
        print("Almost the weekend!")
    case "Saturday", "Sunday":
        print("Weekend! Time to relax!")
    default:
        print("Keep working hard!")
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

func main() {
    number := 42

    switch {
    case number%2 == 0:
        print("The number is even.")
    case number%2 != 0:
        print("The number is odd.")
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

func main() {
    choice := "coffee"

    switch choice {
    case "coffee":
        print("Preparing your coffee...")
    case "tea":
        print("Preparing your tea...")
    case "juice":
        print("Preparing your juice...")
    default:
        print("Invalid choice! Please select a valid drink.")
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

func main() {
    isRaining := true

    switch isRaining {
    case true:
        print("Don't forget your umbrella!")
    case false:
        print("Enjoy the sunshine!")
    }
}
```

**Output:**

```
Don't forget your umbrella!
```

---
