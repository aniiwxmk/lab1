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

# Викликаємо функцію для тестування
task_boolean_point_inside_rectangle()