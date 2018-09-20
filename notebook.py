"""Implements a notebook, a collection of notes"""
from typing import Dict
from note import Note

class Notebook:
    def __init__(self, name):
        self.name = name
        self.notes: Dict[Note] = {}

    def add_note(self, name: str, text: str) -> None:
        self.notes[name] = Note(name, "TEXT" + text)
    def get_note_text(self, name):
        return self.notes[name].__repr__
