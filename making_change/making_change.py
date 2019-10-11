#!/usr/bin/python

import sys

# def making_change(amount, denominations):
#   total = 0

#   if len(denominations) == 1:
#     return 1
#   else:
#     if (amount - (denominations[-1])) >= 0:
#       q = amount//denominations
#       b = q*making_change(amount - denominations[-1]*q,denominations)
#       popped = denominations
#       popped.pop()
#       return b + making_change(amount-denominations[-1]*q,popped)
#     else:
#       popped = denominations
#       popped.pop()
# #       return making_change(amount,popped)



#   for i in denominations:
#     if i >= amount:
#       total = total + making_change

def making_change(amount, denominations):
  if amount == 0:
    return 1

  if len(denominations) == 1:
    return 1



  else:
    if (amount - (denominations[-1])) >= 0:
      q = amount//denominations[-1]
      b = 0 
      popped = list(denominations) 
      z = popped.pop()
      for i in range(0,q+1):
        b = b + making_change(amount - z*i,popped)
      

      return b
    else:
      popped = denominations
      popped.pop()
      return making_change(amount,popped)


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")