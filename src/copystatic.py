import os
import shutil

def website_generation(source, dest):
        if not os.path.exists(dest):
                os.mkdir(dest)
        names = os.listdir(source)
        for name in names:
                full_path = os.path.join(source, name)
                dest_path = os.path.join(dest, name)
                if os.path.isfile(full_path):
                        shutil.copy(full_path, dest_path)
                else:
                        website_generation(full_path, dest_path)

