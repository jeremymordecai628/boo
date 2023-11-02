#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    # Define variables a and b in separate lines
    a = 10
    b = 5

    # Perform mathematical operations using the imported functions
    sum_result = add(a, b)
    difference_result = sub(a, b)
    product_result = mul(a, b)
    division_result = div(a, b)

    # Print the results
    print(f"{a} + {b} = {sum_result}")
    print(f"{a} - {b} = {difference_result}")
    print(f"{a} * {b} = {product_result}")
    print(f"{a} / {b} = {division_result}")

