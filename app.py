from database.db import Database
from ui.register import register_screen
from ui.login import login_screen
from ui.tasks import tasks_screen
from ui.main_screen import main_screen

def main():
    db = Database()
    db.create_db()
    main_screen(db)

if __name__ == "__main__":
    main()