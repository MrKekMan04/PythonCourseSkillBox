from Entities import MyFileManager


with MyFileManager("test.txt") as file:
    """ Successfully write 'cause file doesn't exists and opened in write mode """
    file.write("12345")

with MyFileManager("test.txt") as file:
    try:
        file.write("124")
    except IOError as e:
        print(f"Got IO Exception 'cause file exists and opened in read mode")

    print("But program works!")
