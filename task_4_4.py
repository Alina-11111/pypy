#for
numb = [1, 2, 3, 4, 5]
new_numb = []
for i in range(1, len(numb)):
    new_numb.append(numb[i])
if len(new_numb) > 0:
    new_numb.append(numb[0])
print(new_numb)

#while
numb = [1, 2, 3, 4, 5]
new_numb = []
i = 1
while i <len(numb):
    new_numb.append(numb[i])
    i +=1
if len(new_numb) > 0:
    new_numb.append(numb[0])
print(new_numb)