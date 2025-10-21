def selection_sort(arr):
    n = len(arr)
    # Ініціалізація лічильників
    comparisons = 0
    assignments = 0

    # # Зовнішній цикл ітерується по всьому списку
    # # від 0 до n-2 проходів
    for i in range(n - 1):
        
        # # Припускаємо, що поточний елемент є мінімальним
        min_index = i
        assignments += 1  # Присвоєння змінній min_index
        
        # # Внутрішній цикл шукає найменший елемент в решті списку
        for j in range(i + 1, n):
            comparisons += 1  # Операція порівняння arr[j] < arr[min_index]
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1  # Присвоєння змінній min_index

        # # Обмін елементів, якщо знайдено новий мінімальний
        comparisons += 1  # Операція порівняння min_index != i (хоча в чистому коді може бути неявним, тут рахуємо для логіки)
        if min_index != i:
            # # Обмін елементів
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3  # Три присвоєння при обміні (темп, arr[i], arr[min_index])

    return arr, comparisons, assignments

my_list = [58, 5, 50, 99, 61, 32, 27, 45, 75]

# Виконання сортування та отримання лічильників
# Використання .copy(), щоб не змінювати оригінал
sorted_list, comps, assigs = selection_sort(my_list.copy()) 

print(f"Оригінальний список: {my_list}")
print(f"Відсортований список: {sorted_list}")
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоєнь: {assigs}")
