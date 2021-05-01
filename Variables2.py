# Unpacking Values from List and Import it Into Variables
names = ["Mohamad" , "Hamed" , "Ali"]
name3 , name2 , name1 = names
print(name1)
print(name2)
print(name3)
print("----------------------------")
#----------Local and Global Variables------------#
hello = "Global Var"

def myfunc():
    hello = "Local Var"
    print(hello)
myfunc()
print(hello)
# You can Make a Local Variable Global by Typing "global variable_name" Inside Function
