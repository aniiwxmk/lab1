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

# Виклик функції
rearrange_digits()