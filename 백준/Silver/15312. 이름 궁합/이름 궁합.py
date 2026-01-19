alphabet = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a = input()
b = input()

numbers = []

for i in range(len(a)):
    numbers.append(alphabet[ord(a[i])-ord('A')])
    numbers.append(alphabet[ord(b[i])-ord('A')])

for i in range(len(a) + len(b) -2):
    temp = []
    for j in range(len(numbers)-1):
        temp.append((numbers[j] + numbers[j+1]) % 10)
    numbers = temp

print("".join(map(str,numbers)))