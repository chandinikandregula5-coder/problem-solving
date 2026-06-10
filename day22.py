'''
#ERROR HANDLING
try block---the try block,test a block of code for error
except block---the except block let hand if the code contain errors...

try:
    print(10/0)
except:
    print('this will handle zeroDivisionError')

else block:it is executed only when there is no error in try block code
-------------
note:it handles only the error in the flow of try block and not on the except block
try:
    print(5+"py")
except NameError:
     print('this will handle NameError')
else:
    print("no error")
    
try:
    print(5.4+"py")
except TypeError:
     print('this will handle typeError')
else:
    print("no error")

try:
   for i in range(1,10):
except:
   print(no error)
   
note:indentation errors and syntax errors not solved

finally block:it will be executed regardless of whether the code in try block has error or not.
