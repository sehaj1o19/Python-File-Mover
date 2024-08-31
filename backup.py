import os
import shutil
import datetime
import schedule
import time

source_dir = "/Users/ekamjotsingh/desktop/Study/Projects/Backup/Main"
destination_dir = "/Users/ekamjotsingh/desktop/Study/Projects/Backup/Backup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    #print(f"Source Directory: {source}")
    #print(f"Destination Directory: {dest_dir}")

    try:
        print(f"Attempting to copy from {source} to {dest_dir}...")
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")

copy_folder_to_directory(source_dir, destination_dir)

def job():
    copy_folder_to_directory(source_dir, destination_dir)

schedule.every().day.at("10:00").do(job)

#schedule.every().day.at("10:00").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
