class Console:
    # noinspection PyMethodMayBeStatic
    def display_string(self, text=''):
        print(text)

    # noinspection PyMethodMayBeStatic
    def get_input(self, message=''):
        if len(message) != 0:
            print(message)
        return input()

    def display_tasks(self, tasks):
        date_string_format = '%e %b'
        if len(tasks) != 0:
            task_count = 1
            for task, deadline in tasks.items():
                deadline = deadline.strftime(date_string_format)
                self.display_string(f'{task_count}. {task}. {deadline}')
                task_count += 1
            return True
        else:
            return False

    def display_all_tasks(self, tasks):
        self.display_string('All tasks:')
        if self.display_tasks(tasks):
            self.display_string()
        else:
            self.display_string('Nothing to do!\n')

    def display_missed_tasks(self, tasks):
        self.display_string('Missed tasks:')
        if self.display_tasks(tasks):
            self.display_string()
        else:
            self.display_string('Nothing is missed!\n')

    def display_date(self, date):
        date_string_format = '%A %e %b:'
        date = date.strftime(date_string_format)
        self.display_string(date)

    def display_date_tasks(self, date, tasks):
        self.display_date(date)
        if len(tasks) != 0:
            task_count = 1
            for task in tasks.keys():
                self.display_string(f'{task_count}. {task}')
                task_count += 1
            else:
                self.display_string()
        else:
            self.display_string('Nothing to do!\n')

    def display_tasks_to_delete(self, tasks):
        if not self.display_tasks(tasks):
            self.display_string('Nothing is to delete!\n')
