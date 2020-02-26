from path import Path
import time
import os
import re
import subprocess
import glob
import shutil




d = Path('E:\\SharePoint\\Reporting - Sales GPS Documents\\Pipeline\\Pipeline Snapshot\\Detailed Student Pipeline PLUS\\') #set root path
exclude=set(['E:\\SharePoint\\Reporting - Sales GPS Documents\\Training\\',
             'E:\\SharePoint\\Reporting - Sales GPS Documents\\Teams\\Finance\\'])#folder NAME i dont want to walk in(any folder with 2 seperate files)


for root, dirs, files in os.walk(d):

    dirs[:] = [d for d in dirs if d not in exclude]

    num_files = len(files)

    i = num_files - 5
    #i=3
    if i>0:

        sorted(d.files(), key=os.path.getctime)
        files2remove=files[:i]

        for x in range(0,len(files2remove)):


            removedFile= files2remove[x]


            for subdir, dirs, files in os.walk(root):
                sorted(d.files(), key=os.path.getctime)
                #print("SUBDIR: ",subdir)

                for file in files:
                    if file.endswith('.zip') or file.endswith('.xlsm'):
                        if file==removedFile:
                            print("removed file:", removedFile)
                            #print("fullpath: ",os.path.abspath(subdir))
                            try:
                                shutil.move(os.path.join(subdir, removedFile),os.path.abspath(subdir))
                                print("File moved to archive before deleting: ",removedFile)
                            except:
                                pass
                            try:
                                shutil.move(os.path.join(subdir, removedFile), os.path.abspath(subdir)+"\\Archive\\")
                                print("File moved to archive before deleting: ",removedFile)
                            except:
                                pass
                            try:
                                shutil.move(os.path.join(subdir, removedFile), os.path.abspath(subdir)+"\\Archives\\")
                                print("File moved to archives before deleting: ",removedFile)
                            except:
                                pass

                            sorted(d.files(), key=os.path.getctime)
                            #os.remove(os.path.join(subdir, file))
                    else:
                        pass
print('file archiving completed')


for root, dirs, files in os.walk(d):

    dirs[:] = [d for d in dirs if d not in exclude]

    num_files = len(files)

    i = num_files - 7
    # i=3
    if i > 0:

        sorted(d.files(), key=os.path.getctime)
        files2remove = files[:i]

        for x in range(0, len(files2remove)):

            removedFile = files2remove[x]

            for subdir, dirs, files in os.walk(root):
                sorted(d.files(), key=os.path.getctime)
                # print("SUBDIR: ",subdir)

                for file in files:
                    if file.endswith('.zip') or file.endswith('.xlsm'):
                        if file == removedFile:
                            print("removed file:", removedFile)
                            # print("fullpath: ",os.path.abspath(subdir))
                            sorted(d.files(), key=os.path.getctime)
                            print("the file being removed is: ", subdir+"\\"+file)
                            os.remove(os.path.join(subdir, file))

print('file archiving completed')


for root, dirs, files in os.walk(d):

    dirs[:] = [d for d in dirs if d not in exclude]

    num_files = len(files)


    # i=3


    sorted(d.files(), key=os.path.getctime)


    for subdir, dirs, files in os.walk(root):
        sorted(d.files(), key=os.path.getctime)
        # print("SUBDIR: ",subdir)

        for file in files:
            #print(file)
            if file=='Archive' or file=='Archives':
                os.remove(os.path.join(subdir, file))



