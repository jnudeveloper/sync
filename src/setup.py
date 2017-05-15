from distutils.core import setup
import py2exe
import sys

# this allows to run it with a simple double click.
sys.argv.append('py2exe')

py2exe_options = {
    "includes": ["wx","prompt","gui","process_win","hash_algorithm","path","serialize","sync","synchash","path_win"],
    "dll_excludes": ["MSVCP90.dll", ],
    "compressed": 1,
    "optimize": 2,
    "ascii": 0,
}

setup(
    name='Sync',
    version='1.0',
    windows=[{"script": 'main_win.py'}],
    zipfile=None,
    options={'py2exe': py2exe_options}
)