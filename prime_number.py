import numpy as np 

def prime_num(num):
  if num<2:
    prime=False
  for i in range(2, num):
     if  (num % i)== 0:
        prime=False
     else:
        prime=True
  return prime
   

while True:
    num = input("Write a number: ")
    if num == "exit":
        break
    else:
        num = int(num)
    if prime_num(num) == True:
        print(f"{num} is Prime")
    else:
        print(f"{num} is not prime")