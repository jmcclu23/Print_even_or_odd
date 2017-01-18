############################################################
### CheckOddEven.py:Check if a number is Odd or Even     ###
### Input: Any number                                    ###
### Output: Prints whether an Even or Odd Number         ###
### Author: Joshua McClure                               ###
### 2018-08-17                                           ###
############################################################

############################################################
#                         Variables                        #
############################################################

number_input = int(input('Please input a number:'))

############################################################
#                         Operation                        #
############################################################

number_check = number_input % 2

############################################################
#                          Output                          #
############################################################

if(number_check == 0):
    print('Even Number')
else:
    print('Odd Number')
    

