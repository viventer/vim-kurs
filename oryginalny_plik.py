class Task:
    def __init__(self, task_name, due_date):
        self.task_name = task_name
        self.due_date = due_date

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task_name, due_date):
        task = Task(task_name, due_date)
        self.tasks.append(task)
    
    def remove_task(self, task_name):
        task_exists = False
        for task in self.tasks:
            if task.task_name == task_name:
                self.tasks.remove(task)
                task_exists = True
                print("Zadanie o nazwie:", task_name, "zostało usunięte")
                break
        if not task_exists:
            print("Nie można odnaleźć zadania o nazwie:", task_name)
    
    def display_tasks(self):
        if not self.tasks:
            print("Brak zadań.")
        else:
            print("Lista zadań:")
            for task in self.tasks:
                print(task.task_name, "| termin:", task.due_date)
    
    def change_due_date(self, task_name, new_due_date):
        task_exists = False
        for task in self.tasks:
            if task.task_name == task_name:
                task.due_date = new_due_date
                task_exists = True
                print("Termin zadania:", task_name, "został zmieniony na:", new_due_date)
                break
        if not task_exists:
            print("Nie można odnaleźć zadania o nazwie:", task_name)

def print_menu():
    print("======= Task Manager =======")
    print("1. Wyświetl zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zmień termin zadania")
    print("5. Wyjście")
    print("============================")

task_manager = TaskManager()

while True:
    print_menu()
    choice = input("Wybierz opcję: ")

    if choice == "1":
        task_manager.display_tasks()
    elif choice == "2":
        task_name = input("Podaj nazwę zadania: ")
        due_date = input("Podaj termin wykonania (DD.MM.RRRR): ")
        task_manager.add_task(task_name, due_date)
        print("Zadanie zostało dodane.")
    elif choice == "3":
        task_name = input("Podaj nazwę zadania do usunięcia: ")
        task_manager.remove_task(task_name)
    elif choice == "4":
        task_name = input("Podaj nazwę zadania do zmodyfikowania: ")
        new_due_date = input("Podaj nowy termin do wykonania zadania: ")
        task_manager.change_due_date(task_name, new_due_date)
    elif choice == "5":
        print("Zamykanie programu...")
        break
    else:
        print("Nieprawidłowa opcja. Spróbuj ponownie.")