#todo class
class ToDo:
    #main task list initialization
    def __init__(self):
        self.tasks = []

    def new_task(self,task):
        '''
        Adds new task to the list
        param task: task to be added
        '''
        self.tasks.append(task)
        print("Task added sucessfully")
        print("")

    def del_task(self,task_index):
        '''
        Deletes task from the list by index
        param task_index: index of task to be deleted
        '''
        self.tasks.pop(task_index - 1)
        print("Task deleted successfully")
        print("")


    def mrk_task(self,task_index):
        '''
        Marks task from the list as completed by index
        param task_index: index of task to be marked as completed
        '''
        task = self.tasks[task_index - 1]
        self.tasks[task_index - 1] = task + ' - completed'
        print("Yey ! task completed")
        print("")

        #prints tasks
    def prt_task(self):
        for task in self.tasks:
            index = self.tasks.index(task) + 1
            print("{}.{}".format(index,task))
        print(" ")

#main method
def main():
    todo  = ToDo()
    choice = 1
    while True:
        choice = int(input("Select option \n 1. Add new task \n 2. Delete task \n 3. Mark task as completed \n 4. Print tasks\n 5. Exit \nEnter Number : "))
        if(choice == 1):
            task = input("Enter new task : ")
            todo.new_task(task)
        elif(choice == 2):
            task_index = int(input("Enter task index to delete(get it via printing tasks) : "))
            todo.del_task(task_index)
        elif(choice == 3):
            task_index = int(input("Enter task index to mark completed (get it via printing tasks) : "))
            todo.mrk_task(task_index)
        elif(choice == 4):
            todo.prt_task()
        elif(choice == 5):
            exit(0) #exit condition
        else:
            print("Wrong choice !")

if __name__ == '__main__':
    main()