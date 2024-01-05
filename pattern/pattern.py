#This program prints star(asterisk) patters using if-else and a single for loop

'''
The pattern that will be produced when the code below runs is:

*
**
***
****
*****
****
***
**
*

'''

#intialising variables
stars = "*"
index = 9

for i in range(0,index):
        if i < 5:
                print(stars)
                stars += "*" #one asterisk at a time is concatenated to the string 'stars'
        else:
                print(stars[0:index-i]) #prints the string 'stars' by slicing one asterisk at a time
                
        

