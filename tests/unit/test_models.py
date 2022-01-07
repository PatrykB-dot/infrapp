from app.models import User


def test_new_user():
    user = User(username="Patryk", email="patryk@test.pl")
    assert user.username == "Patryk"
    assert user.email == "patryk@test.pl"
    user.set_password("Testing Password")
    assert user.password_hash != "Testing Password"
