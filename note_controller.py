""""""
from note_console_view import NoteConsoleView
from note_model import NoteModel

class NoteController:
    """
    Implements the controller from MVC-Pattern
    :param model: The model from mvc
    :param view:  The view from mvc
    """
    def __init__(self, model: NoteModel, view: NoteConsoleView):
        self.model = model
        self.view = view
        self.view.add_observer(self)

    def new_notebook(self, name) -> None:
        self.model.new_notebook(name)

    def save_notebook(self, name) -> None:
        self.model.save_notebook(name)

    def load_notebook(self, name):
        self.model.load_notebook(name)

    def add_note(self, notebook_name, note_name,text):
        self.model.add_note(notebook_name, note_name, text)

    def exit(self):
        exit(0)

