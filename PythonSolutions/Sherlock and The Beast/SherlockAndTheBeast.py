#!/bin/python3

import sys


T=int(input())

K=[int(input()) for i in range(T)]

for k in K:
  #3x+5y=k maximize x
  for x in range(k//3,-1,-1):
    if (k-3*x)%5==0:
      y=(k-3*x)//5
      print('5'*3*x+'3'*5*y)
      break
    elif x==0:
      print(-1)