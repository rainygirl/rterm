from pathlib import Path
import os

defaultdir = str(Path.home()) + '/'

p = {
    'pathkeys': ['path_data'],
    'path_data': defaultdir + '.rterm_data/'
}

for d in p['pathkeys'] :
    if not os.path.exists(p[d]) :
        os.mkdir(p[d])

