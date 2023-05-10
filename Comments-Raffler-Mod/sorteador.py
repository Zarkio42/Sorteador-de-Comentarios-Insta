from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
import random
from credentials import username, password
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def sorteador(url, number, remove_repeated):

    #define app options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #comment the line bellow if you want the app to run the web service in the screen
    # Aqui é definido que o chrome será excecutado em segundo plano
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(options=chrome_options)

    #web application url
    url_1 = "https://instagram.com/"

    #go to url
    #vai até a url 'url_1'
    driver.get(url_1)
    sleep(3)


    #login structure
    input_username = driver.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input')
    input_password = driver.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input')
    button_login = driver.find_element('xpath', '//*[@id="loginForm"]/div/div[3]/button')

    #login
    for char in username():
        input_username.send_keys(char)
        time.sleep(0.3)  # 0.2 second delay entre caracteres.
    for char in password():
        input_password.send_keys(char)
        time.sleep(0.2) # 0.2 second delay entre caracteres.

    button_login.click()
    sleep(5)

    #remove pop-ups
    try:
        button_dont_save = driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
        sleep(1)
        button_dont_save.click()
        sleep(3)
    except:
        pass
    try:
        button_dont_notify = driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        sleep(1)
        button_dont_notify.click()
        sleep(3)
    except:
        pass

    #go to required publication that 'url' contains, in this case it is the user who types.
    #vai até a publicação que 'url' contém, no caso é o usuário quem digita.
    driver.get(url)

    #see if there are more comments!
    #Faz a checagem para ver se existem mais comentários!
    while True:
        try:
            # Finds the load more comments button, with a delay until the page loads.
            # Encontra o botão de carregar mais comentários, com um delay até carregar a página.
            wait = WebDriverWait(driver, 10)                                                       
            button_more_comments = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div[2]/div[2]/div/div/ul/li/div')))

            #Click the load more comments button
            # Clica no botão de carregar mais comentários
            button_more_comments.click()
            print('finalmente')
        except:
            print('Sem resultados')
            False
            break

    #Find comments and create a list with the users / remove repeated users
    #Encontra comentários e cria uma lista com os nomes de usuário / remove ou não os usuários repetidos, dependendo do que é selecionado no input do html.
    comments = driver.find_elements(By.CLASS_NAME, "_a9ym")
    list_users = []
    list_checked = []
    for comment in comments:
        user_name = comment.find_element(By.CLASS_NAME, "_a9zc").text
        list_users.append(user_name)
        print(user_name)
    
    #Remove repeated users if remove_repeated = "on" | o 'set' é utilizado para remover usuários repetidos da lista list_users
    # Aqui está a função que remove os usuários repetidos caso remove_repeated esteja com o value = "on"
    if remove_repeated == "on":
        list_checked = list(set(list_users))
    else:
        list_checked = list_users.copy()

    #random the winner
    #vencedor aleatório
    
    list_ch_len = len(list_checked)
    winners = random.choices(list_checked, k = number)
    print(winners)
    info = [list_ch_len, winners]
    #end app
    #fim
    driver.close()
    return info