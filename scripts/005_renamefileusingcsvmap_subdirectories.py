"""
Created: 07/06/2022
Updated 07/06/2022
Author: slopezmarcano

"""
#Rename files using a csv map. The csv map is a two column csv (column 1=old_filename and column2=new_filename). The script renames the files rather than copy or move the original files. A backup is recommended.

#--IMPORT MODULES--#
import os
import pandas as pd

#--DEFINE DIRECTORY--#
dr = '' #add here your directory where the data is. This is the parent directory.

#--READ CSV MAP--#
df = pd.read_csv("output_samples/csv_map_sample.csv")#two columns

#-RUN THROUGH THE DIRECTORY, MATCH THE FILE WITH NAME IN CSV MAP AND THEN RENAME BUT USING THE SAME FILE STRUCTURE --#
for root, dirs, files in os.walk(dr):
    for f in files:
        for row in df.itertuples():
            old_filename = row[1]
            new_filename = row[2]
            if f == old_filename:
                os.rename(root + "/" + f, root + "/" + new_filename) #videos are saved in the same directory structure
            else:
                print(old_filename + " does not exist")