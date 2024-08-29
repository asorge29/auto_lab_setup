from selenium import webdriver
from selenium.webdriver.common.by import By
from os import path, listdir
from time import sleep
import subprocess

def check_installed():
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True, check=True)
        version = result.stdout.replace('git version', '')
        print(f'GIT is installed\nVersion: {version}')
        return True, version

    except subprocess.CalledProcessError:
        print('GIT is not installed, proceeding to git install')
        return False, None

    except FileNotFoundError:
        print('GIT is not installed, proceeding to git install')
        return False, None

def check_downloaded(downloads_path):
    downloads = listdir(downloads_path)
    for i in downloads:
        if i.endswith('64-bit.exe') and i.startswith('Git'):
            print(f'Found git installer {i} in {downloads_path}')
            return True, i
    return False, None

def download_git():
    downloaded = False

    driver = webdriver.Edge()
    driver.get("https://git-scm.com/download/win")
    driver.implicitly_wait(10)
    download_button = driver.find_element(By.LINK_TEXT, '64-bit Git for Windows Setup')
    download_button.click()

    while not downloaded:
        downloaded, installer_file = check_downloaded(path.expanduser('~/Downloads'))
        sleep(0.5)
        print('Downloading Git...')

    print('Finished downloading git!')

#TODO
def install_git():
    pass

def setup_git():
    installed, version = check_installed()
    if not installed:
        downloaded = check_downloaded(path.expanduser('~/Downloads'))
        if not downloaded:
            download_git()
        else:
            pass
            #TODO install_git()
    else:
        print('Git already installed')

if __name__ == '__main__':
    setup_git()