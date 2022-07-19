"""
Created: 07/06/2022
Updated: 07/06/2022
Author: slopezmarcano
"""
#Rename files using a csv map. The csv map is a two column csv (column 1=old_filename and column2=new_filename). The script renames the files rather than copy or move the original files. A backup is recommended.

#Remember to have this script in the directory where the images are or add a directory variable to the script.

#--IMPORT MODULES--#
import os
import pandas as pd

#--READ YOUR CSV MAP --#
df = pd.read_csv("output_samples/csv_map_sample.csv")#two columns

#--ITERATE OVER EACH ROW AND COLUMN AND RENAME THE FILES--#
for row in df.itertuples():
    old_filename = row[1]
    new_filename = row[2]
    if os.path.exists(old_filename):
        os.rename(old_filename, new_filename)
    else:
        print (old_filename + " does not exist")