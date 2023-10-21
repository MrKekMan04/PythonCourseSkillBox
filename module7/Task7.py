def my_zip(first: iter, second: iter) -> iter:
    for i in range(min(len(first), len(second))):
        yield first[i], second[i]


string = "abcd"
numbers = (10, 20, 30, 40)

print(my_zip(string, numbers))
print("\n".join(str(i) for i in my_zip(string, numbers)))
