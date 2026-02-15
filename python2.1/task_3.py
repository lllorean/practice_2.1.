import csv
import os

CSV_FILE = "resource/products.csv"

if not os.path.exists(CSV_FILE):
    print(f"Создаю файл {CSV_FILE} с тестовыми данными...")
    with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Название", "Цена", "Количество"])
        writer.writerow(["Яблоки", 100, 50])
        writer.writerow(["Бананы", 80, 30])
        writer.writerow(["Молоко", 120, 20])
        writer.writerow(["Хлеб", 40, 100])
    print("Файл создан.")

print("Система учета товаров ")

while True:
    print("\nМеню:")
    print("1. Показать все товары")
    print("2. Добавить новый товар")
    print("3. Поиск товара по названию")
    print("4. Расчет общей стоимости всех товаров")
    print("5. Выход и сохранение")

    choice = input("Выберите действие (1-5): ")

    if choice == "1":
        print("\nСписок товаров:")
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    print(f"{row[0]:<15} {row[1]:<10} {row[2]}")
                else:
                    print(f"{row[0]:<15} {row[1]:<10} {row[2]}")

    elif choice == "2":
        print("\nДобавление нового товара:")
        name = input("Название товара: ")
        price = int(input("Цена: "))
        quantity = int(input("Количество: "))

        with open(CSV_FILE, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, price, quantity])

        print(f"Товар '{name}' добавлен.")

    elif choice == "3":
        search_name = input("\nВведите название товара для поиска: ").lower()
        found = False

        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                if row[0].lower() == search_name:
                    print(f"\nНайден товар:")
                    print(f"Название: {row[0]}")
                    print(f"Цена: {row[1]} руб.")
                    print(f"Количество: {row[2]} шт.")
                    found = True
                    break

        if not found:
            print(f"Товар '{search_name}' не найден.")

    elif choice == "4":
        total_value = 0
        total_quantity = 0

        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                if len(row) >= 3:
                    price = int(row[1])
                    quantity = int(row[2])
                    total_value += price * quantity
                    total_quantity += quantity

        print(f"\nОбщая стоимость всех товаров: {total_value} руб.")
        print(f"Общее количество товаров: {total_quantity} шт.")

    elif choice == "5":
        print("\nДанные сохранены в файле products.csv")
        print("Выход из программы.")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")