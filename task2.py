import math

def calculate_expression():
    try:
        x = float(input("Enter the value of x: "))
    except ValueError:
        print("Invalid input. x must be a number.")
        input("Press enter to exit...")
    else:
        try:
            # Обчислення математичного виразу
            numerator = math.exp(-x) * math.sin(math.radians(x + 39))**2
            denominator = (abs(1 - math.sqrt(abs(x - 2 * math.sin(x)))))**(1/3)
            second_term = (1/2) * math.tan(x) * math.log(x, 3)
            
            y = numerator / denominator + second_term
        except ValueError:
            print("Invalid input. x must satisfy the expression requirements.")
            input("Press enter to exit...")
        else:
            print("Result (y):", y)

# Виклик функції
calculate_expression()