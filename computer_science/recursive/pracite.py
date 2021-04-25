arr = [1,2,3,4,5,6]

def sum_list(arr):
    if arr == []:
        return 0
    return arr[0]+sum_list(arr[1:])

print(sum_list(arr))

name = "Norbert"

def spell_name(name):
    if name == "":
        return("all done")
    print(name[0])
    return spell_name(name[1:])

spell_name(name)


for letter in name:
    print(letter)
print("all done")
