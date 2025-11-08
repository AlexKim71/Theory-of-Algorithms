def quicksort_recursive(a, l, r):
    """
    Рекурсивна реалізація алгоритму швидкого сортування з підрахунком операцій,
    за схемою Хоара.
    Повертає (total_comparisons, total_assignments, total_recursive_calls).
    """
    total_comparisons = 0
    total_assignments = 0
    
    # ⚠️ КОРИГУВАННЯ: Рахуємо цей виклик ТІЛЬКИ якщо це не базовий випадок (l < r)
    # Якщо l >= r, це базовий випадок, і ми повертаємо 0 викликів.
    if l >= r:
        return 0, 0, 0
    
    total_recursive_calls = 1 # Рахуємо цей виклик (оскільки l < r)

    # 1. Розбиття масиву
    # q - це індекс j (точка розбиття)
    q, c1, a1 = partition_hoare_original(a, l, r)
    total_comparisons += c1
    total_assignments += a1
        
    # 2. Рекурсивні виклики для лівого та правого підмасивів
    # Примітка: Лівий підмасив включає точку розбиття q (за схемою Хоара)
    c2, a2, r2 = quicksort_recursive(a, l, q)
    c3, a3, r3 = quicksort_recursive(a, q + 1, r)
        
    total_comparisons += c2 + c3
    total_assignments += a2 + a3
    total_recursive_calls += r2 + r3
        
    return total_comparisons, total_assignments, total_recursive_calls

def partition_hoare_original(a, l, r):
    """
    Допоміжна функція для розділення масиву за схемою Хоара.
    Використовує перший елемент як опорний (a[l]).
    Повертає індекс 'j' (точки розбиття) та лічильники.
    """
    comparisons = 0
    assignments = 0
    
    # Вибір опорного елемента (pivot) - перший елемент
    pivot = a[l]
    assignments += 1
    
    # ⚠️ КОРИГУВАННЯ: ініціалізація індексів
    i = l - 1
    j = r + 1
    assignments += 2
    
    while True:
        # Рухаємо індекс i вправо
        i += 1
        assignments += 1 # Присвоєння інкрементованого i
        while a[i] < pivot:
            comparisons += 1
            i += 1
            assignments += 1 # Присвоєння інкрементованого i
        comparisons += 1  # Порівняння, що завершило цикл (a[i] >= pivot)

        # Рухаємо індекс j вліво
        j -= 1
        assignments += 1 # Присвоєння декрементованого j
        while a[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1 # Присвоєння декрементованого j
        comparisons += 1  # Порівняння, що завершило цикл (a[j] <= pivot)
        
        # Перевірка на перетин індексів
        comparisons += 1
        if i >= j:
            # j - це точка розбиття, повертаємо її
            return j, comparisons, assignments
            
        # Обмін елементів a[i] та a[j]
        # Використовуємо тимчасову змінну для коректного підрахунку присвоєнь
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        assignments += 3 # Три присвоєння при обміні (temp=a[i], a[i]=a[j], a[j]=temp)

# --- Блок для введення даних та виконання ---
try:
    # Запит на введення даних
    # Приклад для тестування: 58, 5, 50, 99, 61, 32, 27, 45, 75
    input_str = input("Введіть елементи масиву через кому (наприклад, 89, 45, 68, 90, 29, 34, 17): ")
    
    # Парсинг введеного рядка
    my_list_rec = [int(x.strip()) for x in input_str.split(',')]
    
    if not my_list_rec:
        print("Масив порожній. Сортування не виконано.")
    else:
        print("\n--- РЕКУРСИВНЕ ШВИДКЕ СОРТУВАННЯ (за схемою Хоара) ---")
        print(f"Оригінальний список: {my_list_rec}")

        # Створення копії для сортування, щоб зберегти оригінал
        list_copy = my_list_rec.copy()

        # Перший виклик функції
        total_comps, total_assigs, total_calls = quicksort_recursive(list_copy, 0, len(list_copy) - 1)

        print(f"Відсортований список: {list_copy}")
        print(f"Загальна кількість порівнянь: {total_comps}")
        print(f"Загальна кількість присвоювань: {total_assigs}")
        print(f"Загальна кількість рекурсивних викликів: {total_calls}")

except ValueError:
    print("\nПомилка: Некоректний формат введених даних. Переконайтеся, що ви ввели числа через кому.")
except Exception as e:
    # ⚠️ Видалено виведення помилки 'e' для чистоти, але в реальному коді можна залишити
    print(f"\nВиникла непередбачувана помилка.")
