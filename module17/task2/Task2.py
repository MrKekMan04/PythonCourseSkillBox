from typing import List

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

zipped = list(map(lambda arr1, arr2: (arr1, arr2), letters, numbers))
