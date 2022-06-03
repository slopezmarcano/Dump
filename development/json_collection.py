"""
Created 
Updated
Author: slopezmarcano

"""

import os
import pandas as pd

directory = "/Users/sebs/Library/Mobile Documents/com~apple~CloudDocs/3DMods"

metadata =[]
for root, directories, files in os.walk(directory, topdown=False):
	for name in files:
        if name.endswith("info.json"):
            f = os.path.join(root,name)
            df = pd.read_json(f)
            df2 = df[['title','gpsLatitude', 'gpsLongitude']].drop_duplicates()
        metadata.append((df2))

metadata_logbook = pd.concat(metadata).drop_duplicates()
metadata_logbook.to_csv('metadata_logbook.csv')
