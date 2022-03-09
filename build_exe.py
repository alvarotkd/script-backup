import PyInstaller.__main__

PyInstaller.__main__.run([
    'backup.py',
    '--onefile',
    '--console', # or --windowed if you don´t need windows command line
    '--name',
    'AppName',
    '--clean'
])