def insertion_sort(arr):
    # Вихідні дані: масив arr [0, ..., n-1] елементів, що впорядковуються у зростаючому порядку
    # Початковий масив: arr = [79, 43, 31, 5, 66, 62, 34, 76]
    n = len(arr)
    comparisons = 0
    assignments = 0
    # Цикл ітерується від другого елемента до кінця
    # i - це індекс елемента, який потрібно вставити
    for i in range(1, n):
        # Зберігаємо поточний елемент для вставки
        key = arr[i]
        assignments += 1
        # j - індекс попереднього елемента
        j = i - 1
        assignments += 1
        # Пересуваємо елементи, що більші за key,
        # вправо, щоб звільнити місце для вставки
        while j >= 0 and arr[j] > key:
            comparisons += 1  # Порівняння в умові while
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1
        # Додаткове порівняння, коли умова while стає false
        # (якщо j не стало менше 0)
        if j >= 0:
            comparisons += 1
        # Вставляємо key на його правильне місце
        arr[j + 1] = key
        assignments += 1
    return arr, comparisons, assignments

# Приклад використання
my_list = [79, 43, 31, 5, 66, 62, 34, 76]
sorted_list, comps, assigs = insertion_sort(my_list.copy())
print("Оригінальний список:", my_list)
print("Відсортований список:", sorted_list)
print("Кількість порівнянь:", comps)
print("Кількість присвоєнь:", assigs)
