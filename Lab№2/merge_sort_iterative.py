
def merge_sort_iterative(A):
    """
    Ітеративний алгоритм сортування злиттям (Bottom-up).
    Включає підрахунок порівнянь та присвоєнь.
    """
    n = len(A)
    # Створюємо копію масиву для роботи, щоб не змінювати оригінал
    a = list(A)
    
    comparisons = 0
    assignments = n  # Початкове присвоєння 'a = list(A)'
    
    i = 1 # i - розмір підмасивів, що зливаються (1, 2, 4, 8...)
    assignments += 1

    # Основний цикл: ітерується по розміру блоків
    while i < n:
        comparisons += 1 # Порівняння i < n
        
        j = 0 # j - початковий індекс першого підмасиву
        assignments += 1
        
        # Цикл по проходах: ітерується по масиву
        while j < n - i:
            comparisons += 1 # Порівняння j < n - i
            
            left = j
            mid = j + i
            right = min(j + 2 * i, n)
            assignments += 3 # Присвоєння left, mid, right
            comparisons += 1 # Порівняння в min()
            
            # --- Логіка злиття (Merge) ---
            
            # Створюємо тимчасові підмасиви
            L = a[left:mid] 
            R = a[mid:right]
            
            # Присвоєння при копіюванні даних у тимчасові масиви
            assignments += len(L) + len(R) 

            k = left   # Початковий індекс у вихідному масиві 'a'
            l_idx = 0  # Індекс у L (Left)
            r_idx = 0  # Індекс у R (Right)
            assignments += 3 
            
            # Злиття L та R у масив 'a'
            while l_idx < len(L) and r_idx < len(R):
                comparisons += 1 # Порівняння в умові while
                comparisons += 1 # Порівняння в умові if: L[l_idx] <= R[r_idx]
                
                if L[l_idx] <= R[r_idx]:
                    a[k] = L[l_idx]
                    l_idx += 1
                else:
                    a[k] = R[r_idx]
                    r_idx += 1
                
                k += 1
                assignments += 2 # Присвоєння a[k] та інкремент l_idx/r_idx
                assignments += 1 # Присвоєння k
            
            # Додаємо залишки з L
            while l_idx < len(L):
                comparisons += 1 # Порівняння в умові while
                a[k] = L[l_idx]
                k += 1
                l_idx += 1
                assignments += 3 # Присвоєння a[k], k, l_idx
            comparisons += 1 # Порівняння, що завершило цикл

            # Додаємо залишки з R
            while r_idx < len(R):
                comparisons += 1 # Порівняння в умові while
                a[k] = R[r_idx]
                k += 1
                r_idx += 1
                assignments += 3 # Присвоєння a[k], k, r_idx
            comparisons += 1 # Порівняння, що завершило цикл
            
            # --- Кінець логіки злиття ---
            
            j += 2 * i
            assignments += 1 # Присвоєння j

        comparisons += 1 # Порівняння j < n - i, що завершило внутрішній цикл
        
        i *= 2
        assignments += 1 # Присвоєння i
    
    comparisons += 1 # Порівняння i < n, що завершило зовнішній цикл
    
    return a, comparisons, assignments

# Приклад використання
my_list = [58, 5, 50, 99, 61, 32, 27, 45, 75]

# Виконання сортування та отримання лічильників
sorted_list, comps, assigs = merge_sort_iterative(my_list.copy())

print(f"Оригінальний список: {my_list}")
print(f"Відсортований список: {sorted_list}")
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоєнь: {assigs}")
