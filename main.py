"""Module from which the program gets started"""
from note_controller import NoteController
from note_model import NoteModel
from note_console_view import NoteConsoleView
import logger

if __name__ == "__main__":
    MODEL = NoteModel()
    VIEW = NoteConsoleView(MODEL)
    CONTROLLER = NoteController(model=MODEL, view=VIEW)
    VIEW.run()
    VIEW.subject_state = VIEW.State.SAVE_ALL
    logger.fh.close()

