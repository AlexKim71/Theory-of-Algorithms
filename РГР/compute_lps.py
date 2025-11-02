def compute_lps(pattern):
    M = len(pattern)
    # lps (Longest Proper Prefix which is also a Suffix) - Префікс-функція π
    lps = [0] * M
    length = 0  # Довжина попереднього найдовшого префікс-суфікса
    i = 1
    
    while i < M:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Це ключовий елемент: повернення до попередньої довжини
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps
