'''
# Author: Sunny Bhaveen Chandra
# Contact: sunny.c17hawke@gmail.com
# dated: March 08th, 2020
# NOTE: must be used with templates folder which contains 
        templates of index and base html 
'''
import os
from shutil import copyfile as cp
import time

def path_maker(p1=None, p2=None):
    return os.path.join(p1, p2)

def make_dir_structures(root=None):
    '''
    creates a dir skelton for the flask project
    '''
    os.makedirs(path_maker(root, "templates/placeholders"))
    static_dirs = ["css", "script", "uploads"]
    for static_dir in static_dirs:
        os.makedirs(path_maker(root, f"static/{static_dir}"))

def copy_templates_to_dirs(templates=None, root=None):
    '''
    copies html templates to the template directory 
    in root from templates
    '''
    cp(path_maker(templates, "app.py"), path_maker(root, "app.py"))
    htmls = ["base.html", "index.html"]
    for html in htmls:
        cp(path_maker(templates, html), path_maker(root, f"templates/{html}"))
    
def touch_empty_files(root=None):
    '''
    creates empty css and js file in the static dir
    '''
    def file_maker(path=None):
        with open(path, "w") as f:
            f.write("")
            print(f"created file {path}")

    static_root = path_maker(root, "static")
    files = ["css/main.css", "script/index.js"]
    for file in files:
        path = path_maker(static_root, file)
        file_maker(path)

def main():
    ROOT = time.strftime("FlaskApp_%Y_%m_%d-%H_%M_%S")
    TEMPLATES = "templateFiles"
    # make_dir_structures - 
    make_dir_structures(root=ROOT)
    copy_templates_to_dirs(templates=TEMPLATES, root=ROOT)
    touch_empty_files(root=ROOT)

if __name__=="__main__":
    main()