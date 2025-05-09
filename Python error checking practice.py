print("Welcome to the Temperature Converter!")
print("This program converts between Celsius and Fahrenheit")

continue_program = "yes"

while continue_program == "yes":
    temperature = int(input("Enter the temperature: "))
    conversion = input("Convert to (C)elsius or (F)ahrenheit?")

    if conversion == "C":
        result = (temperature - 32) *5/9
        original_unit = "Fahrenheit"
        converted_unit = "Celsius"

    elif conversion == "F":
        result = (temperature * 9/5) + 32
        original_unit = "Celsius"
        converted_unit = "Fahrenheit"

    else:
        print("Invalid conversion choice! Please enter C or F.")

    print(result)
