def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    # Зовнішній цикл: ітерується по всьому списку
    for i in range(n - 1):
        # Припускаємо, що поточний елемент є мінімальним
        min_index = i
        assignments += 1  # Присвоєння змінній min_index

        # Внутрішній цикл: шукає найменший елемент у решті списку
        for j in range(i + 1, n):
            comparisons += 1  # Операція порівняння
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1  # Присвоєння змінній min_index

        # Обмін елементів, якщо знайдено новий мінімальний
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3  # Три присвоєння при обміні
    return arr, comparisons, assignments

# Вхідні дані з вашого варіанту 22
data = [79, 43, 31, 5, 66, 62, 34, 76]

# Створення копії списку для сортування
sorted_data, comps, assigs = selection_sort(data.copy())
# Вивід результатів
print("Оригінальний список:", data)
print("Відсортований список:", sorted_data)
print("Кількість порівнянь:", comps)
print("Кількість присвоєнь:", assigs)
