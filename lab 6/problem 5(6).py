"""lst=[(),(),("manav")]
for i in range(len(lst)):
    if isinstance(lst[i],tuple):
        if lst[i]==():
            del(lst[i])
            break

print(lst)"""

lst = [(), (), ("manav")]
lst = [x for x in lst if x != ()]  # Keep only non-empty tuples

print(lst)