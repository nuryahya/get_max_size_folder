"""Main module."""

import os
import logging

"""-------------------------------------------------------------------------
        Tool:               Get Maximum Sie Folder
        Source Name:        get-max-size-folder.py
        Version:            0.0.0
        Author:            Nur Yahya
        Usage:              MaxSizeFolder(FolderPath)

        Required Arguments: Full Path of the Directory


        Description:        Finds Maximum size folder in a Directory  and
                            puts the result in the dir in a text file
                           named = Maximum_Size_Folder.txt
        Updated:            Not yet.
        ------------------------------------------------------------------------"""

class MaxSizeFolder(object):
    def __init__(self,directory):
        self.label = "Get Maximum Sie Folder"
        self.description = "Looks for a maximum size Folder  " + \
                           "in a Directory given as an input parameter. " + \
                           "The user will find the output in 'Maximum_Size_Folder.txt' "+\
                            "file in the directory stated ."
        self.directory = directory


    def execute(self):
        directory = self.directory

        def get_size(path=os.getcwd()):
            print("Calculating Size: ", path)
            total_size = 0
            # if path is directory--
            if os.path.isdir(path):
                print("Path type : Directory/Folder")
                for dirpath, dirnames, filenames in os.walk(path):
                    for f in filenames:
                        fp = os.path.join(dirpath, f)
                        # skip if it is symbolic link
                        if not os.path.islink(fp):
                            total_size += os.path.getsize(fp)
            return total_size

        def get_max_folder_size(directory):
            max_folder_size = 0
            max_folder_name = ''
            for foldername in os.listdir(directory):
                folder_path = os.path.join(directory, foldername)
                if os.path.isdir(folder_path):
                    folder_size = get_size(folder_path)
                    if folder_size > max_folder_size:
                        max_folder_size = folder_size
                        max_folder_name = foldername
            return max_folder_name, max_folder_size

        max_folder_name, max_folder_size = get_max_folder_size(directory)
        os.chdir(directory)
        logging.basicConfig(filename='FeatureDictionary.log', level=logging.INFO)
        with open('Maximum_Size_Folder.log', 'w') as textWriter:
            textWriter.write("Max Folder Name = {0},Size = {1}".format(max_folder_name,max_folder_size))

        with open('Maximum_Size_Folder.txt', 'w') as f:
            f.write("Max Folder Name = {0},Size = {1}".format(max_folder_name,max_folder_size))


st = MaxSizeFolder(directory = str(input("FolderPath :")))
st.execute()
