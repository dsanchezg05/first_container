import numpy as np 

def prime_num(num):
  if num<2:
    return False
  for i in range(2, num):
     if  (num % i)== 0:
        return False
     else:
        return True
   
num_list = []
while True:
    num = input("Write a number: ")
    if num == "exit":
        break
    else:
        num = int(num)
        num_list.append(num)
    if prime_num(num) == True:
        print(f"{num} is Prime")
    else:
        print(f"{num} is not prime")

with open("num_file.txt","w") as f:
  for n in num_list:
    f.write(f"{n}\n")

