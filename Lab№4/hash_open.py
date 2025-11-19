# --- ДОПОМІЖНІ ФУНКЦІЇ --- (ті, що у вас вже є: calculate_k, simple_hash_from_map)
# ... (залишити без змін) ...

# Оновлена назва функції
def build_chained_hash_table(words: list, m: int) -> list:
    """
    Будує хеш-таблицю з роздільними ланцюжками (списками) за методом ділення.
    Повертає хеш-таблицю.
    """
    hash_table = [[] for _ in range(m)] # Ініціалізація списку списків

    for word in words:
        k = calculate_k(word)
        address = simple_hash_from_map(k) # Використовуємо вашу хеш-функцію
        hash_table[address].append(word) # Додаємо слово до відповідного ланцюжка
    return hash_table

# Оновлена назва функції
def display_chained_hash_table(table: list, title: str):
    """Виводить хеш-таблицю з ланцюжками у зручному форматі."""
    print(f"\n--- {title} (Таблиця M={M}) ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {', '.join(chain) if chain else '[]'}")
    print()

# --- ВИКОНАННЯ ---
# print("АЛГОРИТМ ХЕШУВАННЯ З РОЗДІЛЬНИМИ ЛАНЦЮЖКАМИ") # Можливо, додати такий заголовок

# Будівництво таблиці
# Оновлена назва функції
chained_hash_table = build_chained_hash_table(WORDS_UA, M)
# Оновлена назва функції та заголовок
display_chained_hash_table(chained_hash_table, "Результат Хеш-таблиці з роздільними ланцюжками")
