# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 17:23:39 2021

@author: atman
"""
from multiprocessing import Process, Queue
import os
import time

workers_number = 4
final_fibonacci_number = 40

def worker(tasks: Queue, process_index: int):
    def fib(n: int) -> int:
        return fib(n-1) + fib(n-2) if n > 2 else 1
    while not tasks.empty(): # пока очередь не пуста, выполняем одну очередную задачу
        number = tasks.get()
        answer = fib(number)
        print(f"worker {process_index}, PID={os.getpid()}: fib({number}) = {answer}")
        
def main()
