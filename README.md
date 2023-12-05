Link to the tested site: "https://selenium1py.pythonanywhere.com".

There are some UI tests using POM pattern.

Version of Python : 3.11.5

To run this mini-project you have to create virtual environment and install all requirements from the
file "requirements.txt". You can do it by the command :

python3 -m venv <venv> to create virtual environment, where <venv> is name of your virtual environment;

source <venv>/bin/activate to activate your virtual environment;

pip3 install -r requirements.txt to install requirenments.

I use webdriver-manger from pip3, so you don't need to set a path to your WebDriver.

You can choose browser (Chrome/Firefox) for running tests by the command:

--browser="chrome" or --browser="firefox"

You can choose locale of the site when tests will be run by command:

--language="uk" or -language="es" etc. All languages you can find on site.

Example:
pytest --browser="firefox" --language="uk" test_main_page.py
