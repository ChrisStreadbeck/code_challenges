#takes in two numbers and an operator, then returns the evaluated answer

import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}   

def maths(a,b, op_char):
  op_func = ops[op_char]
  return op_func(a, b)

print(maths(2, 5, "+"))


#------------------------------------
#find the median of a list of numbers

import statistics

numlist = [4, 8, 12, 62, 1, 6, 19, 14]

def median_num(nums):
  return statistics.median(nums)

print(median_num(numlist))