"""
Created: 02/06/2022
Updated 03/06/2022
Author: slopezmarcano

"""
#A script that locates all info.json files, then extracts the 3D reconstruction title, gps latitude and longitude and then add it to a metadata_logbook in a csv format.

import os
import pandas as pd

#-- ADD YOUR DIRECTORY --#
directory = ""

#-- LOOP OVER ALL INFO.JSON FILES AND THEN EXPORT THE CSV --#
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
