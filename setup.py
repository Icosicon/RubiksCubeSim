from cx_Freeze import setup,Executable
base ="Win32GUI"
setup(name="Cube Sim",
      version='0.6',
      decription="Rubiks Cube Simulator",
      executables = [Executable(script="Rubik's Cube Sim.py",icon="Interface\ICO\Icon.ico",base=base)])
