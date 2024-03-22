#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__stack_max = [0,]

    def Push(self, a):
        top = - 1
        if a > self.__stack_max[top]:
            self.__stack_max.append(a)
        else:
            self.__stack_max.append(self.__stack_max[top])
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__stack_max.pop()

    def Max(self):
        assert(len(self.__stack_max))
        result = self.__stack_max.pop()
        self.__stack_max.append(result)
        return result


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
