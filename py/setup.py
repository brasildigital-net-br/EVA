import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "datetime", "pyperclip"], "includes": [
    "tkinter", "pyperclip", "re", "messagebox"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Atendimentos",
    version="0.1",
    description="Minha 1° Aplicação!",
    options={"build_exe": build_exe_options},
    executables=[Executable("Flash 4.py", base=base)]
)
