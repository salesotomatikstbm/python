weather = input("Enter weather (sunny, rainy, cloudy, snowy): ").lower()

match weather:
    case "sunny":
        print("Wear sunglasses")
    case "rainy":
        print("Take an umbrella")
    case "cloudy":
        print("It might rain later")
    case "snowy":
        print("Wear warm clothes")
    case _:
        print("Unknown weather condition")
