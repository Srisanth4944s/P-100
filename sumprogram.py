def squareEach(num1, num2, num3):

    sq1=num1**2
    sq2=num2**2
    sq3=num3**2
    return sq1, sq2, sq3

def sumList(lst):
    return sum(lst)

num1,num2,num3=eval(input("Enter three integers: "))
square=squareEach(num1,num2,num3)
sum_of_Squared=sumList(square)
print(sum_of_Squared)