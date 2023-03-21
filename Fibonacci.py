import time


#RecursionError maximum recursion depth exceeded
def fib1(n: int):
    return fib1(n-1) + fib1(n-2)


#With base and recursion case
def fib2(n: int):
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)


#with memoization
from typing import Dict
memo: Dict[int, int] = {0:0, 1:1}#base case

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n - 2)#memoization
    return memo[n]


#with automemoization with cache
from functools import lru_cache
@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n-1) + fib4(n-2)


#iterative method
def fib5(n: int) -> int:
    if n == 0: return 0
    last: int = 0 #if initial val fib(0)
    next: int = 1 #if initial val fib(1)
    for _ in range(1,n):
        last, next = next, last + next
    return next


#genarator meth
from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
    yield 0 #special case
    if n > 0: yield 1
    last: int = 0 #if initial val fib(0)
    next = int = 1 #if initial val fib(1)
    for _ in range(1,n):
        last, next = next, last + next
        yield next # Its main stage of generation

if __name__ == '__main__':
    start_time = time.time()
    #print(fib5(50))
    print(time.time()-start_time)