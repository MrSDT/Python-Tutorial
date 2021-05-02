# Convertor Part
print("Welcome to KM/s Convertor to Miles")
UserInput = input("Type Km: ")
Mile = float(UserInput) / 1.60934
Mile = round(Mile,2)
print(f"{UserInput} Km/s is {Mile} Mile")
print("--------------------------------")
# Date of Birth Part
UserBirth = input("What is your date of birth: ")
print("Your Date of Birth is: " + UserBirth)
print("--------------------------------")
# User Name Part
UserName = input("What is your name: ")
# Result
print(f"Your name is : {UserName} & Your Date of Birth is : {UserBirth} and You are Driving At {Mile} Miles")