#Write code to find elements that are common in both lists and are greater than a given value (e.g., greater than 5).

list1 = [3, 7, 8, 3, 5, 7, 1, 9, 5, 2, 45, 66, 99]
list2 = [6, 2, 8, 6, 9, 3, 4, 8, 7, 4, 77, 11]

l3 = list1 + list2
print("Total elements in both the list : ",len(l3))                                #total elements in both the list

common =  []

for x in list1:
    if x in list2 and x not in common:
        common.append(x)

print("Common in both list : ",common)
print("Number of common elements in both the list : ",len(common))
a = sorted(common)
print(f"Sorted : {a}")

value = []
for  x in common:
    if x > 5:
        value.append(x)

print(f"Common value greater than 5 : {value}")