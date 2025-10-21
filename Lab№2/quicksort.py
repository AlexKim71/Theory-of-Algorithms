def partition(a, l, r):
    """
    Допоміжна функція для розділення масиву за схемою Хоара.
    """
    comparisons = 0
    assignments = 0

    # Вибір опорного елемента (перший елемент)
    pivot = a[l]
    assignments += 1
    
    # Індекси i та j
    i = l - 1
    j = r + 1
    assignments += 2

    while True:
        # Шукаємо елемент, що більший або дорівнює опорному
        i += 1
        assignments += 1
        while a[i] < pivot:
            comparisons += 1
            i += 1
            assignments += 1

        # Порівняння для виходу з циклу (a[i] >= pivot)
        comparisons += 1

        # Шукаємо елемент, що менший або дорівнює опорному
        j -= 1
        assignments += 1
        while a[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1

        # Порівняння для виходу з циклу (a[j] <= pivot)
        comparisons += 1

        comparisons += 1
        if i >= j:
            # Поділ завершено, повертаємо індекс
            return j, comparisons, assignments

        # Обмін елементів
        a[i], a[j] = a[j], a[i]
        assignments += 3

def quicksort(a, l, r):
    """
    Рекурсивна реалізація алгоритму швидкого сортування з підрахунком операцій, за схемою Хоара.
    """
    if l < r:
        # Виконання partition
        q, c1, a1 = partition(a, l, r)
        
        # Рекурсивні виклики
        c2, a2, r2 = quicksort(a, l, q)
        c3, a3, r3 = quicksort(a, q + 1, r)
        
        # Підсумок лічильників
        total_comparisons = c1 + c2 + c3
        total_assignments = a1 + a2 + a3
        total_recursive_calls = 1 + r2 + r3 # 1 - поточний виклик
        
        return total_comparisons, total_assignments, total_recursive_calls
    else:
        # Базовий випадок
        return 0, 0, 1 # Повертаємо 1 виклик для підрахунку базових викликів

# Приклад використання
# Використовуємо Ваші вхідні дані: [58, 5, 50, 99, 61, 32, 27, 45, 75]
my_list = [58, 5, 50, 99, 61, 32, 27, 45, 75]
original_list = my_list.copy()

total_comparisons, total_assignments, total_recursive_calls = quicksort(my_list, 0, len(my_list) - 1)

print("Оригінальний список:", original_list)
print("Відсортований список:", my_list)
print(f"Загальна кількість порівнянь: {total_comparisons}")
print(f"Загальна кількість присвоювань: {total_assignments}")
print(f"Загальна кількість рекурсивних викликів: {total_recursive_calls}")
