import sys
from cx_Freeze import setup, Executable
import Classificacao

base = None
if sys.platform == "win64":
    base = "Win64GUI"

Executables = [
    Executable("classification.py", base=base)
]

buildOptions = dict(
    packages = [],
    includes = ["Classificacao"],
    include_files = [],
    excludes = []
)

setup(
    name = "Classificacao",
    version="1.0",
    description = "Espero que funcione",
    options = dict(build_exe = buildOptions),
    Executables = Executables
)