import math
import copy

# --- КОНСТАНТИ ---
M = 13
A = (5**0.5 - 1) / 2 # ~0.6180339887 для методу множення

WORDS_UA = ["СКІЛЬКИ", "ВОВКА", "НЕ", "ГОДУЙ", "А", "ВІН", "УСЕ", "В", "ЛІС", "ДИВИТЬСЯ"]
LETTER_POSITIONS_UA = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8, 'Ж': 9, 'З': 10,
    'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19,
    'П': 20, 'Р': 21, 'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28,
    'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}

# --- ДОПОМІЖНА ФУНКЦІЯ: Обчислення K (суми позицій) ---
def calculate_k(key: str) -> int:
    """Обчислює числовий ключ K як суму позицій букв."""
    k = 0
    for char in key.upper():
        k += LETTER_POSITIONS_UA.get(char, 0)
    return k

# --- ХЕШ-ФУНКЦІЇ З ОСНОВНИМ ЗОНДУВАННЯМ ---
# Примітка: 'i' тут є індексом спроби зондування (0, 1, 2, ...)

def hash_division_probe(k: int, i: int) -> int:
    """Функція хешування методом ділення з лінійним зондуванням: h(K, i) = (K mod M + i) mod M"""
    return (k % M + i) % M

def hash_multiplication_probe(k: int, i: int) -> int:
    """Функція хешування методом множення з лінійним зондуванням: h(k, i) = (floor(M * (k*A mod 1)) + i) mod M"""
    h0 = int(M * ((k * A) % 1))
    return (h0 + i) % M

# --- АЛГОРИТМ ПОБУДОВИ ТАБЛИЦІ ---

# Перейменовуємо функцію та оновлюємо коментар
def build_open_hash_table(words: list, m: int, probe_func) -> (list, list):
    """
    Будує хеш-таблицю з відкритим адресуванням (лінійне зондування).
    Повертає таблицю та список довжин зондування.
    """
    hash_table = [None] * m
    probe_lengths = []

    for word in words:
        k = calculate_k(word)
        i = 0 # Лічильник спроб зондування

        # Лінійне зондування: шукаємо наступну вільну комірку
        while i < m:
            address = probe_func(k, i)

            # Якщо знайшли вільну комірку або зустріли той самий елемент (для пошуку)
            # При вставці ми завжди шукаємо None
            if hash_table[address] is None:
                hash_table[address] = word
                probe_lengths.append((word, i + 1)) # i+1 - довжина зондування (кількість спроб)
                break # Елемент вставлено, переходимо до наступного слова
            # Якщо комірка зайнята, але це не наш елемент, продовжуємо зондування
            elif hash_table[address] == word: # Це для уникнення дублікатів, якщо це дозволено
                 probe_lengths.append((word, i + 1)) # Все одно враховуємо спробу
                 break
            
            i += 1 # Збільшуємо лічильник спроб для зондування
        else:
            # Цей блок виконується, якщо цикл 'while' завершився без 'break'
            print(f"Помилка: Таблиця переповнена, не вдалося вставити '{word}'")
            # Якщо таблиця переповнена, можливо, варто повернути поточну таблицю і probe_lengths
            # або викликати виняток
            return hash_table, probe_lengths # Повертаємо те, що встигли вставити

    return hash_table, probe_lengths

# Перейменовуємо функцію та оновлюємо коментар
def display_open_hash_table(table: list, title: str):
    """Виводить хеш-таблицю з відкритим адресуванням у зручному форматі."""
    print(f"\n--- {title} (Таблиця M={M}) ---")

    # Заголовки індексів
    print("Індекс:", end=" ")
    for i in range(len(table)):
        print(f"{i:02d}", end=" ")
    print()

    # Вміст комірок
    print("Вміст:", end=" ")
    for item in table:
        print(f"{item[:2] if item else '--'}", end=" ") # Відображаємо лише перші 2 символи або '--' для None
    print("\n")


# --- ВИКОНАННЯ ---

print("АЛГОРИТМ ХЕШУВАННЯ З ВІДКРИТИМ АДРЕСУВАННЯМ")

# 1. Метод Ділення
# Оновлюємо назву функції
hash_table_div, lengths_div = build_open_hash_table(WORDS_UA, M, hash_division_probe)
# Оновлюємо назву функції та заголовок
display_open_hash_table(hash_table_div, "Результат Хеш-таблиці з Відкритим Адресуванням (Ділення)")

# 2. Метод Множення
# Оновлюємо назву функції
hash_table_mult, lengths_mult = build_open_hash_table(WORDS_UA, M, hash_multiplication_probe)
# Оновлюємо назву функції та заголовок
display_open_hash_table(hash_table_mult, "Результат Хеш-таблиці з Відкритим Адресуванням (Множення)")

# Аналіз довжин зондування
print("\n--- Аналіз Довжин Зондування (Кількість кроків для вставки) ---")
print("Метод Ділення:")
for word, length in lengths_div:
    print(f" {word}: {length} кроків")

print("\nМетод Множення:")
for word, length in lengths_mult:
    print(f" {word}: {length} кроків")
