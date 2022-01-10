from app.models import User, Asset


def test_new_user():
    user = User(username="Patryk", email="patryk@test.pl")
    assert user.username == "Patryk"
    assert user.email == "patryk@test.pl"
    user.set_password("Testing Password")
    assert user.password_hash != "Testing Password"

def test_new_asset():
    asset = Asset(name='Asus', type='pc', owner='test', serial_number='12345678')
    assert asset.name == 'Asus'
    assert asset.type == 'pc'
    assert asset.owner == 'test'
    assert asset.serial_number != '09876'