""""""
from note_console_view import NoteConsoleView
from note_model import NoteModel
from observer import Observer
from logger import logger
class NoteController(Observer):
    """
    Implements the controller from MVC-Pattern
    :param model: The model from mvc
    :param view:  The view from mvc
    """
    def __init__(self, model: NoteModel, view: NoteConsoleView):
        self.model = model
        self.view = view
        self.view.attach(self)

    def new_notebook(self, name) -> None:
        self.model.new_notebook(name)

    def save_notebook(self, name) -> None:
        self.model.save_notebook(name)

    def load_notebook(self, name):
        self.model.load_notebook(name)

    def add_note(self, notebook_name, note_name,text):
        self.model.add_note(notebook_name, note_name, text)

    def save_all_notebooks(self):
        logger.info("Saving all notebooks")
        self.model.save_all_notebooks()

    def update(self, arg):
        logger.info("arg: " + str(arg) + " Length: " + str(len(arg)))

        state = arg[0]

        logger.info("State: "  + str(state))
        if state == self.view.State.NEW_NOTEBOOK:
            logger.info("Making new notebook" + arg[1])
            self.new_notebook(name=arg[1])
        elif state == self.view.State.SAVE:
            self.save_notebook(name=arg[1])
        elif state == self.view.State.OPEN:
            self.model.current_notebook = arg[1]
        elif state == self.view.State.ADD:
            logger.info("Adding new note with name " + arg[1] + " and text " + arg[2])
            self.model.add_note(arg[1], arg[2])
        elif state == self.view.State.SAVE_ALL:
            self.save_all_notebooks()
            self.exit()

    def exit(self):
        exit(0)

