"""Implements the Model from MVC, aka. loading and handling the data"""
import os
from typing import Dict, List
import pickle
from logger import logger
from notebook import Notebook


class NoteModel:
    """Implements the Model from MVC, aka. loading and handling the data"""
    def __init__(self):
        if not os.path.exists("Notebooks"):
            os.makedirs("Notebooks")
        self.notebooks: Dict[str, Notebook] = {}
        self.current_notebook: str = None

    def new_notebook(self, name: str) -> None:
        """
        Creates a new notebook and saves it a dictionary
        :param name: The name (and at the moment the id) of the notebook
        :raises Exception: Raises an exception if one tries to create a notebook with an
            name that already exists
        """
        logger.info("Creating notebook %s", name)
        notebook = Notebook(name)
        if name in self.notebooks:
            raise Exception("A note which the given name already exists")
        self.notebooks[name] = notebook
        logger.info("Created notebook %s", name)

    def save_notebook(self, name: str) -> None:
        """
        Saves a notebook to the disk
        :param name: The name of the notebook which should be saved 
        """
        logger.info("Saving %s", name)
        filename = "Notebooks/" + name
        outfile = open(filename, 'wb')
        pickle.dump(self.notebooks[name], outfile)
        outfile.close()
        logger.info(" Saved %s", name)

    def load_notebooks(self) -> None:
        """
        Load all notebooks in the Notebooks/ directory into self.notebooks
        """
        filenames = os.listdir("Notebooks/")
        # filenames = [filename for filename in filenames if filename.endswith(".db")]
        if not filenames:
            pass  # TODO Error hinzufuegen damit man asugeben kann das keine Notebooks vorhanden sind
        for name in filenames:
            logger.info(("Loading %s", name))
            filename = "Notebooks/" + name
            infile = open(filename, 'rb')
            notebook = pickle.load(infile)
            self.notebooks[notebook.name] = notebook
            logger.info("Finished loading %s", name)

    def save_all_notebooks(self) -> None:
        """
        Saves all notebooks in self.notebooks to the disk
        """
        logger.info("Saving off all notebooks started")
        logger.info("%s to save", str(len(self.notebooks)))
        for notebook_name in self.notebooks:
            logger.info(" Saving %s", notebook_name)
            self.current_notebook = self.notebooks[notebook_name]
            self.save_notebook(notebook_name)
        logger.info("Saving off all notebooks finished")

    def list_all_notebooks(self) -> List[str]:
        """
        Creates a list of all names(ids) of all the notebooks in self.notebooks
        :return: A list of all notebook names
        """
        names = []
        for name in self.notebooks:
            names.append(name)
        if names:
            return names
        return ["There are no notebooks"]

    def list_all_notes(self) -> List[str]:
        """
        Creates a list of all the notes in the current notebook
        :return: A list of all the note in currently open notebook
        """
        if self.current_notebook is None:
            raise Exception("self.current must not be none")
        names = []
        for name in self.notebooks[self.current_notebook].notes:
            names.append(name)
        if names:
            return names
        return ["There are no notes"]

    def add_note(self, note_name, note_text) -> None:
        """
        Adds a note the current notebook
        :param note_name: The name of the note which should be added
        :param note_text: The text of the note which should be added
        :raises Exception: Raises an exception if the self.current_notebook is none
            which means that the user didn't open a notebook and the application doesn't
            know to which notebook the note should be added
        """
        if self.current_notebook is None:
            raise Exception("self.current must not be none")

        logger.info("Making new note in %s with name %s", self.current_notebook, note_name)
        self.notebooks[self.current_notebook].add_note(note_name, note_text)

    def get_note_text(self, note_name) -> None:
        """
        Gets the text of the note as a string
        :param note_name: The name of the note from which to get the text 
        :raises Exception: If there isn't an open notebook, one can not get the text from a note
        """
        if self.current_notebook is None:
            raise Exception("self.current must not be none")

        return self.notebooks[self.current_notebook].get_note_text(note_name)




