import math

def rearrange_digits():
    try:
        # Введення тризначного числа
        num = int(input("Enter a three-digit number: "))
        
        # Перевірка на те, щоб число було тризначним
        if 99 < num < 1000:
            # Закреслюємо першу цифру і приписуємо її справа
            rearranged_num = int(str(num)[1:] + str(num)[0])
            
            # Вивід результату
            print("Original number:", num)
            print("Rearranged number:", rearranged_num)
        else:
            print("Please enter a three-digit number.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

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

def point_inside_rectangle(x, y, x1, y1, x2, y2):
    """
    Check if the point (x, y) lies inside the rectangle
    with top-left corner (x1, y1) and bottom-right corner (x2, y2).
    """
    is_inside = x1 < x < x2 and y1 < y < y2
    return is_inside

def task_boolean_point_inside_rectangle():
    try:
        x = int(input("x = "))
        y = int(input("y = "))
        x1 = int(input("x1 = "))
        y1 = int(input("y1 = "))
        x2 = int(input("x2 = "))
        y2 = int(input("y2 = "))
    except ValueError:
        print("Coordinates must be integers.")
        input("Press enter to exit...")
    else:
        is_point_inside = point_inside_rectangle(x, y, x1, y1, x2, y2)
        print(f"The point ({x}, {y}) is inside the rectangle: {is_point_inside}")