import datetime
import os

LOG_FILE = "resource/calculator.log"

if os.path.exists(LOG_FILE):
    print("Последние 5 операций")
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            last_lines = lines[-5:] if len(lines) >= 5 else lines
            for line in last_lines:
                print(line.strip())
    except:
        print("Не удалось прочитать файл лога")
else:
    print("Файл лога не существует. Будет создан при первой операции.")

print("\nКалькулятор")

while True:
    print("\nМеню:")
    print("1. Выполнить вычисление")
    print("2. Показать последние операции")
    print("3. Очистить файл лога")
    print("4. Выход")

    choice = input("Выберите действие (1-4): ")

    if choice == "1":
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            operation = input("Введите операцию (+, -, *, /): ")

            result = None
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = num1 / num2
            else:
                print("Ошибка: неверная операция!")
                continue

            print(f"Результат: {num1} {operation} {num2} = {result}")

            timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            log_entry = f"{timestamp} {num1} {operation} {num2} = {result}\n"

            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(log_entry)

            print("Операция записана в лог.")

        except ValueError:
            print("Ошибка: введите числа корректно!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    elif choice == "2":
        if os.path.exists(LOG_FILE):
            try:
                with open(LOG_FILE, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                if not lines:
                    print("Файл лога пуст.")
                else:
                    print(f"\nВсего операций в логе: {len(lines)}")
                    print("Сколько последних операций показать?")
                    try:
                        n = int(input("Введите число (по умолчанию 5): ") or "5")
                        if n <= 0:
                            n = 5
                    except:
                        n = 5

                    last_lines = lines[-n:] if len(lines) >= n else lines
                    print(f"\nПоследние {len(last_lines)} операций:")
                    for line in last_lines:
                        print(line.strip())
            except:
                print("Не удалось прочитать файл лога.")
        else:
            print("Файл лога не существует.")

    elif choice == "3":
        if os.path.exists(LOG_FILE):
            confirm = input("Вы уверены, что хотите очистить файл лога? (да/нет): ").lower()
            if confirm == "да":
                with open(LOG_FILE, "w", encoding="utf-8") as f:
                    f.write("")
                print("Файл лога очищен.")
            else:
                print("Очистка отменена.")
        else:
            print("Файл лога не существует.")

    elif choice == "4":
        print("Выход из программы.")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")