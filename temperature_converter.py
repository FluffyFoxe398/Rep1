# Конвертер градусов Цельсия в Фаренгейты
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Пример использования
temp_c = float(input("Введите температуру в Цельсиях: "))
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f:.2f}°F")
