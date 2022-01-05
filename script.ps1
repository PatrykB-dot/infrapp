cd 'C:\nowy python\infraapp\'
venv\Scripts\activate
$env:FLASK_APP = "infrapp.py"
$env:FLASK_ENV = "development"
flask run