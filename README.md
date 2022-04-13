# Dump
![Status](https://img.shields.io/badge/Status-Ongoing-orange)

## Summary
A flexible repository that stores random R or Python code for different data science projects from Sebastian Lopez-Marcano

## Script 001
`001_annotation_heatmaps_FishID.R`

Deep learning models, like fish object detection models require lots of training data. At FishID we have built models that have >50,000 fish annotations. These annotations
are done by different users with different levels of expertise. I wanted to develop a _easy to use script_ (in R) that would display frame regions where there are many or few annotations.

This annnotation heatmap can be used for quality assurance and quality check. You can compare training and evaluation annotation heatmaps for a species to determine annotation bias or potential ecological dynamics (e.g. fish swimming always near the substrate).

My script has different data requirements, which are documented in `001_annotation_heatmaps_FishID.R`

The output of my script looks like this ![alt text](http://url/to/img.png)


