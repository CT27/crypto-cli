from models import SessionLocal, User
from sqlalchemy.exc import IntegrityError
from rich.console import Console

console = Console()

class UserService:
    @staticmethod
    def add_user(username):
        """Adds a new user to the database."""
        session = SessionLocal()  # Create a fresh session

        console.print(f"DEBUG: Attempting to add user '{username}'")

        try:
            existing_user = session.query(User).filter_by(username=username).first()
            if existing_user:
                console.print(f"[bold red]Error: User '{username}' already exists.[/bold red]")
                return

            new_user = User(username=username)
            session.add(new_user)
            session.commit()  # COMMIT CHANGES
            session.refresh(new_user)  # REFRESH SESSION

            console.print(f"[bold green]User '{username}' added successfully.[/bold green]")

        except IntegrityError:
            session.rollback()
            console.print(f"[bold red]Error: Could not add user '{username}'.[/bold red]")

        finally:
            session.close()  # Close the session to prevent locks
