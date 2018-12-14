"""Implements the View from MVC, aka. showing the data to the user"""
from enum import Enum
from observer import Subject


class NoteConsoleView(Subject):
    """Implements the View from MVC, aka. showing the data to the user"""
    class State(Enum):
        """"
        Private class to capture the state of te program,
        can be used from an observer to implement actions 
        when the state changes
        """
        NEW_NOTEBOOK = 1
        SAVE = 3
        SET_CURRENT_NOTEBOOK = 4
        SAVE_ALL = 5
        OPEN = 6
        ADD = 7
        PRINT = 8

    def __init__(self, model):
        """
        Constructor
        :param model: The model from which the view gets the data
        """
        Subject.__init__(self)
        self.model = model

    def attach(self, observer) -> None:
        """
        Adds an observer to the mdoel which listens to user input
        :param observer: The observer which should be listening 
        """
        Subject.attach(self, observer)

    @staticmethod
    def show_error(text) -> None:
        """
        Prints an error message 
        :param text: The error message you want to print 
        """
        print(text)

    @staticmethod
    def print_options() -> None:
        """
        Prints all the options you have in the program
        """
        print("What do you want to do")
        print("(1) Make new notebook")
        print("(2) Save notebook")
        print("(3) List notebooks")
        print("(4) Open notebook")
        print("(5) Add note")
        print("(6) Print note")
        print("(7) List all notes")
        print("(8) Exit")
        print("(9) Help")

    def run(self) -> None:
        """
        Starts the interactive part of the application
        """
        NoteConsoleView.print_options()
        while True:
            x = input("Please choose an option:\n")
            if x == "1":
                name: str = input("what should be the name of the new notebook:\n")
                self.subject_state = self.State.NEW_NOTEBOOK, name
            elif x == "2":
                self.subject_state = self.State.SAVE, ""
            elif x == "3":
                if not self.model.list_all_notebooks():
                    print("The notebook folder is empty")
                else:
                    for x in self.model.list_all_notebooks():
                        print(x)
            elif x == "4":
                notebook_name = input("Which notebook do you want to open:\n")
                try:
                    self.subject_state = self.State.OPEN, notebook_name
                except KeyError:
                    error = "A notebook with the name " + notebook_name + " doesn't exist"
                    NoteConsoleView.show_error(error)
            elif x == "5":
                note_name = input("Name of the note:\n")
                text = input("Text:\n")
                self.subject_state = self.State.ADD, note_name, text
            elif x == "6":
                note_name = input("Name of the note you want to print:\n")
                print(self.model.get_note_text(note_name))
            elif x == "7":
                if not self.model.list_all_notes():
                    print("This notebook contains no notes")
                else:
                    for x in self.model.list_all_notes():
                        print(x)
            elif x == "8":
                self.subject_state = self.State.SAVE_ALL, ""
            elif x == "9":
                NoteConsoleView.print_options()










