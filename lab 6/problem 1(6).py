bg=["meena","heer","riya",("manav",)]
boys=0
girls=0
for name in bg:
    if isinstance(name,tuple):
        boys+=1
    else:
        girls+=1
        
print("boys :",boys)
print("girls :",girls)
