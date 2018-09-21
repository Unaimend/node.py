from note_controller import NoteController
from note_model import NoteModel
from note_console_view import NoteConsoleView
import logger

if __name__ == "__main__":
    print("WTF1")
    model = NoteModel()
    view = NoteConsoleView(model)
    controller = NoteController(model=model, view=view)
    print("WTF")
    view.run()

    logger.fh.close()

