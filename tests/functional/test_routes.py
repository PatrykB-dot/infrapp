from app import create_app

flask_app = create_app()

def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"This is infraapp" in response.data
        assert b"This is not infraapp" not in response.data

#def login(client, username, password):
#    return client.post('/login', data=dict(
#        username=username,
#        password=password
#    ), follow_redirects=True)