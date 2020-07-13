from datetime import datetime, timedelta


class ToDoApp:
    def __init__(self, db_manager, i_o_device):
        self.db_manager = db_manager
        self.i_o_device = i_o_device
        self.menu = """\
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit"""

    def run(self):
        is_running = True
        while is_running:
            self.i_o_device.display_string(self.menu)
            command = int(input())
            self.i_o_device.display_string()
            if command == 0:
                is_running = False
            elif command == 1:
                self.show_tasks_for_date(datetime.today().date())
            elif command == 2:
                self.show_tasks_for_week(datetime.today().date())
            elif command == 3:
                self.show_all_tasks()
            elif command == 4:
                self.show_missed_tasks()
            elif command == 5:
                self.add_task()
            elif command == 6:
                self.delete_task()
        else:
            print('Bye!')

    def add_task(self):
        description = self.i_o_device.get_input('Enter task')
        deadline = self.i_o_device.get_input('Enter deadline')
        deadline = deadline.split('-')
        deadline = [int(data_component) for data_component in deadline]
        deadline = datetime(*deadline)
        self.db_manager.add_task(description, deadline)
        self.i_o_device.display_string('The task has been added!')
        self.i_o_device.display_string()

    def show_tasks_for_date(self, date):
        tasks = self.db_manager.get_tasks_for_deadline(date)
        self.i_o_device.display_date_tasks(date, tasks)

    def show_tasks_for_week(self, date):
        first_day = date
        for day in range(7):
            self.show_tasks_for_date(first_day + timedelta(days=day))

    def show_all_tasks(self):
        tasks = self.db_manager.get_all_tasks()
        self.i_o_device.display_all_tasks(tasks)

    def show_missed_tasks(self):
        tasks = self.db_manager.get_missed_tasks()
        self.i_o_device.display_missed_tasks(tasks)

    def delete_task(self):
        tasks = self.db_manager.get_all_tasks()
        if len(tasks) != 0:
            self.i_o_device.display_string('Chose the number of the task you want to delete:')
            self.i_o_device.display_tasks(tasks)
            task_number = int(self.i_o_device.get_input())
            tasks = list(tasks.keys())
            self.db_manager.delete_task(tasks[task_number - 1])
            self.i_o_device.display_string('The task has been deleted!\n')
        else:
            self.i_o_device.display_string('Nothing to delete!\n')


