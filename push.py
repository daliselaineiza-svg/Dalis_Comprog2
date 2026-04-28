try:
    f = open("group4ever.txt", "x")
    f.write("Shopping list Manager")
    f.close()
except Error:
    print("Error")