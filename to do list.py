todo_list=[]
print("welcome!!!")
print("press 1, if u want to see your todo list,press 2, if u want to add into your todo list and press 3, if u want to remove something to from your todo list")
input=input()
if input=="1":
    print("your todo list is",todo_list)
elif input=="2":
    response=input("please add what you want to add to your todo list")
    todo_list.append(response)
    print("your new list is:", todo_list)
elif input=="3":
    response2=input("what do you want to remove")
    todo_list.remove(response2)
    print("your new list is:",todo_list)
else:
    print("error, please try again")
    

    