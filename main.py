from logging import exception
from os import getcwd, system
from pathlib import Path
from time import sleep
import chromedriver_binary
from login.chromedrive import ChromeDriver
from src.etapas.Processos import login, processo_perfil, salvar_pdf

ROOT_DIR = str(Path(getcwd()))
CHROME_PORT = '9222'
url = 'https://www.linkedin.com/home'


def create_profile():
    call_start_chrome = r'start "Chrome" chrome.exe'
    call_port = fr'--remote-debugging-port={CHROME_PORT}'
    chrome_profile = fr'{ROOT_DIR}\bin\chromeprofile'
    call_data_dir = fr'--user-data-dir="{chrome_profile}"'

    comm = fr'{call_start_chrome} {call_port} {call_data_dir}'

    system(comm)


def main():
    try:
        chrome_driver = ChromeDriver(ROOT_DIR, CHROME_PORT).driver()
        chrome_driver.get(url)
        login(chrome_driver)
        processo_perfil(chrome_driver)
        salvar_pdf(chrome_driver)

    except Exception:
        exception('Erro no projeto.')

    finally:
        sleep(2)


if __name__ == '__main__':
    main()
