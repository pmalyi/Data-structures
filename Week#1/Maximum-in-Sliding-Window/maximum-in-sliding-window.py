# Рішення з використанням двохсторонньої черги. Складність O(n)
from collections import deque


def max_sliding_window(sequence, m, n):
    maximums = []
    dq = deque()
    for i in range(n):

        while dq and sequence[dq[-1]] < sequence[i]: # доки черга не порожня і елемент з крайнім правим номером черги
            # менший за елемент з поточним  номером
            dq.pop()  # видаляємо з черги крайні праві номери елементів, які менші за свого сусіда справа

        dq.append(i) # додаємо поточний номер в кінець черги

        if dq and dq[0] < i - m + 1: # якщо крайній лівий номер в черзі менший за номер крайнього лівого елемента вікна
            dq.popleft() # видаляємо з черги крайній лівий номер

        if i >= m - 1: # починаючи з номера, який рівний або більший за розмір вікна мінус 1
            maximums.append(sequence[dq[0]]) # додаємо до результуючого списку елементи з номером, який рівний значенню
                                            # крайного лівого в черзі

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    print(*max_sliding_window(input_sequence, window_size, n))
