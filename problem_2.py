#initial number
num1, num2 = 0,1
listValue = []

#start the loop for 10 numbers
while True:
    fibonacci = num1+num2
    if(fibonacci%2 == 0 and fibonacci <= 4000000):
        listValue.append(fibonacci)
    if(fibonacci >= 4000000):
        break
    num1 = num2
    num2 = fibonacci
print(sum(listValue))
