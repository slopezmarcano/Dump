"""
Created: 27/05/2022
Updated: 03/05/2022
Author: slopezmarcano

"""
#A python script that is monitoring events and creating actions. In this case, all new zip files that are uploaded from a 3D reconstruction app are extracted into the same folder.

#-- IMPORT MODULES --#
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from zipfile import ZipFile

#-- DEFINE THE EVENT HANDLER--#
if __name__ == "__main__":
    patterns = ["*.zip"] #only zip files
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

#-- FUNCTIONS WITH ACTIONS TO HANDLE ALL EVENTS --#
def on_created(event):
    z = ZipFile(event.src_path)
    z.extractall()
    z.close()
    print(f"{event.src_path} has been created!")

def on_deleted(event):
    print(f" {event.src_path} has been deleted!")

def on_modified(event):
    print(f" {event.src_path} has been modified")

#def on_moved(event):
    #print(f"someone moved {event.src_path} to {event.dest_path}")


my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved


#-- CREATE AN OBSERVER --#
path = "."
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

#-- START THE OBSERVER --#
my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
