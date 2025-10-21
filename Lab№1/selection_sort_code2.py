def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    # Цикл ітерується від другого елемента до кінця
    # i – це індекс елемента, який потрібно вставити 
    for i in range(1, n):
        
        # Зберігаємо поточний елемент для вставки
        key = arr[i]
        assignments += 1

        # j – індекс попереднього елемента
        j = i - 1
        assignments += 1
        
        # Пересуваємо елементи, що більші за key,
        # вправо, щоб звільнити місце для вставки
        while j >= 0 and arr[j] > key:
            
            # Порівняння в умові while (arr[j] > key)
            comparisons += 1
            
            arr[j + 1] = arr[j]
            assignments += 1 # Присвоєння елементу масиву
            
            j = j - 1
            assignments += 1 # Присвоєння змінній j
            
        # Додаткове порівняння, коли умова while стає false
        # Якщо цикл зупинився через arr[j] <= key
        if j >= 0:
            comparisons += 1
            
        # Вставляємо key на його правильне місце
        arr[j + 1] = key
        assignments += 1

    return arr, comparisons, assignments

my_list = [58, 5, 50, 99, 61, 32, 27, 45, 75]

# Використання .copy(), щоб не змінювати оригінал
sorted_list, comps, assigs = insertion_sort(my_list.copy()) 

print(f"Оригінальний список: {my_list}")
print(f"Відсортований список: {sorted_list}")
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоєнь: {assigs}")
