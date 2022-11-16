def hello():
    print("Hi how are you!")
hello()

def pack(x,y,z):
    return[x, y, z]
print(pack("x", "y", "z"))

def eat_lunch(list):
    if len(list)  == 0:
        print("lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print("first I eat {list[0]}")
            else:
                print("Next I eat my{list[i]}")
eat_lunch([])
eat_lunch(["Burger", "Fries", "Hotdog"])