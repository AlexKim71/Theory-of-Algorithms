def brute_force_search(text, pattern):
    # Довжина тексту N та шаблону M
    N = len(text)
    M = len(pattern)
    
    # Ітерація по всіх можливих початкових позиціях у тексті
    for i in range(N - M + 1):
        j = 0
        # Порівняння символів шаблону з відповідною частиною тексту
        while j < M and text[i + j] == pattern[j]:
            j += 1
        
        # Якщо знайдено повний збіг
        if j == M:
            return i  # Повертає індекс першого входження
            
    return -1  # Підрядок не знайдено
