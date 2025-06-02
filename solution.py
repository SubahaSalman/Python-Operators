english = int(input("Enter your grade for english: "))
mathematics = int(input("Enter your grade for mathematics: "))
biology = int(input("Enter your grade for biology: "))
chemistry = int(input("Enter your grade for chemistry: "))

sum = english+mathematics+biology+chemistry
percent = (sum/400)*100

print("Your Percentage Mark is", percent)