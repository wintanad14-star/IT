todo_list=[] 
complete=[]

def main_display():
    for x in todo_list:
        print(x)
def addd():
    z=input("enter your new task")
    main_display()
    todo_list.append(z)
    
def rem():
    u=input("what do you want to remove")
    main_display()
    todo_list.remove(u)
    print(u,"is removed from your todo list")
def ed():
    main_display()
    o= input("Enter the task you want to edit: ")
    if o in todo_list:
        n= input("Enter the edited task: ")
        i = todo_list.index(o)
        todo_list[i] = n
        print("Task updated!")
    else:
        print("Task not found!")
        
def mac():
    main_display()
    w=input("enter the task you want it to be marked as complete")
    todo_list.remove(w)
    complete.append(w)
def mac_done():
    print(complete)
    
def comp_display():
      for w in complete:
          print(w)
              
def interface():
    while True:
        print("=== TO-DO LIST ===")
        main_display()
        print("=== COMPLETED ===")
        comp_display()
        print("=== MAIN MENU ===")
        print("1. ADD NEW TASK")
        print("2. REMOVE TASK")
        print("3. EDIT TASK")
        print("4. MARK TASK AS COMPLETE")
        print("5. EXIT")
        c=int(input("enter your choice 1-5"))
        if c==1:
            addd()
        elif c==2:
            rem()
        elif c==3:
            ed()
        elif c==4:
            mac()
           
        elif c==5:
            print("exitting, until next time 🫡🫡🫡🫡")
            break
interface()
    
    
    
    

