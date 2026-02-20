with open('resource/text.txt', 'w', encoding='utf-8') as file:
    file.write("""Группа 651
Это вторая строчка
Что-то сделала вроде
Просто строчка
Последняя срочка""")

print("Файл text.txt успешно создан и заполнен текстом.\n")

try:
    with open('resource/text.txt', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]

    print(f"1. Количество строк в файле: {len(lines)}")

    word_count = sum(len(line.split()) for line in lines)
    print(f"2. Количество слов в файле: {word_count}")

    longest_line = max(lines, key=len)
    print(f'3. Самая длинная строка: "{longest_line}"')

except FileNotFoundError:
    print("Ошибка: Файл text.txt не найден")
except Exception as e:

    print(f"Произошла ошибка: {e}")
