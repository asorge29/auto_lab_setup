import subprocess
from os import path
import zipfile
from platform import system
#FIXME
def get_windows_desktop():
    if path.exists(path.expanduser('~/OneDrive/Desktop')):
        return path.expanduser('~/OneDrive/Desktop')
    else:
        return path.expanduser('~/Desktop')

def install_blender(zip_url:str = 'https://mirrors.iu13.net/blender/release/Blender4.2/blender-4.2.1-windows-x64.zip'):
    system_name = system()
    print(f'Detected system: {system_name}')
    if system_name == 'Windows':
        desktop_path = get_windows_desktop()
    else:
        desktop_path = path.expanduser('~/Desktop')
    print(f'Desktop path: {desktop_path}')
    print(f'Downloading Blender from {zip_url}')

    install_command = f'cd {desktop_path}; iwr {zip_url} -OutFile blender.zip' if system_name == 'Windows' else f'cd {desktop_path}; curl {zip_url} --output blender.zip'
    print(f'Running: {install_command}')
    print('Downloading Blender...')
    subprocess.run([f'cd {desktop_path}', f'iwr '], shell=True, text=True)
    print('Download complete!')

    zip_path = path.join(desktop_path, 'blender.zip')
    print(f'Blender zip path: {zip_path}')

    print('Extracting Blender...')
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(desktop_path)
    if system_name == 'Windows':
        delete_command = f'cd ~; del {zip_path}'
        subprocess.run([delete_command])
        print('Cleaning up...')
    elif system_name == 'Linux':
        delete_command = f'cd ~; rm {zip_path}'
        subprocess.run([delete_command])
        print('Cleaning up...')
    elif system_name == 'Darwin':
        delete_command = f'cd ~; rm {zip_path}'
        subprocess.run([delete_command])
        print('Cleaning up...')
    else:
        print('Unsupported system')
        print('Clean up yourself')

    print('Blender successfully installed!')
    
if __name__ == '__main__':
    install_blender()


import subprocess
from os import path
import zipfile
from platform import system

def get_windows_desktop():
    if path.exists(path.expanduser('~/OneDrive/Desktop')):
        return path.expanduser('~/OneDrive/Desktop')
    else:
        return path.expanduser('~/Desktop')

def install_blender(zip_url: str = 'https://mirrors.iu13.net/blender/release/Blender4.2/blender-4.2.1-windows-x64.zip'):
    system_name = system()
    print(f'Detected system: {system_name}')
    
    if system_name == 'Windows':
        desktop_path = get_windows_desktop()
    else:
        desktop_path = path.expanduser('~/Desktop')
    
    print(f'Desktop path: {desktop_path}')
    print(f'Downloading Blender from {zip_url}')
    
    zip_path = path.join(desktop_path, 'blender.zip')
    
    if system_name == 'Windows':
        # Prepare the download command
        install_command = ['powershell', '-Command', f'Invoke-WebRequest {zip_url} -OutFile "{zip_path}"']
    else:
        install_command = ['curl', zip_url, '--output', zip_path]
    
    print(f'Running: {" ".join(install_command)}')
    print('Downloading Blender...')
    
    # Use subprocess.run correctly
    subprocess.run(install_command, check=True)
    print('Download complete!')

    print('Extracting Blender...')
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(desktop_path)

    print('Cleaning up...')
    delete_command = None
    if system_name == 'Windows':
        delete_command = ['cmd', '/C', f'del "{zip_path}"']
    else:
        delete_command = ['rm', zip_path]

    subprocess.run(delete_command, check=True)
    print('Blender successfully installed!')

if __name__ == '__main__':
    install_blender()
