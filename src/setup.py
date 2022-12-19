import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
#"packages": ["os", ""] is used as example only
build_exe_options = {"packages": ["os", "customtkinter", "tktooltip"], "include_files":["data", "assets"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"



company_name = 'Grupo6'
product_name = 'MLP'

bdist_msi_options = {
'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),

}



setup(
    name="MLP",
    version="0.1",
    description="MLP group 6",
    options={"build_exe": build_exe_options},
    executables=[Executable("app.py", base=base, icon="assets/logoa.ico", shortcut_name="MLP", shortcut_dir="DesktopFolder")],
)

