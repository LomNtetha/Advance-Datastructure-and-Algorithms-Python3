def swapPosition(List,pos1,pos2):
     
     List[pos1], List[pos2] = List[pos2], List[pos1]
     return List
     
List = [23, 65, 19, 90]
pos1=1
pos2=3
     
print(swapPosition(List,pos1-1, pos2-1))


def reverse(List):
     List.sort(reverse=True)
     return List

List = [4, 5, 6, 7, 8, 9]
print(reverse(List))


def countnumber(lst, x):

    count = 0
    for element in lst:
        if element == x:
            count += 1
    return count

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10

print('{} has occurred {} times'.format(x, countnumber(lst, x)))

