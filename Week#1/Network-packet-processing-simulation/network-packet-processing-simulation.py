from collections import namedtuple, deque
Request = namedtuple("Request", ("arrived_at", "time_to_process")) # Клас іменованих кортежів для формування списку запитів
Response = namedtuple("Response", ("was_dropped", "started_at")) # Клас іменованих кортежів для формування списку відповідей

class Buffer:
    def __init__(self, size):
        self.size = size # розмір буфера
        self.q_finish_times = deque()  # черга, у яку зберігаємо час завершення обробки пакета

    def process(self, request):
        arrived_at = request.arrived_at # час прибуття пакета
        time_to_process = request.time_to_process # час обробки пакета
        len_q = len(self.q_finish_times) # довжина черги

        if self.q_finish_times and arrived_at >= self.q_finish_times[0]: # якщо черга не порожня і час прибуття пакета
                                                            # перевищує час завершення обробки першого пакета з черги:
            self.q_finish_times.popleft() # видалення першого пакета з черги
            len_q = len(self.q_finish_times) # переобчислення довжини черги

        if len_q == self.size: # якщо довжин черги рівна розміру буфера:
            return Response(True, -1) # повертаємо was_dropped=True і значення -1

        last = len_q - 1 # номер останнього елемента черги
        if not self.q_finish_times or self.q_finish_times[last] <= arrived_at: # якщо черга порожня або час прибуття
                                                # пакета перевищує час завершення обробки останнього пакета з черги:
            started_at = arrived_at # значення часу початку обробки пакета рівне часу його прибуття
        else:
            started_at =  self.q_finish_times[last] # значення часу початку обробки пакета рівне часу
                                    # завершення обробки попереднього пакета (значення останнього елемента черги)

        finished_at = started_at + time_to_process  # обчислення часу завершення обробки пакета
        self.q_finish_times.append(finished_at)  # додавання часу завершення обробки пакета у кінець черги
        return Response(False, started_at) # повертаємо was_dropped=False і значення часу початку обробки пакета


def process_requests(requests, buffer): # функція, яка робить ітерацію по запитах, для кожного запиту викликає метод buffer.process(request), результат
    responses = []                      # кожного запиту записує у список відповідей
    for request in requests:
        response = buffer.process(request)
        responses.append(response)
    return responses


def main():
    #inF = open("22", "r")
    #outF = open("22.a", "w")
    buffer_size, n_requests = map(int, input().split())
    # buffer_size, n_requests = map(int, inF.readline().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        # arrived_at, time_to_process = map(int, inF.readline().split())
        request = Request(arrived_at, time_to_process)
        requests.append(request)

    buffer = Buffer(buffer_size) # створення екземпляру класу Buffer
    responses = process_requests(requests, buffer) # виклик функції process_requests
    for response in responses:
        print((response.started_at, -1)[response.was_dropped]) # вивід з використанням тернарного оператора
        # print(response.started_at)
        """if not response.was_dropped:
            #print(response.started_at, file=outF)
            print(response.started_at)
        else:
            #print(-1, file=outF)
            print(-1)"""
    #inF.close()
    #outF.close()


if __name__ == "__main__":
    main()