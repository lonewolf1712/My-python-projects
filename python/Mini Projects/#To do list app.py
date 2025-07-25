#To do list app

def view_task():
    print(To_do_list)

def task_completed():
    
def delete_task():
    To_do_list.pop(int(input('Enter the task which you want to delete: ')))

To_do_list=[]
Task=To_do_list[]
while True:
    print('Welcome to your To-Do List!')
    print('1. Add task')
    print('2. View tasks')
    print('3. Mark task as complete')
    print('4. Delete task')
    print('5. Exit')

    try:
        choice=input('Enter you choice: ')

        if choice==1:
            print('Do you want to priortise your new task?(yes/no)\n').strip().lower()
            answer=input()
            if answer=='yes':
                Task.insert(int(input('Write your priority in numbers: ')),input('Enter task: '))
            else:
                Task.append(input('Enter task: '))
            print('Task added succesfully.')
        elif choice==2:
            print(To_do_list)
        elif choice==3:
            task_completed()
            print('Task marked succesfully.')
        elif choice==4:
            delete_task()
            print('Task deleted succefully.')
        elif choice==5:
            print('Thank you for  using this code.')
            break
        else:
            print('Invalid optipn choose between 1-5.')
    except ValueError:
        print('Invalid value enter valid number.')
