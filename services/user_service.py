from models import session, User
from sqlalchemy.exc import IntegrityError

class UserService:

    @staticmethod
    def add_user(username):
        """
        Adds a new user to the database.

        Args:
            username (str): The username to add.

        Returns:
            str: Success or error message.
        """
        existing_user = session.query(User).filter_by(username=username).first()
        if existing_user:
            return f"[bold red]Error: User '{username}' already exists.[/bold red]"

        new_user = User(username=username)
        session.add(new_user)
        try:
            session.commit()
            return f"[bold green]User '{username}' added successfully.[/bold green]"
        except IntegrityError:
            session.rollback()
            return f"[bold red]Error: Username '{username}' already exists.[/bold red]"
        finally:
            session.close()
