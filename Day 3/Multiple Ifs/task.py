print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Type y for yes and n for no.\n")
    if wants_photo == "y":
        bill += 3
        print(f"You have to pay ${bill}")
    print(f"You have to pay ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
