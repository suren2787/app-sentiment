from pathlib import Path
import os

def renamefile(file_name_str, backup_filename_str):
    curr_file = Path(file_name_str)
    if curr_file.is_file():
        os.rename(file_name_str,backup_filename_str)

# # Writing to sample.json
def savefile(file_name_str, json_object):
    with open(file_name_str, "w",encoding="utf-8") as outfile:
        outfile.write(json_object)