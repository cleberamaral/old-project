date = input("Enter today's date: ")
rate = input("How do you rate your mood today from 1 to 10? ")
thoughts = input ("Let your toughts flow: ")

with open (f"../journal/{date}.txt","w") as file:
    file.write(rate + 2 * "\n") 
    file.write(thoughts)

