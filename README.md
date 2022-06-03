# Dump
![Status](https://img.shields.io/badge/Status-Ongoing-orange)

📧 s.lopez-marcano@griffith.edu.au

## ☀️ Summary
A flexible repository that stores random R or Python code for different data science projects from Sebastian Lopez-Marcano.

## 🚀 Script 001
`001_annotation_heatmaps_FishID.R`

Deep learning models, like fish object detection models require lots of training data. At FishID we have built models that have > 50,000 fish annotations 🤯. 

FishID annotations are done by different users with different levels of expertise. I wanted to develop a _easy to use script_ (in R) that would display frame regions where there are many or few annotations.

This annotation heatmap can be used for quality assurance and quality check. You can compare training and evaluation annotation heatmaps for a species to determine annotation bias or potential ecological dynamics (e.g. fish swimming always near the substrate).

My script has different data requirements, which are documented in `001_annotation_heatmaps_FishID.R`

To use (if data requirements are met 🚨), you only need to read your annotation csv.

The output of my script looks like this ![alt text](https://github.com/slopezmarcano/Dump/blob/main/output_samples/001_annotation_heatmap_sampleoutput.png)

Regions with red are areas with low annotation percentage. Overall, we want to see a good distribution of annotations across the entire frame, but depends on the species ecology.

Hope you can use it, and good luck 🍀

## 🚀 Script 002 and 003
`002_watchdog_monitor.py` & `003_json_collection.py`


Fieldwork is a tedious but necessary task in environmental science. 
Traditionally, all data collected is stored in hard drives or written down in notepads. I wanted to fix this! (or at least provide a sneak peek on how automation can help with this process).


**💡My idea**: Auto-populate a metadata file with the survey_name, GPS lat and GPS long when doing 3D reconstructions.


**📝The workflow**: Anytime a 3D reconstruction was uploaded to a cloud folder, then a python workflow would start and produce a csv file that included metadata files (already collected by our sensor).


**🚨The sensor**: An Iphone 13 Pro with the 3d Scanner App


**🛠How does it work?**: Using your Iphone, open the 3d Scanner App, then do the reconstruction. Once done and processed, share `All Data` to an iCloud folder and then inside the iCloud folder two python scripts will 1) Grab any zip folder with the reconstructions file and decompress it and 2) select the `info.json` (file that contains the metadata), extract the relevant information and then output a clean csv. 

`002_watchdog_monitor.py`: a python script that has a watchdog. A watchdog is a monitoring system where you specify a folder to constantly observe. The watchdog has specific actions for created, modified, deleted or moved files.
`003_json_collection.py`: a python script with a simple for loop that searches all info.json files (where metadata of the 3D reconstructions are stored), and then extract and output the key metadata values.

Hope you can use it, and good luck 🍀