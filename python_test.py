# Question1
x = [100,110,120,130,140,150]
d=[]
for y in x:
    d.append(y*5)
    print(d)

def divisible_by_three(n):
    for x in range(1,n):
        if(x%3==0):
            print(x)
divisible_by_three(21)
divisible_by_three(21)






# Question2

def divisibla_by_three(n):
     
    for num in range(n):
            if num % 3 == 0:
                print(str(num))
                 
            else:
                pass
if __name__ == "__main__":
     
    n = 100
    result(n)


# Question3
x = [[1,2],[3,4],[5,6],]

flatten_list = []

for subl in x:

    for item in subl:

        flatten_list.append(item)

print(flatten_list)

# Question4
y= [4,5,6,7,2]
y.sort()



    
# Qeustion5
def dublicate():
    x= ['a','b','a','e','d','b','c','e','f','g','h']
    final_list = set(x)
    print(list(final_list))


# Question 6
# def divisible_by_seven():
#     for n in range(100,200):
#         if (n%7==0):
#         print(n)
















