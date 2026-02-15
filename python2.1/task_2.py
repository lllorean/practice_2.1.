with open('resource/students.txt', encoding='utf-8') as f:
    data = [line.strip().split(':') for line in f]

results = []
for name, grades in data:
    avg = sum(map(int, grades.split(','))) / len(grades.split(','))
    if avg > 4.0:
        results.append((name, avg))

with open('resource/result.txt', 'w', encoding='utf-8') as f:
    for name, avg in results:
        f.write(f'{name}:{avg:.2f}\n')

if results:
    best = max(results, key=lambda x: x[1])
    print(f'Лучший студент: {best[0]} со средним баллом {best[1]:.2f}')