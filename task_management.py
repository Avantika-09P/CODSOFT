def task():
    tasks=[]
    print("------------Welcome to task management app!!------------------")
    total_task=int(input("Enter how many tasks you want to add: "))
    for i in range(1,total_task+1):
        task_name=input("Enter task name: ")
        tasks.append(task_name)

    print(f"Today's tasks are: \n {tasks}")
    while True:
        print("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Stop: ")
        operation=int(input("1/2/3/4/5: "))
        if operation==1 :
            add=input("enter task you want to add:")
            tasks.append(add)
            print(f"{add} : task is added successfully !!")
        elif operation==2:
            updated_val=input("enter the task name you want to update: ")
            if updated_val in tasks:
                up=input("Enter new task: ")
                ind=tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task is : {up}")
        elif operation==3:
            delete_val=input("enter which task you want to delet: ")
            if delete_val in tasks:
                ind=tasks.index(delete_val)
                del tasks[ind]
                print(f"{delete_val}: Task has been deleted!!")
        elif operation==4:
            print(f"Total tasks = {tasks}")
        elif operation==5:
            print("Closing the program....")
            break
        else:
            print("Invalid input!!")

task()

