# weather conditions and corresponding advice
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()
if weather == "sunny":
    print("Wear a T-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget to take an umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm jacket and a scarf.")
else: 
    print("Sorry, I don't have recommendations for that weather condition.")