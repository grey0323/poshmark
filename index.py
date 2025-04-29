from seleniumwire import webdriver  # Importar Selenium Wire
from selenium.webdriver.common.by import By
import time
import random

proxy_residencial = "isp2.hydraproxy.com"
puerto = 9989
usuario = "marmkhkncd331191"
contraseñas = [

    "qduf3lbg33jkn174_country-UnitedStates_session-HsWYw6PF",
    "qduf3lbg33jkn174_country-UnitedStates_session-SZy6cJzg",
    "qduf3lbg33jkn174_country-UnitedStates_session-mpsZy28k",
    "qduf3lbg33jkn174_country-UnitedStates_session-omx2CbG6",
    "qduf3lbg33jkn174_country-UnitedStates_session-IakXoDCN",
    "qduf3lbg33jkn174_country-UnitedStates_session-oxAPt0iM",
    "qduf3lbg33jkn174_country-UnitedStates_session-PU2qRlNu",
    "qduf3lbg33jkn174_country-UnitedStates_session-eFym4rc7",
    "qduf3lbg33jkn174_country-UnitedStates_session-ddg7hrPw",
    "qduf3lbg33jkn174_country-UnitedStates_session-gKXTi6iL",
    "qduf3lbg33jkn174_country-UnitedStates_session-DdCHlPLl",
    "qduf3lbg33jkn174_country-UnitedStates_session-a0cXW173",
    "qduf3lbg33jkn174_country-UnitedStates_session-rK3XBUp9",
    "qduf3lbg33jkn174_country-UnitedStates_session-SsKfAipT",
    "qduf3lbg33jkn174_country-UnitedStates_session-NYlLgb5b",
    "qduf3lbg33jkn174_country-UnitedStates_session-pCZkqihE",
    "qduf3lbg33jkn174_country-UnitedStates_session-Ly6aVLYh",
    "qduf3lbg33jkn174_country-UnitedStates_session-N3MkLdGJ",
    "qduf3lbg33jkn174_country-UnitedStates_session-ZkTZISmQ",
    "qduf3lbg33jkn174_country-UnitedStates_session-XGb03wyd",
    "qduf3lbg33jkn174_country-UnitedStates_session-e9pHfCt9",
    "qduf3lbg33jkn174_country-UnitedStates_session-v8FKzjG1",
    "qduf3lbg33jkn174_country-UnitedStates_session-FxKs64iE",
    "qduf3lbg33jkn174_country-UnitedStates_session-PlFlw1GB",
    "qduf3lbg33jkn174_country-UnitedStates_session-kXvixLB5",
    "qduf3lbg33jkn174_country-UnitedStates_session-f5oEmc2j",
    "qduf3lbg33jkn174_country-UnitedStates_session-w2vhMzFM",
    "qduf3lbg33jkn174_country-UnitedStates_session-pxVRvwNu",
    "qduf3lbg33jkn174_country-UnitedStates_session-6xjFrfmo",
    "qduf3lbg33jkn174_country-UnitedStates_session-HYH340cM",
    "qduf3lbg33jkn174_country-UnitedStates_session-0Pb4Y3oE",
    "qduf3lbg33jkn174_country-UnitedStates_session-Ndv6kBtc",
    "qduf3lbg33jkn174_country-UnitedStates_session-AB84J5qa",
    "qduf3lbg33jkn174_country-UnitedStates_session-9XJFEeJT",
    "qduf3lbg33jkn174_country-UnitedStates_session-POuxNsn1",
    "qduf3lbg33jkn174_country-UnitedStates_session-gvQp2Nd5",
    "qduf3lbg33jkn174_country-UnitedStates_session-X3pksoqk",
    "qduf3lbg33jkn174_country-UnitedStates_session-fkfTtoFs",
    "qduf3lbg33jkn174_country-UnitedStates_session-SRDURsku",
    "qduf3lbg33jkn174_country-UnitedStates_session-o8UjTeIP",
    "qduf3lbg33jkn174_country-UnitedStates_session-O2JLyADv",
    "qduf3lbg33jkn174_country-UnitedStates_session-Bh2w4K4G",
    "qduf3lbg33jkn174_country-UnitedStates_session-va7rNCBX",
    "qduf3lbg33jkn174_country-UnitedStates_session-PTTcREpT",
    "qduf3lbg33jkn174_country-UnitedStates_session-PeJzIiMw",
    "qduf3lbg33jkn174_country-UnitedStates_session-VfJ8ZXxp",
    "qduf3lbg33jkn174_country-UnitedStates_session-zFv2fDo2",
    "qduf3lbg33jkn174_country-UnitedStates_session-2YMRrL6p",
    "qduf3lbg33jkn174_country-UnitedStates_session-lUkYM8WG",
    "qduf3lbg33jkn174_country-UnitedStates_session-xobURETn",
    "qduf3lbg33jkn174_country-UnitedStates_session-rJOfYHF4",
    "qduf3lbg33jkn174_country-UnitedStates_session-Kbv51NYc",
    "qduf3lbg33jkn174_country-UnitedStates_session-v0UNhBHl",
    "qduf3lbg33jkn174_country-UnitedStates_session-BYVIV5it",
    "qduf3lbg33jkn174_country-UnitedStates_session-uLcHkFo4",
    "qduf3lbg33jkn174_country-UnitedStates_session-o2j99hVX",
    "qduf3lbg33jkn174_country-UnitedStates_session-Z6xMM9RN",
    "qduf3lbg33jkn174_country-UnitedStates_session-FyyfoDiJ",
    "qduf3lbg33jkn174_country-UnitedStates_session-Qn33dDjG",
    "qduf3lbg33jkn174_country-UnitedStates_session-DlNsA2mC",
    "qduf3lbg33jkn174_country-UnitedStates_session-xVJl2tcv",
    "qduf3lbg33jkn174_country-UnitedStates_session-ERQyVceg",
    "qduf3lbg33jkn174_country-UnitedStates_session-DJWzfsnY",
    "qduf3lbg33jkn174_country-UnitedStates_session-CW98HFKa",
    "qduf3lbg33jkn174_country-UnitedStates_session-y3jJxEwU",
    "qduf3lbg33jkn174_country-UnitedStates_session-d2aDuwea",
    "qduf3lbg33jkn174_country-UnitedStates_session-9juZC7jK",
    "qduf3lbg33jkn174_country-UnitedStates_session-QS8j6wTG",
    "qduf3lbg33jkn174_country-UnitedStates_session-c9HFAszt",
    "qduf3lbg33jkn174_country-UnitedStates_session-YdQmLpCa",
    "qduf3lbg33jkn174_country-UnitedStates_session-jL28idzR",
    "qduf3lbg33jkn174_country-UnitedStates_session-1U94TnRq",
    "qduf3lbg33jkn174_country-UnitedStates_session-jaZ7uzFE",
    "qduf3lbg33jkn174_country-UnitedStates_session-r80P9IsK",
    "qduf3lbg33jkn174_country-UnitedStates_session-ZnOJcb65",
    "qduf3lbg33jkn174_country-UnitedStates_session-VBW9jWC3",
    "qduf3lbg33jkn174_country-UnitedStates_session-0KVpKXYs",
    "qduf3lbg33jkn174_country-UnitedStates_session-2dn4w1Op",
    "qduf3lbg33jkn174_country-UnitedStates_session-2hGbMN2g",
    "qduf3lbg33jkn174_country-UnitedStates_session-kWFXtFjY",
    "qduf3lbg33jkn174_country-UnitedStates_session-OshtLSfe",
    "qduf3lbg33jkn174_country-UnitedStates_session-BpCguKFj",
    "qduf3lbg33jkn174_country-UnitedStates_session-8EttkZhy",
    "qduf3lbg33jkn174_country-UnitedStates_session-dcIGEuTa",
    "qduf3lbg33jkn174_country-UnitedStates_session-epV6XbG4",
    "qduf3lbg33jkn174_country-UnitedStates_session-0pckDAhG",
    "qduf3lbg33jkn174_country-UnitedStates_session-89KIGMxV",
    "qduf3lbg33jkn174_country-UnitedStates_session-ChgCXESr",
    "qduf3lbg33jkn174_country-UnitedStates_session-nmEiCZ7p",
    "qduf3lbg33jkn174_country-UnitedStates_session-bLBs6kl5",
    "qduf3lbg33jkn174_country-UnitedStates_session-bMen1AEu",
    "qduf3lbg33jkn174_country-UnitedStates_session-aMXm0LcT",
    "qduf3lbg33jkn174_country-UnitedStates_session-fpo0QZsm",
    "qduf3lbg33jkn174_country-UnitedStates_session-8kf7gVe4",
    "qduf3lbg33jkn174_country-UnitedStates_session-wcAGWOH7",
    "qduf3lbg33jkn174_country-UnitedStates_session-zCpwBcq9",
    "qduf3lbg33jkn174_country-UnitedStates_session-joTXbeoC",
    "qduf3lbg33jkn174_country-UnitedStates_session-QpWUv42n",
    "qduf3lbg33jkn174_country-UnitedStates_session-QQ5Qyb0Q",
    "qduf3lbg33jkn174_country-UnitedStates_session-cxafWATm",
    "qduf3lbg33jkn174_country-UnitedStates_session-bsOyGqjB",
    "qduf3lbg33jkn174_country-UnitedStates_session-GYJWP0YF",
    "qduf3lbg33jkn174_country-UnitedStates_session-iNrvYB2I",
    "qduf3lbg33jkn174_country-UnitedStates_session-OWlh36Yb",
    "qduf3lbg33jkn174_country-UnitedStates_session-85Zuetsh",
    "qduf3lbg33jkn174_country-UnitedStates_session-bxc3ZqHI",
    "qduf3lbg33jkn174_country-UnitedStates_session-hPOFeHqu",
    "qduf3lbg33jkn174_country-UnitedStates_session-6c77n14I",
    "qduf3lbg33jkn174_country-UnitedStates_session-YLczBtz4",
    "qduf3lbg33jkn174_country-UnitedStates_session-R6XPvRKw",
    "qduf3lbg33jkn174_country-UnitedStates_session-Oud2y4Y8",
    "qduf3lbg33jkn174_country-UnitedStates_session-7xGdr0GC",
    "qduf3lbg33jkn174_country-UnitedStates_session-hklfehbn",
    "qduf3lbg33jkn174_country-UnitedStates_session-MiUtpVCg",
    "qduf3lbg33jkn174_country-UnitedStates_session-H1nkZ2FO",
    "qduf3lbg33jkn174_country-UnitedStates_session-MYN3FXrH",
    "qduf3lbg33jkn174_country-UnitedStates_session-MLUbjsSh",
    "qduf3lbg33jkn174_country-UnitedStates_session-PmZP1ikh",
    "qduf3lbg33jkn174_country-UnitedStates_session-cYF66Xui",
    "qduf3lbg33jkn174_country-UnitedStates_session-gBALAwIM",
    "qduf3lbg33jkn174_country-UnitedStates_session-1wsM4TPs",
    "qduf3lbg33jkn174_country-UnitedStates_session-X3xrmzAL",
    "qduf3lbg33jkn174_country-UnitedStates_session-9f6HDf8j",
    "qduf3lbg33jkn174_country-UnitedStates_session-5yNgxQdv",
    "qduf3lbg33jkn174_country-UnitedStates_session-1uaHg5Kf",
    "qduf3lbg33jkn174_country-UnitedStates_session-x36IwabE",
    "qduf3lbg33jkn174_country-UnitedStates_session-bGIdFLGX",
    "qduf3lbg33jkn174_country-UnitedStates_session-jt2DTUuA",
    "qduf3lbg33jkn174_country-UnitedStates_session-LtdW9KPH",
    "qduf3lbg33jkn174_country-UnitedStates_session-XJ0taqK3",
    "qduf3lbg33jkn174_country-UnitedStates_session-DfPFGUMl",
    "qduf3lbg33jkn174_country-UnitedStates_session-LgXpgKn2",
    "qduf3lbg33jkn174_country-UnitedStates_session-78S8OJv9",
    "qduf3lbg33jkn174_country-UnitedStates_session-TgP4lHrC",
    "qduf3lbg33jkn174_country-UnitedStates_session-TKichSFf",
    "qduf3lbg33jkn174_country-UnitedStates_session-L5bV5INy",
    "qduf3lbg33jkn174_country-UnitedStates_session-oGDcNWyf",
    "qduf3lbg33jkn174_country-UnitedStates_session-IFjnE2xY",
    "qduf3lbg33jkn174_country-UnitedStates_session-qdiI5C4u",
    "qduf3lbg33jkn174_country-UnitedStates_session-1dqEzVCH"
]

