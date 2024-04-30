# seleniun login linkedin

This is a simple example of how to use Selenium with Python to login linkedin.

## Requirements

* Python 3.6+
* [Selenium Python Bindings](https://selenium-python.readthedocs.io/)
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## How can i use?

You need create a ".env" file with the following variables:

```bash
WEB_USERNAME=your_username
WEB_PASSWORD=your_password
```

Because the ".env" file contains sensitive information, it is ignored by Git.

In this project don't is necessary to download the ChromeDriver, because it is use the [webdriver-manager](https://pypi.org/project/webdriver-manager/) to download the ChromeDriver automatically.

But I recommend you use a virtual environment to install the dependencies.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

After that, you can run the script:

```bash
python3 main.py
```
