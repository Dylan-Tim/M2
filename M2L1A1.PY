MYlist = ['Apple' ,'Guava' ,'cheese' ,'football', 'gloves']

print("Length of List:", len(MYlist))
print("First Element:", MYlist[0])
print("Last Element:", MYlist[-1])

MYlist.append('glasses')
print("Updated List :", MYlist)

MYlist.remove('cheese')
print("Updated List :", MYlist)

MYlist.sort()
print("Sorted List :", MYlist)

MYlist.pop(1)
print("Updated List :", MYlist)

MYlist.reverse()
print("Reversed List :", MYlist)

print("Multiplication on List :", MYlist*2)

MYlist = MYlist[:4]
print("Sliced List :", MYlist)

MYlist.clear()
print("Updated List :", MYlist)
