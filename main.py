import os

from dotenv import load_dotenv
from loguru import logger
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
def login(user: str, password: str) -> None:

    options: webdriver = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver: webdriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

    driver.get('https://www.linkedin.com/login/pt')
    driver.find_element(By.NAME, 'session_key').send_keys(user)
    driver.find_element(By.NAME, 'session_password').send_keys(password)
    driver.find_element(By.XPATH, '//button[text()="Entrar"]').send_keys(Keys.ENTER)
    validation: webdriver = driver.find_element(By.XPATH, '//*[@id="ember14"]')
    validation.click()
def main() -> None:
    load_dotenv()
    user: str = os.getenv('WEB_USER')
    password: str = os.getenv('WEB_PASSWORD')

    logger.add("logs.log", format="{time: DD-MM-YY HH:mm:ss} | {level} | {message}",level='INFO')

    try:
        login(user, password)
        logger.info('success!')
    except:
        logger.error('email or password error!')


if '__main__' == __name__:
    main()