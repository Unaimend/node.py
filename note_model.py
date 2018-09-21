"""Implements the Model from MVC, aka. loading and handling the data"""
import os
from typing import Dict
import pickle
from logger import logger
from notebook import Notebook
class NoteModel:
    """Implements the Model from MVC, aka. loading and handling the data"""
    def __init__(self):
        if not os.path.exists("Notebooks"):
            os.makedirs("Notebooks")
        self.notebooks: Dict[Notebook] = dict()

    def new_notebook(self, name: str):
        logger.info("New notebook " + name)
        notebook = Notebook(name)
        self.notebooks[name] = notebook

    def save_notebook(self, name):
        logger.info("Saving" + name)
        filename = "Notebooks/" + name
        outfile = open(filename, 'wb')
        pickle.dump(self.notebooks[name], outfile)
        outfile.close()
        logger.info("Saved" + name)

    def load_notebook(self, name):
        logger.info("Loading" + name)
        filename = "Notebooks/" + name
        infile = open(filename, 'rb')
        notebook = pickle.load(infile)
        self.notebooks[notebook.name] = notebook
        logger.info("Finished loading" + name)

    def add_note(self, notebook_name, note_name, note_text):
        self.notebooks[notebook_name].add_note(note_name, note_text)
    def get_note_text(self, notebook_name, note_name):
        return self.notebooks[notebook_name].notes[note_name].__repr__
    def get_notes(self, name):
        return Notebook.notes[name]


