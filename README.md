## Disclaimer

All resources is for friend's use only

## Compatibility 
Windows

## How to use
1. Install python3
2. Install pip
3. Install and run miniconda3
4. In miniconda3, run `pip install pyinstaller` and `pip install pyglet`
5. Run `pyinstaller --hidden-import="pyglet,os" --add-data "<PATH>;." --noconsole "<PATH>\Cat_Dungeon.py" --onefile`
6. A file will be located at "C:\Users\<User>\dist\Cat_Dungeon.exe"
