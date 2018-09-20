"""Implements the View from MVC, aka. showing the data to the user"""

class NoteConsoleView:
    """Implements the View from MVC, aka. showing the data to the user"""
    def __init__(self, model):
        """
        Constructor
        :param model: The model from which the view gets the data
        """
        self.model = model
        self.observer = None

    def add_observer(self, observer) -> None:
        """
        Adds an observer to the mdoel which listens to user input
        :param observer: The observer which should be listening 
        """
        self.observer = observer

    def run(self) -> None:
        """
        Starts the interactive part of the application
        """
        print("What do you want to do")
        print("(1) Make new notebook")
        print("(2) Save notebook")
        print("(3) Load notebook")
        print("(4) print note")
        print("(5) add note")
        print("(6) Exit")


        while True:
            x = input("Please choose an option:\n")
            if x == "1":
                name: str = input("what should be the name of the new notebook:\n")
                self.observer.new_notebook(name)
            elif x == "2":
                name: str = input("Which notebook do you want to save:\n")
                self.observer.save_notebook(name)
            elif x == "3":
                name: str = input("Which notebook do you want to load:\n")
                self.observer.load_notebook(name)
            elif x == "4":
                notebook_name: str = input("From which notebook do you want to print:\n")
                note_name: str = input("which note do you want to print:\n")
                self.model.print_note(notebook_name, note_name)
            elif x == "5":
                notebook_name: str = input("Name of te Notebook:\n")
                note_name: str = input("Name of the note:\n")
                text: str = input("TEXT:\n")
                self.observer.add_note(notebook_name, note_name,text)
            elif x == "6":
                self.observer.exit()





