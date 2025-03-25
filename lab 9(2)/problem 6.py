def senitize_list(lst, index=0):
    if index == len(lst):
        return
    
    if lst[index] < 0:
        lst[index] = 0
    
    senitize_list(lst, index + 1)

lst = [3, 2, -1, -4, 7, -9]
senitize_list(lst)
print(lst)
