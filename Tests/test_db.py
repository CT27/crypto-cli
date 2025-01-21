from models import session, User
from sqlalchemy.exc import IntegrityError

def test_database():
    existing_user = session.query(User).filter_by(username="testuser").first()
    if not existing_user:
        new_user = User(username="testuser")
        session.merge(new_user)
        try:
            session.commit()
            print(f"User added with ID: {new_user.id}")
        except IntegrityError:
            session.rollback()
            print("User already exists.")
    else:
        print("User already exists in the database.")

if __name__ == "__main__":
    test_database()
