import random
from fileinput import filename

# filename = 'f1.txt'

# with open(filename, 'w') as f:
#     f.write('New text!')
#
# with open(filename, 'r') as f:
#     text = f.read()
#     print(text)

# with open(filename, 'w') as file:
#     for n in range(0, 10):
#         file.write(str(random.randint(-10, 10)) + '\n')
#
#
# with open(filename, 'r') as file:
#     nuber = file.readline()
#     while nuber:
#         print(nuber)
#         nuber = file.readline()

# filename = 'f2.txt'
# with open(filename, 'w', encoding='utf-8') as file:
#     print(file.write('Text utf-8.'))

filename = 'b1.txt'
with open(filename, 'wb') as file:
    file.write(b'\x4E')
with open(filename, 'rb')as file:
    content = file.name
    print()
