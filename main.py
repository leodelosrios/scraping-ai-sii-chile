import os
import time

import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()
API_KEY = os.getenv("API_KEY")
GEMINI_MODEL = "gemini-2.0-flash"

TIME_WAITING_IMG = 1
TIME_END_SESSION = 2
URL_SII = "https://zeus.sii.cl/cvc/stc/stc.html"

rut = ""
dv = ""


def load_driver():
    service = Service(ChromeDriverManager().install())

    chrome_options = Options()
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    )

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(URL_SII)

    return driver


def put_rut_input(driver):
    flag = True

    while flag:
        try:
            rut_input = driver.find_element(By.ID, "RUT")
            rut_input.send_keys(rut)
            flag = False
        except Exception:
            driver.refresh()


def put_dv_input(driver):
    flag = True

    while flag:
        try:
            rut_input = driver.find_element(By.ID, "DV")
            rut_input.send_keys(dv)
            flag = False
        except Exception:
            driver.refresh()


def put_captcha_input(driver, captcha_text):
    flag = True

    while flag:
        try:
            captcha_input = driver.find_element(By.ID, "txt_code")
            captcha_input.send_keys(captcha_text)
            flag = False
        except Exception:
            driver.refresh()


def submit_form(driver):
    flag = True

    while flag:
        try:
            submit_button = driver.find_element(By.NAME, "ACEPTAR")
            submit_button.click()
            flag = False
        except Exception:
            driver.refresh()


def get_captcha(driver):
    flag = True

    while flag:
        try:
            captcha_image_element = driver.find_element(By.ID, "imgcapt")
            flag = False
        except Exception:
            driver.refresh()

    time.sleep(TIME_WAITING_IMG)

    captcha_image_element.screenshot("captcha.png")
    img = Image.open("captcha.png")
    return img


def get_num_captcha(img):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel()

    response = model.generate_content(
        [
            img,
            "\n\n",
            "Dime exactamente cuáles son los 4 números que aparece en la imagen, sin darme formato, únicamente quiero el número.",
        ]
    )

    captcha_text = response.text.strip()
    print("Captcha: ", captcha_text)

    return captcha_text


def get_alert(driver):
    try:
        return driver.switch_to.alert
    except NoAlertPresentException:
        return None


# Bucle para que se obtengan los datos del RUT correcto
def rut_is_correct(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, "font.texto")

        driver.refresh()
        rut_is_correct(driver)
    except Exception:
        return True


def form_is_correct(driver):
    max_attempts = 5  # Número de intentos máximos para resolver el captcha
    attempts = 0
    alert = None

    while attempts < max_attempts:
        if alert == None:
            put_rut_input(driver)
            put_dv_input(driver)

        img = get_captcha(driver)
        captcha_text = get_num_captcha(img)

        put_captcha_input(driver, captcha_text)
        submit_form(driver)
        alert = get_alert(driver)

        if alert:
            alert_text = alert.text
            if "RUT incorrecto" in alert_text:
                print("RUT incorrecto")
                break
            alert.accept()
            attempts += 1
        elif rut_is_correct(driver):
            return True

    return False


if __name__ == "__main__":
    rut = input("Ingrese el RUT: ")
    dv = input("Ingrese el DV: ")

    driver = load_driver()

    if form_is_correct(driver):
        print("Continuar con el Scraping...")
    else:
        print("No se pudo completar el formulario.")

    time.sleep(TIME_END_SESSION)
    driver.quit()
