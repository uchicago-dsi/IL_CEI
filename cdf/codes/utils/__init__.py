
import importlib
import pkgutil

# Import all symbols from submodules
submodule_names = ['cleaning', 'geocoding', 'vizualizing']

for name in submodule_names:
    module = importlib.import_module(f'.{name}', __name__)
    globals().update(vars(module))


print("utils package is being imported!")




