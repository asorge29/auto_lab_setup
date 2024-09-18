import subprocess
from os import path
import zipfile
from platform import system
#FIXME
def get_windows_desktop():
    if path.exists(path.expanduser('~\\OneDrive\\Desktop')):
        return path.expanduser('~\\OneDrive\\Desktop')
    else:
        return path.expanduser('~\\Desktop')

def install_blender(zip_url:str = 'https://mirrors.iu13.net/blender/release/Blender4.2/blender-4.2.1-windows-x64.zip'):
    system_name = system()
    print(f'Detected system: {system_name}')
#TODO make platform specific adjustments
    if system_name == 'Windows':
        desktop_path = get_windows_desktop()
        logical_and = ';'
    else:
        desktop_path = path.expanduser('~\\Desktop')
        logical_and = '&&'
    print(f'Desktop path: {desktop_path}')
#FIXME windows ps script with iwr and OutFile
    install_command = f'cd {desktop_path} {logical_and} curl {zip_url} --output blender.zip'
    print(f'Running: {install_command}')
    print('Downloading Blender...')
    subprocess.run([install_command], shell=True, text=True)
    zip_path = path.join(desktop_path, 'blender.zip')
    print(f'Blender zip path: {zip_path}')

    print('Extracting Blender...')
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(desktop_path)
    if system_name == 'Windows':
        delete_command = f'cd {path.expanduser('~')}; del blender.zip'
        subprocess.run([delete_command])
        print('Cleaning up...')
    elif system_name == 'Linux':
        delete_command = f'cd {path.expanduser('~')} && rm {zip_path}'
        subprocess.run([delete_command])
        print('Cleaning up...')
    elif system_name == 'Darwin':
        delete_command = f'cd {path.expanduser('~')} && rm {zip_path}'
        subprocess.run([delete_command])
        print('Cleaning up...')
    else:
        print('Unsupported system')
        print('Clean up yourself')

    print('Blender successfully installed!')
    
if __name__ == '__main__':
    install_blender()
