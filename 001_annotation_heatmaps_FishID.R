#Created:06/04/2022
#Updated: 13/04/2022
#Author: slopezmarcano

#Script to visualise FishID annotations as a heatmap to perform quality assurance and control

#-- LIBRARIES --#
library(tidyverse)
library(ggplot2)
library(ggforce)
library(ggThemeAssist)
library(gridExtra)

#-- READ ANNOTATIONS CSV --#
#Export annotation csv from FID20. Go to Datasets, select the iteration to perform the QA and QC and export annotations as csv

#add here a dropbox link or path to the csv file
annos <- read_csv("https://www.dropbox.com/s/lmtrdok2f5tvabp/mbeec-masktest_iteration8.csv?dl=1") #This example uses the Moreton Bay Dataset from 2017-2021


#-- DATASET STRUCTURE --#
#The annos file should be a csv file and must have the following columns. Each row represents an annotation.
#xmin= minimum x value of bounding box detection [can use xmax or difference]
#ymin= minumim y value of bounding box detection [can use ymax or difference]
#category_id= numerical id (e.g. 1 or 10) for each species or class annotated. circular reference.
#className= character. name of the class. e.g. Australasian Snapper
#width= image width
#height= image height
#id= unique id of an annotation. must be unique across the entire dataset.

#--- SELECT SPECIES ---#
species <- annos %>%
  group_by(category_id, className)%>%
  distinct(category_id)%>%
  rename(species=className,
         category_id2=category_id)

#--- FUNCTION CODE --#
annotations_heatmaps <- function (category_id2){
  #REQUIREMENTS
  #category_id2: circular id from the annotations files (annos) [see line 32-36]

  #Generate x and y bins
  q <- seq(1,max(annos$width), length.out = 20)
  e <- seq(1,max(annos$height), length.out = 20)

  #Create combinations between (X and Y) expand grid
  data <- expand.grid(X=q, Y=e)

  #Select bin X values
  Xvalues <- data %>%
    select(X) %>%
    distinct(X)%>%
    mutate(join=1)

  #Select bin Y values
  Yvalues <- data %>%
    select(Y) %>%
    distinct(Y) %>%
    mutate(join=1)

  #Select the detections for one species
  detections <- annos %>%
    filter(category_id==category_id2)%>%
    select(xmin, ymin, id)%>% #selecting xmin and ymin of the
    mutate(join=1)

  #Calculate the difference between all detections (x values) and x bin values
  xdifferences <- Xvalues %>%
    full_join(detections)%>%
    mutate(xdifference=abs(xmin-X))%>%
    group_by(id)%>% #all annotations have a unique ID
    slice(which.min(xdifference)) %>% #select the lowest difference between detection X and x bin value for each annotation
    select(id,X)

  #Calculate the difference between all detections (y values) and y bin values
  ydifferences <- Yvalues %>%
    full_join(detections)%>%
    mutate(ydifference=abs(ymin-Y))%>%
    group_by(id)%>% #all annotations have a unique ID
    slice(which.min(ydifference)) %>% #select the lowest difference between detection Y and Y bin value for each annotation
    select(id,Y)

  combined_x_y <- full_join(xdifferences, ydifferences) #combine the x and y differences

  #Output of the function.
  counts <- combined_x_y %>%
    group_by(X,Y)%>%
    summarise(n = n())%>% #counts per bin
    ungroup() %>%
    mutate(freq = (n / sum(n)))%>% #calculate the frequency of annotations per bin
    add_row(X=max(annos$width), Y=max(annos$height), n =0, freq=0)%>% #add fake row to ensure that margins are close to the height and width of the largest image in the dataset
    mutate(category_id2=paste0(category_id2))

 return(counts)
}

#--- RUN THE FUNCTION ---#
annos_freq <- bind_rows(lapply(1:nrow(species), function(x){annotations_heatmaps(species$category_id2[x])}))

#--- ADD SPECIES NAMES TO CATEGORY IDS --#
annos_freq2 <- species %>%
  mutate(category_id2 = as.factor(category_id2)) %>%
  full_join(annos_freq, by='category_id2') %>%
    mutate(freq2 = round((freq * 100),2)) #%>% #turn frequency values to percentages and round
  #filter(freq2 > 0.5) #for future use in case we want to filter #TODO: provide count annotation box in the plots

#--- PLOTS ---#
p=list() #generate empty list
#FOR loop
for (i in unique(species$species)) {

  plot <- annos_freq2 %>%
    filter(species == i)%>%
    ggplot()+
    aes(x=X, y=Y, fill=round(freq2))+
    geom_tile(color = "white",
            lwd = 1.5, linetype = 1)+
    theme_classic()+
    coord_fixed()+
    scale_fill_distiller(type='div', palette = 9, direction = 1) + theme(axis.title = element_text(size = 10),
    axis.text = element_text(size = 10),
    plot.title = element_text(size = 12),
    legend.text = element_text(size = 10),
    legend.title = element_text(size = 10),
    legend.position = "top", legend.direction = "horizontal") +labs(x = "X Bbox Coordinates", y = "Y Bbox Coordinates",
    fill = "Annotation Percentage",
    plot.margin =  margin(10,10,10,10)) + guides(fill = guide_colourbar(barwidth = 15))+
    annotate(geom="text", x=(max(annos$width)/4), y=max(annos$height), label='Bottom of the image', color="black", size=3)+
    ggtitle(i)

  p[[i]] <- ggplotGrob(plot)
}
#Arrange plots across several pages using gridExtra
main <- marrangeGrob(grobs=p, ncol=2, nrow=2)

#Display results
main