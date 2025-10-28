# --- КОНСТАНТИ ---
M = 13
A = (5**0.5 - 1) / 2 # ~0.6180339887 для методу множення

WORDS_UA = ["СКІЛЬКИ", "ВОВКА", "НЕ", "ГОДУЙ", "А", "ВІН", "УСЕ", "В", "ЛІС", "ДИВИТЬСЯ"]

LETTER_POSITIONS_UA = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8, 'Ж': 9, 'З': 10, 'И': 11, 'І': 12, 'Ї': 13, 'Й': 14,
    'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19, 'П': 20, 'Р': 21, 'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27,
    'Ч': 28, 'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}

# --- ДОПОМІЖНА ФУНКЦІЯ: Обчислення K (суми позицій) ---
def calculate_k(key: str) -> int:
    """Обчислює числовий ключ K як суму позицій букв."""
    k = 0
    for char in key.upper():
        k += LETTER_POSITIONS_UA.get(char, 0)
    return k

# --- ХЕШ-ФУНКЦІЇ З ОСНОВНИМ ЗОНДУВАННЯМ ---

def hash_division_probe(k: int, i: int) -> int:
    """h(K) = (K mod M + i) mod M"""
    return (k % M + i) % M

def hash_multiplication_probe(k: int, i: int) -> int:
    """h(k) = (floor(M * (k*A mod 1)) + i) mod M"""
    h0 = int(M * ((k * A) % 1))
    return (h0 + i) % M

# --- АЛГОРИТМ ПОБУДОВИ ТАБЛИЦІ ---

def build_closed_hash_table(words: list, m: int, probe_func) -> (list, list):
    """
    Будує закриту хеш-таблицю (відкрита адресація) з лінійним зондуванням.
    Повертає таблицю та список довжин зондування.
    """
    hash_table = [None] * m
    probe_lengths = []
    
    for word in words:
        k = calculate_k(word)
        i = 0
        
        # Лінійне зондування: шукаємо наступну вільну комірку
        while i < m:
            address = probe_func(k, i)
            
            if hash_table[address] is None:
                hash_table[address] = word
                probe_lengths.append((word, i + 1)) # i+1 - довжина зондування
                break
            
            i += 1
        else:
            print(f"Помилка: Таблиця переповнена, не вдалося вставити {word}")

    return hash_table, probe_lengths

def display_closed_hash_table(table: list, title: str):
    """Виводить хеш-таблицю у зручному форматі."""
    print(f"\n--- {title} (Таблиця M={M}) ---")
    
    # Заголовки індексів
    print("Індекс:", end=" ")
    for i in range(len(table)):
        print(f"{i:02d}", end=" ")
    print()
    
    # Вміст комірок
    print("Вміст:", end="  ")
    for item in table:
        print(f"{item[:2] if item else '--'}", end=" ") # Відображаємо лише перші 2 символи
    print("\n")


# --- ВИКОНАННЯ ---

# 1. Метод Ділення
hash_table_div, lengths_div = build_closed_hash_table(WORDS_UA, M, hash_division_probe)
display_closed_hash_table(hash_table_div, "Результат Закритої Хеш-таблиці (Ділення)")

# 2. Метод Множення
hash_table_mult, lengths_mult = build_closed_hash_table(WORDS_UA, M, hash_multiplication_probe)
display_closed_hash_table(hash_table_mult, "Результат Закритої Хеш-таблиці (Множення)")

# Аналіз довжин зондування
print("\n--- Аналіз Довжин Зондування (Кількість кроків для вставки) ---")
print("Метод Ділення:")
for word, length in lengths_div:
    print(f"  {word}: {length} кроків")

print("\nМетод Множення:")
for word, length in lengths_mult:
    print(f"  {word}: {length} кроків")
