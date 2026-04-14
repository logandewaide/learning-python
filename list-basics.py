basicList = [1, 10, 0, 3]
print(basicList)

# len
print(f"length = {len(basicList)}")

# get values
print(basicList[1])
print(basicList[-3])
print(basicList[:3])

# in
print("in: ")
if 1 in basicList:
    print("1 is in basicList")

# replace
print("replace")
basicList[1:3] = [5, 5, 5, 5]
print(basicList)

basicList[1:5] = [2]
print(basicList)

# insert single items
print("insert single: ")
basicList.insert(1, 8)
print(basicList)

# insert multiple items
print("insert multiple: ")
basicList[1:1] = [0, 0, 0, 0]
print(basicList)

# append
print("append: ")
basicList.append(3)
print(basicList)

# extend
print("extend: ")
addList = [-1, -2]
basicList.extend(addList)
print(basicList)

# remove
print("remove: ")
basicList.remove(0)
print(basicList)
basicList.remove(0)
print(basicList)

# pop
print("pop: ")
basicList.pop(1)
print(basicList)
basicList.pop()
print(basicList)

#del and clear
del basicList[-1]
print(basicList)
basicList.clear()
print(basicList)
del basicList