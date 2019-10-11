#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# my mathematical failure sadface

# def eating_cookies(n, cache=None):
#   if n == 2:
#     return 2
#   if n == 1 or n == 0:
#     return 1
#   final_answer = 0
#   inner_increase = 1
#   for i in range (1,n-2):
#     for j in range(0, i):
#       inner_increase = inner_increase + j
#     final_answer = final_answer + inner_increase 
#   return (2**(n-1) - final_answer)

# def eating_cookies(n, cache=None):

#   print(cache[n-1])
#   if n == 0 or n == 1:
#     return 1
#   if n == 2:
#     return 2
#   if n == 3:
#     return 4
#   if n > 3:
#     if cache[n-1] != 0:
#       a = cache[n-1]
#     else:
#       a = eating_cookies(n-1,cache)
#       cache[n-1] = a
#     if cache[n-2] != 0:
#       b = cache[n-2]
#     else:
#       b = eating_cookies(n-2,cache)
#       cache[n-2] = b
#     if cache[n-3] != 0:
#       c = cache[n-3]
#     else:
#       c = eating_cookies(n-3,cache)
#       cache[n-3] = c
#     return (a+b+c)

def eating_cookies(n, cache=None):

  
   if n == 0 or n == 1:
     return 1
   if n == 2:
     return 2
   if n == 3:
     return 4
   if n > 3:
    if cache: 
      if cache[n-1] != 0:
        a = cache[n-1]
      else:
        a = eating_cookies(n-1,cache)
        cache[n-1] = a
      if cache[n-2] != 0:
        b = cache[n-2]
      else:
        b = eating_cookies(n-2,cache)
        cache[n-2] = b
      if cache[n-3] != 0:
        c = cache[n-3]
      else:
        c = eating_cookies(n-3,cache)
        cache[n-3] = c
      return (a+b+c)
    else:
       return(eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))

# def eating_cookies(n, cache=None):

#   if n == 0 or n == 1:
#     return 1
  
#   if n == 2:
#     return 2
  
#   if n == 3:
#     return 4
  
#   if n > 3:
#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

print(eating_cookies(8))