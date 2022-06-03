"""
Created:
Updated
Author: slopezmarcano

"""

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from zipfile import ZipFile

#Step 2 - the event handler
if __name__ == "__main__":
    patterns = ["*.zip"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

#Step 3 - handle all the events
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
    #print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")


my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved


#Step 4 - create an observer
path = "."
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

#Step 5 - start the observer
my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
