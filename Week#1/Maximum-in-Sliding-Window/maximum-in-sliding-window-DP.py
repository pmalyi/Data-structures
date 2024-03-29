# Рішення з використанням динамічного програмування. Складність O(n)

def max_sliding_window(sequence, m, n):
    maximums = []
    right = [0] * n  # масив, у якому буемо записувати значення за правилом:
                    #  кожен елемент масиву є номером найближчого справа більшого елемента масиву sequence
    right[n - 1] = n # призначимо крайньому правому елементу значення n

    for i in range(n - 2, -1, -1): # ітеруємось реверсом від n - 2 до 0
        r = i + 1 # номер наступного (правого) елемента.
        while (r < n and sequence[r] <= sequence[i]): # поки r лежить у межах масиву та правіший елемент масиву sequence
                                                        # менший за поточний елемент
            r = right[r] # перевизначаємо номер наступного (правіше) ще більшого елемента масиву sequence
        right[i] = r # присвоюємо і-му елементу масиву right значення r

    i = 0
    j = 0
    while i <= n - m: # Тепер ітеруємося по і від 0 до n - m (в межах першого вікна)

        if i > j: # Якщо j більше немає у вікні.
            j = i # j присвоюємо номер першого елемента вікна

        while right[j] < i + m:
            j = right[j]   # Пошук номера найбільшого елемента вікна.

        if j == n:
            maximums.append(sequence[i]) # Якщо j виходить за межі масиву, це означає, що a[i] є найбільшим елементом
        else:
            maximums.append(sequence[j]) # В іншому випадку a[j] є найбільшим елементом вікна.

        i += 1

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    print(*max_sliding_window(input_sequence, window_size, n))
