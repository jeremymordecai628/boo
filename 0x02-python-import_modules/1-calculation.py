#!/usr/bin/python3 
from calculator_1 import add, sub, mul, div
a = 10
b = 5
sum_result = add(a ,b)
abstract = sub(a ,b) 
times =mul(a ,b)
result =div(a , b) 

print(f"{a} + {b} = {sum_result}")
print(f"{a} - {b} = {abstract}")
print(f"{a} * {b} = {times} ")
print(f"{a} / {b} = {result} ")

