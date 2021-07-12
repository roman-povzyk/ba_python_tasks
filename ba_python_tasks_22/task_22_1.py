from typing import List, Tuple
import functools
import time


# We assume that all lists passed to functions are same length N answers
# 1 - n
# 2 - 1
# 3 - n^2
# 4 - n
# 5 - n^2
# 6 - log n

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Name: {func}. Elapsed time: {elapsed_time:0.7f} seconds")
        return value

    return wrapper_timer


@timer
def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        for el_second_list in second_list:
            res.append(el_first_list)
    return res


@timer
def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n


@timer
def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


@timer
def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


@timer
def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


@timer
def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n


question1([1, 2, 3], [4, 5])
question2(5)
question3([1, 2, 3], [4, 5])
question4([1, 2, 3, 4, 5])
question5(5)
question6(5)
