def main():
    print("Due to changes to Google's APIs, Folderclone is dead.")
    yn = input('Would you like me to uninstall folderclone for you? [Y/n] ')
    if len(yn) == 0 or yn.lower()[0] == 'y':
        import subprocess, sys
        subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', 'folderclone', '-y'])