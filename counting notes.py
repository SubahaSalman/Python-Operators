amount = int(input("Enter the desired amount:"))

note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//20

print(" Notes of 100 rupee", note1)
print(" Notes of 50 rupee", note2)      
print(" Notes of 20 rupee", note3)