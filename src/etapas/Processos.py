from os.path import exists
from time import sleep
from pywinauto.keyboard import send_keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from variaveis_projeto import variaveis, _email_pessoal, __senha_pessoal, path_pdf
from pywinauto import Application


def login(chrome_driver):
    btn_login = WebDriverWait(chrome_driver, 5).until(
        e_c.presence_of_element_located((By.XPATH, variaveis['btn_entrar'])))
    btn_login.click()
    sleep(2)
    email_campus = WebDriverWait(chrome_driver, 2).until(
        e_c.presence_of_element_located((By.ID, variaveis['campus_email'])))
    email_campus.click()
    sleep(0.5)
    email_campus.send_keys(_email_pessoal)
    sleep(2)
    senha_campus = WebDriverWait(chrome_driver, 5).until(
        e_c.presence_of_element_located((By.ID, variaveis['campus_senha'])))
    senha_campus.click()
    sleep(0.5)
    senha_campus.send_keys(__senha_pessoal)
    sleep(2)
    btn_lkd_entrar = WebDriverWait(chrome_driver, 5).until(
        e_c.presence_of_element_located((By.XPATH, variaveis['btn_entrar_lkd']))).click()
    sleep(5)


def processo_perfil(chrome_driver):
    btn_notificacao = WebDriverWait(chrome_driver, 5).until(
        e_c.presence_of_element_located((By.XPATH, variaveis['btn_notificacao']))).click()
    sleep(5)
    click_perfil = WebDriverWait(chrome_driver, 5).until(
        e_c.presence_of_element_located((By.ID, variaveis['click_perfil']))).click()
    sleep(5)
    btn_perfil = WebDriverWait(chrome_driver, 5).until(
        e_c.presence_of_element_located((By.XPATH, variaveis['visualizar_perfil']))).click()
    sleep(5)


def salvar_pdf(chrome_driver):
    nome_perfil = chrome_driver.find_element_by_xpath(variaveis['perfil_nome']).text
    sleep(1)
    path_completo = f'{path_pdf}\\{nome_perfil}.pdf'
    if exists(path_completo):
        print('Arquivo existente, saindo...')
    else:
        app = Application(backend="uia").connect(title=f"{nome_perfil} | LinkedIn - Google Chrome")
        sleep(1)
        btn_mais = WebDriverWait(chrome_driver, 5).until(
            e_c.presence_of_element_located((By.XPATH, variaveis['btn_mais']))).click()
        sleep(2)
        btn_salvar_pdf = WebDriverWait(chrome_driver, 5).until(
            e_c.presence_of_element_located((By.XPATH, variaveis['btn_salvar_pdf']))).click()
        sleep(1)
        script = app.top_window()
        save = script.window(title='Salvar como')
        sleep(2)
        save.FileNameEdit.set_focus()
        sleep(0.5)
        send_keys('^a')
        sleep(0.5)
        send_keys('{DELETE}')
        sleep(1)
        save.FileNameEdit.set_edit_text(path_pdf + str(f'\\{nome_perfil}'))
        sleep(1)
        save.child_window(title='Salvar', control_type='Button').click()
        sleep(0.5)

        print('Arquivo feito download com sucesso')

    click_perfil = WebDriverWait(chrome_driver, 5).until(
        e_c.presence_of_element_located((By.ID, variaveis['click_perfil']))).click()
    sleep(2)
    sair_btn = WebDriverWait(chrome_driver, 5).until(
        e_c.presence_of_element_located((By.XPATH, variaveis['btn_sair']))).click()
    sleep(2)
    try:
        confirmacao_sair = WebDriverWait(chrome_driver, 2).until(
            e_c.presence_of_element_located((By.XPATH, variaveis['btn_sair_dois']))).click()
        sleep(2)

    except:
        print('Não apareceu a confirmação de salvar dados, bot continue')
