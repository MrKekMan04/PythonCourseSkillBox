from collections import Counter
from zipfile import ZipFile

with ZipFile("voina-i-mir.zip") as vim_zip:
    with vim_zip.open("voina-i-mir.txt") as file:
        clean_string = "".join([chr(char) for i in file.readlines() for char in i.rstrip()])

data = dict(Counter(clean_string))

print(data)