contraseña = proxy_aleatorio = random.choice(contraseñas)
seleniumwire_option = {
    'proxy': {
        'http': f'http://{usuario}:{contraseña}@{proxy_residencial}:{puerto}',
        'https': f'http://{usuario}:{contraseña}@{proxy_residencial}:{puerto}',
        'no_proxy': 'localhost,127.0.0.1'
    },
    
    "header_overrides": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    },
    "header_overrides": {
        "Accept-Encoding": "gzip, deflate"
    }
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-gpu")  # Desactivar GPU
chrome_options.add_argument("--blink-settings=imagesEnabled=false")  # Desactiva imágenes
chrome_options.add_argument("--disable-plugins")  # Desactivar plugins
chrome_options.add_argument("--disable-popup-blocking")  # Evitar ventanas emergentes
chrome_options.add_argument("--disable-javascript")  # Desactiva JavaScript
chrome_options.add_argument("--disable-prefetch")
chrome_options.add_argument("--disable-prerender")
chrome_options.add_argument("--disable-background-networking")
chrome_options.add_argument("--disable-client-side-redirects")
#chrome_options.page_load_strategy = "none"  # No espera la carga completa
#chrome_options.add_argument("--headless")  # Ejecutar sin interfaz gráfica



driver = webdriver.Chrome(seleniumwire_options=seleniumwire_option, options=chrome_options )

driver.get("https://poshmark.com/login?pmrd%5Burl%5D=%2F")

try:
    input_element = driver.find_element(By.ID, "login_form_username_email")  # Cambia "campo_id" por el identificador real
    # Enviar texto al campo de entrada
    input_element.send_keys("Texto de ejemplo")
    input_element = driver.find_element(By.ID, "login_form_password")  # Cambia "campo_id" por el identificador real
    # Enviar texto al campo de entrada
    input_element.send_keys("Texto de ejemplo")
    driver.execute_script('document.querySelector("#email-login-form > form > div.form__actions.br--none.p--t--0.jc--sb.fw--w > button").click()')
    time.sleep(2)
    div_element = driver.find_element(By.CLASS_NAME, "error_banner")  # Reemplaza "mi_div" con el ID real
    texto = div_element.text
    if texto == "Invalid Username or Password":
        print("NO FUCIONA")
    else:
        print("Hay probabilidades de que entre")
except:
    print("PY ERROR")

time.sleep(900)