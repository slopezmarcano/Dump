# %%
"""
Created: 18/06/2022
Updated: 01/07/2022
Author: slopezmarcano

"""

#-- IMPORT LIBRARIES --#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#-- IMPORT DATASET --#
#this dataset has 6 columns.
#filename: a unique filename
#species: is there 1 or multiple species in that video?
#location: where was this video collected?
#other columns

videos = pd.read_csv('https://www.dropbox.com/s/985xt1wqw9fk1oh/testing_metadata.csv?dl=1')

#-- FUNCTION --#
def random_selection_species(dataset, single_frac, multi_frac):
    species = dataset[['filename', 'species']]
    grouped = species.groupby('species', group_keys=False)
    species['species'].replace(['single', 'multiple'],[0,1],inplace=True)
    species['c'] = np.select([species['species'].eq(0), species['species'].eq(1)], [single_frac, multi_frac])
    random_selection = species.loc[grouped.apply(lambda x: x['c'].sample(frac=x['c'].iloc[0])).index, ['filename', 'species']]
    random_selection['species'].replace([0,1], ['single', 'multiple'], inplace=True)

    return random_selection

video_selection = random_selection_species(videos, 0.1, 0.8)

# %%
