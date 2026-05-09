#for
dict1 = {'test':'test_value', 'europe':'eur','dolar':'usd', 'ruble':'rub'}
new_dict = {} 
for k, val in dict1.items():
    new_k = k + str(len(k))
    new_dict [new_k] = val
 
print (new_dict)
 
#while
dict1 = {'test':'test_value', 'europe':'eur','dolar':'usd', 'ruble':'rub'}
new_dict = {}
keys = list(dict1.keys())
i = 0
while i < len(keys):
    key = keys[i]
    new_k = key + str(len(key))
    new_dict[new_k]=dict1[key]
    i+=1
print (new_dict)