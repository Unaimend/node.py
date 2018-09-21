"""
Module which implements the controller from the MCV-Pattern
"""
from typing import List
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
        Observer.__init__(self)
        self.model = model
        self.load_notebooks()
        self.view = view
        self.view.attach(self)

    def new_notebook(self, notebook_name) -> None:
        """See self.model.new_notebook for documentation"""
        self.model.new_notebook(notebook_name)

    def save_notebook(self) -> None:
        """See self.model.save_notebook for documentation"""
        self.model.save_notebook()

    def load_notebooks(self) -> None:
        """See self.model.load_notebook for documentation"""
        self.model.load_notebooks()

    def add_note(self, note_name, text) -> None:
        """See self.model.add_note for documentation"""
        try:
            self.model.add_note(note_name, text)
        except KeyError:
            raise KeyError


    def save_all_notebooks(self) -> None:
        """See self.model.save_all_notebooks for documentation"""
        logger.info("Saving all notebooks")
        self.model.save_all_notebooks()

    def update(self, arg) -> None:
        # pylint: disable=R0201
        # There is self use in this function e.g. every state comparision
        """
        Function which gets called from observed objects
        :param arg: Arguments which the observed class wants to be transmitted
        """
        logger.info("arg: %s Length: %s ", str(arg), str(len(arg)))

        state = arg[0]

        logger.info("State: %s", str(state))
        if state == self.view.State.NEW_NOTEBOOK:
            logger.info("Making new notebook %s", arg[1])
            self.new_notebook(notebook_name=arg[1])
        elif state == self.view.State.SAVE:
            self.save_notebook()
        elif state == self.view.State.OPEN:
            if arg[1] in self.model.notebooks:
                self.model.current_notebook = arg[1]
            else:
                raise KeyError
        elif state == self.view.State.ADD:
            logger.info("Adding new note with name " + arg[1] + " and text " + arg[2])
            self.add_note(arg[1], arg[2])
        elif state == self.view.State.SAVE_ALL:
            self.save_all_notebooks()
            NoteController.exit()

    @staticmethod
    def exit():
        """Closes the application"""
        exit(0)
