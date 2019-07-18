"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""
import os
from setuptools import setup
from os import getcwd
from fastai.imports import *

import macholib
print("~"*60 + "macholib verion: "+macholib.__version__)
if macholib.__version__ <= "1.7":
    print("Applying macholib patch...")
    import macholib.dyld
    import macholib.MachOGraph
    dyld_find_1_7 = macholib.dyld.dyld_find
    def dyld_find(name, loader=None, **kwargs):
        #print("~"*60 + "calling alternate dyld_find")
        if loader is not None:
            kwargs['loader_path'] = loader
        return dyld_find_1_7(name, **kwargs)
    macholib.MachOGraph.dyld_find = dyld_find

APP = ['sample_plots.py']
DATA_FILES = []
OPTIONS = {  
    "py2app": {
         "bdist_base": os.path.join(str(Path(os.getcwd()).parent), 'build'),
         "dist_dir": os.path.join(str(Path(os.getcwd()).parent), 'dist'),
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options=OPTIONS,
    setup_requires=['py2app'],
)