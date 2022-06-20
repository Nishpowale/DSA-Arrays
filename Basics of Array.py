user=int(input('Enter the maximum number:'))
odd_nums=[]
for i in range (1,user):
    if i % 2 != 0 :
        odd_nums.append(i)

print('The odd numbers from one to the max number are :',odd_nums)
