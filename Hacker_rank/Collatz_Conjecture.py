import matplotlib.pyplot as plt
num = int(input("input a number: "))
print(type(num))
highest = 1
highest = max(highest,num)
counter = 0
x = []
y = []
while num !=1:
    if num % 2 ==0:
        num = (num/2)
        x.append(counter)
        y.append(num)
        highest = max(highest,num)
        counter+=1
    else:
        num =(num*3+1)
        x.append(counter)
        y.append(num)
        highest = max(highest,num)
        counter+=1
print("The highest we went : {} with the steps :{} for the number :{}".format(highest,counter,num))
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('Iteration')
# naming the y axis
plt.ylabel('Number value')
  
# giving a title to my graph
plt.title('3N+1')
plt.show()