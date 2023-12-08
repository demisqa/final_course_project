## *Description:* 
There is a mini-project with some UI tests using POM pattern.
Link to the tested site: "https://selenium1py.pythonanywhere.com".

____
### Technologies: 
Python 3.11.5
Pytest 7.4.3
Selenium 4.15.2
Webdriver Manager 4.0.1
python-dotenv 1.0.0


____
### How to run:

To run this mini-project you have to create virtual environment and install all requirements from the
file "requirements.txt". You can do it by the commands:

```
python3 -m venv <venv>
``` to create virtual environment, where <venv> is name of your virtual environment;

```
source <venv>/bin/activate
``` to activate your virtual environment;

```
pip3 install -r requirements.txt
```  to install requirements.

I use webdriver-manger from pip3, so you don't need to set a path to your WebDriver.

You can choose browser (Chrome/Firefox) for running tests by the command:

```
--browser_name=chrome
```

```
--browser_name=firefox
```

You can choose locale of the site, where tests will be run by the command:

```
--language="uk"
``` 
or
``` 
--language="es"
``` etc. 
All languages you can find on site.

Example:

```
pytest --browser=firefox --language="uk" test_main_page.py
```

Commands --browser_name and --language have default values "chrome" and "en", in case when you skipped these commands.

Also, it's required to do some steps:

1. Create GitHub token on your GitHub (Settings -> Developer setting -> Personal Access Tokens -> Generate)
2. Create .env on the root of this project (do not forget to add this file to .gitignore)
3. Create GH_TOKEN=YourGitHubToken in .env file, where YourGitHubToken is a value of your token copied from GitHub

Because webdriver_manager downloading some webdrivers from their official GitHub repositories but GitHub has limitations like 60 requests per hour for unauthenticated users. In case not to face an error related to GitHub credentials, you need to create GitHub token and place it into your environment (https://pypi.org/project/webdriver-manager/)