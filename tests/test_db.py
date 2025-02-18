from sqlalchemy import select

from src.fast_zero.models import User


def test_create_user(session):
    user = User(
        username="John Doe", email="john@john.com", password="password"
    )
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == "john@john.com"))

    assert result.username == "John Doe"
