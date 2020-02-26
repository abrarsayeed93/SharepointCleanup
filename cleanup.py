from path import Path
import time
import os
import re
import subprocess
import glob
import shutil




d = Path('E:\SharePoint\Reporting - Sales GPS Documents\\') #set root path
exclude=set(['E:\SharePoint\Reporting - Sales GPS Documents\Training\\'])#folder NAME i dont want to walk in(any folder with 2 seperate files)

num_files = 0

for root, dirs, files in os.walk(d):

    dirs[:] = [d for d in dirs if d not in exclude]

    num_files = len(files)

    i = num_files - 5

    if i>0:

        sorted(d.files(), key=os.path.getctime)
        files2remove=files[:i]

        for x in range(0,len(files2remove)):


            removedFile= files2remove[x]


            for subdir, dirs, files in os.walk(root):


                for file in files:
                    if file == removedFile:
                        print('the removed file is:',file)
                        try:
                            shutil.copy(os.path.join(subdir, file), '.\\Archive\\')
                        except:
                            shutil.copy(os.path.join(subdir, file), '.\\Archives\\')
                        finally:
                            pass
                        os.remove(os.path.join(subdir, file))
    else:
        pass

print('file removal completed')


include=[Path('E:\SharePoint\Reporting - Sales GPS Documents\Training\\')] #the excluded folder paths before

'''
for v in range(0,len(exclude)):
    d= Path(include[v])
    for root,dirs,files in os.walk(d):

        num_files = len(files)

        i = num_files - 12
        print("no of files to be removed:", i)
        if i>0:

            sorted(d.files(), key=os.path.getctime)
            files2remove=files[:i]

            for x in range(0,len(files2remove)):


                removedFile= files2remove[x]


                for subdir, dirs, files in os.walk(d):

                    for file in files:
                        if file == removedFile:
                            print('the removed file is:',file)

                            os.remove(os.path.join(subdir, file))
        else:
            pass

print('file removal completed')



'''














