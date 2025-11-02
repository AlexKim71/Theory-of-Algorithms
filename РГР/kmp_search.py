def kmp_search(text, pattern):
    N = len(text)
    M = len(pattern)
    
    # 1. Попередня обробка: побудова префікс-функції
    lps = compute_lps(pattern)
    
    i = 0  # Індекс для тексту
    j = 0  # Індекс для шаблону
    
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
        if j == M:
            # Знайдено збіг
            return i - j
        
        elif i < N and pattern[j] != text[i]:
            # Невідповідність після j збігів
            if j != 0:
                # Перехід за допомогою таблиці lps
                j = lps[j - 1]
            else:
                i += 1
                
    return -1 # Підрядок не знайдено
