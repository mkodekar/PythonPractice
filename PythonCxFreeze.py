from cx_Freeze import setup, Executable

setup(name='ImageShower',
      version='0.1',
      description='Image show',
      executables=[Executable('TkinterLibrary.py')])
