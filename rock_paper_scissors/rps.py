#!/usr/bin/python

import sys

# def rock_paper_scissors2(n):
#   result = []
#   if n == 1:
#     result = [['rock'],['paper'],['scissors']]
#   else:
#     for i in rock_paper_scissors2(n-1):
#       for j in rock_paper_scissors2(1):
#         result.append(i+j)

#   return result

def rock_paper_scissors(n):
    results = []
    if n == 0:
      return [[]]
    if n == 1:
        return [["rock"], ["paper"], ["scissors"]]
    else:
        for i in rock_paper_scissors(n - 1):
          results.append(i + ['rock'])
          results.append(i + ['paper'])
          results.append(i + ['scissors'])
    return results


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')