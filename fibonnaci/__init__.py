# fibonnaci/__init__.py
from os.path import dirname, basename, isfile, join
import glob
import importlib

# Get all .py files in the directory
module_files = glob.glob(join(dirname(__file__), "*.py"))

# Import all modules dynamically
modules = []
for f in module_files:
    if isfile(f) and not f.endswith('__init__.py'):
        module_name = basename(f)[:-3]
        module = importlib.import_module(f"fibonnaci.{module_name}")
        modules.append(module)

__all__ = [basename(f)[:-3] for f in module_files if isfile(f) and not f.endswith('__init__.py')]