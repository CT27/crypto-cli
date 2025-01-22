from models import session, User
from sqlalchemy.exc import IntegrityError

def add_user(username):
    """Add a new user to the database."""
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        print(f"Error: User '{username}' already exists.")
        return

    new_user = User(username=username)
    session.add(new_user)
    try:
        session.commit()
        print(f"User '{username}' added successfully with ID: {new_user.id}")
    except IntegrityError:
        session.rollback()
        print(f"Error: Username '{username}' already exists.")
    finally:
        session.close()

if __name__ == "__main__":
    username = input("Enter username: ").strip()
    if username:
        add_user(username)
    else:
        print("Error: Username cannot be empty.")
