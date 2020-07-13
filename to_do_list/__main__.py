from sql_manager import SQLManager
from console import Console
from to_do_list_app import ToDoApp

db_manager = SQLManager('todo.db')
i_o_device = Console()
to_do_app = ToDoApp(db_manager, i_o_device)
to_do_app.run()