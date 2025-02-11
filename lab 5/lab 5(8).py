import collections
queue=[]

while True:
    print("\n menu")
    print("1. append")
    print("2. pop")
    
    q=input("enter a choice here:")
    
    if q=='1':
        item=input("enter number here:")
        queue.append(item)
        print(f"{item} is append")
        print(queue)
        
    elif q=='2':
        if len(queue)>0:
            remove=queue.pop(0)   #here pop(0) is nothing but remove fisrt item of the list we are append
            print(f"{remove} is pop")  # we not use pop(0) its look like stack
            print(queue)
        else:
            print(f"queue is empty")
            print(queue)
        
            
        