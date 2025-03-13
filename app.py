import database.db as db

def main():
    pass

if __name__ == "__main__":
    db.create_db()
    db.add_user('Anderson s.', '1234')
    db.autenticate_user('Anderson S.', '1234')
    main()

