# for
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = []
for i in numbers:
    new_numbers.append(i* -2)
print (*new_numbers)
 
#while
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = []
i = 0
while i < len(numbers):
    new_numbers.append(numbers[i]* -2)
    i+=1
print (*new_numbers)