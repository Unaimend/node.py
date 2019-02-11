"""Module from which the program gets started"""
from note_controller import NoteController
from note_model import NoteModel
from note_console_view import NoteConsoleView
import logger
# from PySide2 import QtWidgets
# from qt_view import QtView
import sys
if __name__ == "__main__":
    MODEL = NoteModel()
   # app = QtWidgets.QApplication(sys.argv)
    VIEW = NoteConsoleView(model=MODEL)
    #VIEW.setMinimumSize(800, 800)
    CONTROLLER = NoteController(model=MODEL, view=VIEW)
    VIEW.run()
    # VIEW.subject_state = VIEW.State.SAVE_ALL, ""
    logger.fh.close()
   # sys.exit(app.exec_())


