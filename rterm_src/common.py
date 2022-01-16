import os
from pathlib import Path

defaultdir = str(Path.home()) + "/"

p = {"pathkeys": ["path_data"], "path_data": defaultdir + ".rterm_data/"}

FEEDS_FILE_NAME = os.path.join(p["path_data"], "feeds.json")

for d in p["pathkeys"]:
    if not os.path.exists(p[d]):
        os.mkdir(p[d])
