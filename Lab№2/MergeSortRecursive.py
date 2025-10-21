def merge(left, right):
    """
    Допоміжна функція для злиття двох відсортованих списків.
    Підраховує порівняння та присвоєння під час злиття.
    """
    merged_arr = []
    comparisons = 0
    # Присвоєння: 1 для merged_arr, 1 для i, 1 для j (хоча i=0, j=0)
    assignments = 3 
    
    i = 0
    j = 0
    
    # Зливаємо елементи з обох масивів
    while i < len(left) and j < len(right):
        comparisons += 2  # Порівняння в умові while
        
        comparisons += 1  # Порівняння в умові if
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
        assignments += 2  # Присвоєння (append) + присвоєння (i+=1 або j+=1)
        
    comparisons += 1 # Фінальне порівняння в умові while

    # Додаємо елементи, що залишилися з лівого масиву
    while i < len(left):
        comparisons += 1  # Порівняння в умові while
        merged_arr.append(left[i])
        i += 1
        assignments += 2  # Присвоєння (append) + присвоєння (i+=1)
    comparisons += 1  # Фінальне порівняння в умові while

    # Додаємо елементи, що залишилися з правого масиву
    while j < len(right):
        comparisons += 1  # Порівняння в умові while
        merged_arr.append(right[j])
        j += 1
        assignments += 2  # Присвоєння (append) + присвоєння (j+=1)
    comparisons += 1  # Фінальне порівняння в умові while

    return merged_arr, comparisons, assignments

def merge_sort_recursive_with_counters(arr):
    """
    Рекурсивна функція сортування злиттям з підрахунком операцій.
    """
    comparisons = 0
    assignments = 0
    recursive_calls = 1 # Кожен виклик функції = 1
    
    comparisons += 1 # Порівняння len(arr) <= 1
    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls

    mid = len(arr) // 2
    assignments += 1 # Присвоєння mid
    
    # Рекурсивно ділимо масив на дві половини
    # Зверніть увагу: нарізка масиву (arr[:mid], arr[mid:]) також є присвоєннями
    left_half, c1, a1, r1 = merge_sort_recursive_with_counters(arr[:mid])
    right_half, c2, a2, r2 = merge_sort_recursive_with_counters(arr[mid:])
    
    # Підсумовуємо результати рекурсивних викликів
    comparisons += c1 + c2
    assignments += a1 + a2
    recursive_calls += r1 + r2
    assignments += len(arr) # Додаткові присвоєння при нарізці (копіюванні) масиву

    # Зливаємо відсортовані половини
    merged_arr, c_merge, a_merge = merge(left_half, right_half)
    
    comparisons += c_merge
    assignments += a_merge
    # Присвоєння merged_arr не включаємо, бо це повернення
    
    return merged_arr, comparisons, assignments, recursive_calls

# Приклад використання
my_list = [58, 5, 50, 99, 61, 32, 27, 45, 75]
original_list = my_list.copy()

# Виконання сортування
# Присвоєння total_recursive_calls (r_calls) додано
sorted_list, total_comparisons, total_assignments, total_recursive_calls = \
    merge_sort_recursive_with_counters(original_list)

print(f"Оригінальний список: {my_list}")
print(f"Відсортований список: {sorted_list}")
print(f"Загальна кількість порівнянь: {total_comparisons}")
print(f"Загальна кількість присвоєнь: {total_assignments}")
print(f"Загальна кількість рекурсивних викликів: {total_recursive_calls}")
