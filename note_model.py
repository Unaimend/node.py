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

    def new_notebook(self, name: str):
        logger.info("New notebook " + name)
        notebook = Notebook(name)
        self.notebooks[name] = notebook

    def save_notebook(self, name):
        logger.info("Saving " + name)
        filename = "Notebooks/" + name
        outfile = open(filename, 'wb')
        pickle.dump(self.notebooks[name], outfile)
        outfile.close()
        logger.info(" Saved " + name)

    def load_notebooks(self):
        filenames = os.listdir("Notebooks/")
        # filenames = [filename for filename in filenames if filename.endswith(".db")]
        if len(filenames) == 0:
            pass  # TODO Error hinzufuegen damit man asugeben kann das keine Notebooks vorhanden sind
        for name in filenames:
            logger.info("Loading" + name)
            filename = "Notebooks/" + name
            infile = open(filename, 'rb')
            notebook = pickle.load(infile)
            self.notebooks[notebook.name] = notebook
            logger.info("Finished loading " + name)

    def save_all_notebooks(self):
        logger.info("Saving off all notebooks started")
        logger.info(str(len(self.notebooks)) + " to save")
        for notebook_name in self.notebooks:
            logger.info(" Saving " + notebook_name)
            self.save_notebook(notebook_name)
        logger.info("Saving off all notebooks finished")

    def list_all_notebooks(self) -> List[str]:
        names = []
        for name in self.notebooks:
            names.append(name)
        return names

    def add_note(self, note_name, note_text):
        logger.info("Making new note in" + self.current_notebook + "with name" + note_name )
        self.notebooks[self.current_notebook].add_note(note_name, note_text)

    def get_note_text(self, note_name):
        return self.notebooks[self.current_notebook].get_note_text(note_name)




