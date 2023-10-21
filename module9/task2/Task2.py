with open("zen.txt", "r", encoding="UTF-8") as file:
    print("\n".join(i.rstrip() for i in file.readlines()[::-1]))
