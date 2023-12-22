import sys
import math

def rearrange_digits(num):
    try:
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

def calculate_expression(x):
    try:
        # Обчислення математичного виразу
        numerator = math.exp(-x) * math.sin(math.radians(x + 39))**2
        denominator = (abs(1 - math.sqrt(abs(x - 2 * math.sin(x)))))**(1/3)
        second_term = (1/2) * math.tan(x) * math.log(x, 3)

        y = numerator / denominator + second_term
        print("Result (y):", y)
    except ValueError:
        print("Invalid input. x must satisfy the expression requirements.")
        input("Press enter to exit...")

def point_inside_rectangle(x, y, x1, y1, x2, y2):
    """
    Check if the point (x, y) lies inside the rectangle
    with top-left corner (x1, y1) and bottom-right corner (x2, y2).
    """
    is_inside = x1 < x < x2 and y1 < y < y2
    return is_inside

def task_boolean_point_inside_rectangle_main(args):
    x, y, x1, y1, x2, y2 = args
    is_point_inside = point_inside_rectangle(x, y, x1, y1, x2, y2)
    print(f"The point ({x}, {y}) is inside the rectangle: {is_point_inside}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task.py function_name [args]")
    else:
        function_name = sys.argv[1]

        if function_name == "rearrange_digits":
            if len(sys.argv) == 3:
                rearrange_digits(int(sys.argv[2]))
            else:
                print("Usage: python task.py rearrange_digits num")
        elif function_name == "calculate_expression":
            if len(sys.argv) == 3:
                calculate_expression(float(sys.argv[2]))
            else:
                print("Usage: python task.py calculate_expression x")
        elif function_name == "task_boolean_point_inside_rectangle_main":
            if len(sys.argv) == 8:
                args = [int(arg) for arg in sys.argv[2:]]  # Перетворення аргументів з рядків в цілі числа
                task_boolean_point_inside_rectangle_main(args)
            else:
                print("Usage: python task.py task_boolean_point_inside_rectangle_main x y x1 y1 x2 y2")
        else:
            print("Unknown function:", function_name)