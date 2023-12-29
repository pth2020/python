#This program prompts a user to enter two
#integers. It works out the higher common factor(HFC)
#of the two numbers and outputs the result

def find_hcf(a, b):
    if a < b:
        for i in range(1,int(b/2+1)):
            if a % i == 0 and b % i == 0:
                hcf = i
    elif a > b:
        for i in range(1,int(a/2+1)):
            if b % i == 0 and a % i == 0:
                hcf = i        
    else:
        hcf = a
        
    return hcf

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
print(f"The hcf of {first_number} and {second_number} is {find_hcf(first_number,second_number)}")
