def calculate_bmi(weight, height):
    """
    Calculate the BMI (Body Mass Index) based on the given weight (in kg) and height (in meters)
    """
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """
    Classify the BMI into categories (underweight, normal, overweight, obese)
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    
    # Prompt user for weight (in kg)
    while True:
        try:
            weight = float(input("Enter your weight (in kg): "))
            if weight <= 0:
                print("Weight must be a positive number. Try again!")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid weight.")
    
    # Prompt user for height (in meters)
    while True:
        try:
            height = float(input("Enter your height (in meters): "))
            if height <= 0:
                print("Height must be a positive number. Try again!")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid height.")
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Classify BMI
    category = classify_bmi(bmi)
    
    # Display results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {category}")
    
    print("\nPress Enter to exit...")
    input()  # Wait for user to press Enter

if __name__ == "__main__":
    main()