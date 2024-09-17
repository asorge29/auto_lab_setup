import subprocess
from os import path
import zipfile
from platform import system

def install_blender(zip_url:str = 'https://mirrors.iu13.net/blender/release/Blender4.2/blender-4.2.1-windows-x64.zip'):
    system_name = system()
    print(f'Detected system: {system_name}')
    desktop_path = path.expanduser('~/Desktop')
    print(f'Desktop path: {desktop_path}')
    install_command = f'cd {desktop_path} && curl {zip_url} --output blender.zip'
    print(f'Running: {install_command}')
    print('Downloading Blender...')
    subprocess.run([install_command], shell=True, text=True)
    zip_path = path.join(desktop_path, 'blender.zip')
    print(f'Blender zip path: {zip_path}')
    print('Extracting Blender...')
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(desktop_path)
    if system_name == 'Windows':
        delete_command = f'cd {path.jdesktop_path} && del blender.zip'
        subprocess.run([delete_command])
        print('Cleaning up...')
    elif system_name == 'Linux':
        delete_command = f'cd {desktop_path} && rm {zip_path}'
        subprocess.run([delete_command])
        print('Cleaning up...')
    elif system_name == 'Darwin':
        delete_command = f'cd {desktop_path} && rm {zip_path}'
        subprocess.run([delete_command])
        print('Cleaning up...')
    else:
        print('Unsupported system')
        print('Clean up yourself')

    print('Blender successfully installed!')
    
if __name__ == '__main__':
    install_blender()
