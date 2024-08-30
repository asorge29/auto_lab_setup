import subprocess
import requests
import os
import time

def check_installed():
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True, check=True)
        version = result.stdout.strip().replace('git version', '').strip()
        if version:
            print(f'GIT is installed\nVersion: {version}')
            return True, version
        else:
            print('GIT is installed but unable to determine the version.')
            return False, None
    except subprocess.CalledProcessError:
        print('GIT is not installed, proceeding to git install')
        return False, None
    except FileNotFoundError:
        print('GIT is not installed, proceeding to git install')
        return False, None

def download_git_installer(url, destination_path):
    print("Downloading Git installer...")
    response = requests.get(url)
    with open(destination_path, 'wb') as file:
        file.write(response.content)
    print("Download completed.")

def install_git(installer_path):
    print("Starting Git installation...")
    try:
        # Run the installer with silent mode options
        subprocess.run([installer_path, '/SILENT'], check=True)
        print("Git installation completed.")
    except subprocess.CalledProcessError as e:
        print(f"Installation failed: {e}")

def main():
    # Step 1: Check if Git is already installed
    is_installed, git_version = False, None
    if is_installed:
        print(f"Git is already installed with version {git_version}.")
        return

    # Step 2: Download the Git installer
    git_installer_url = "https://github.com/git-for-windows/git/releases/download/v2.41.0.windows.1/Git-2.41.0-64-bit.exe"  # Change to the latest version URL
    installer_path = os.path.join(os.getcwd(), 'GitInstaller.exe')
    download_git_installer(git_installer_url, installer_path)

    # Step 3: Run the Git installer
    install_git(installer_path)

    # Step 4: Wait a few seconds and verify installation
    time.sleep(10)  # Wait a bit for installation to complete
    is_installed, git_version = check_installed()
    if is_installed:
        print(f"Git was successfully installed with version {git_version}.")
    else:
        print("Git installation failed or was not completed.")

if __name__ == "__main__":
    main()
