'''
# Author: Sunny Bhaveen Chandra
# Contact: sunny.c17hawke@gmail.com
# Dated: March 08th, 2020
# AIM: It creates a basic folder structure to get you started quickly. Following file 
		and folder structure will be created by using this app -
		/app.py
		/templates
			../placeholders
			../base.html
			../index.html
		/static
			../css
				../main.css
			../script
				../index.js
			../uploads

# NOTE: must be used with templates folder which contains 
        templates of index and base html 
'''
import os
from os.path import join
from shutil import copyfile as cp
import time

def make_dir_structures(root=None):
    '''
    creates a dir skelton for the flask project
    this creates structure -
    /templates
    	../placeholders
    /static
    	../css
    	../script
    	../uploads 
    '''
    path_to_placeholders = join("templates", "placeholders")
    os.makedirs(join(root, path_to_placeholders))
    static_dirs = ["css", "script", "uploads"]
    for static_dir in static_dirs:
    	temp_path = join("static", static_dir)
    	os.makedirs(join(root, temp_path))

def copy_templates_to_dirs(templates=None, root=None):
    '''
    copies html templates to the templates directory 
    in root from templates
	this creates structure as follows- 
	/app.py
	/templates
		../base.html
		../index.html    
    '''
    cp(join(templates, "app.py"), join(root, "app.py"))
    htmls = ["base.html", "index.html"]
    for html in htmls:
    	temp_path = join("templates", html)
    	cp(join(templates, html), join(root, temp_path))
    
def touch_empty_files(root=None):
    '''
    creates empty css and js file in the static dir.
    static file structure =>
   	/static
   		../css
			../main.css
		../script
			../index.js
    '''
    def file_maker(path=None):
        with open(path, "w") as f:
            f.write("")

    static_root = join(root, "static")
    files = ["css/main.css", "script/index.js"]
    for file in files:
    	dir_, file_ =  file.split("/")
    	path_to_file = join(dir_, file_)
    	path = join(static_root, path_to_file)
    	file_maker(path)

def main():
    ROOT = time.strftime("FlaskApp_%Y_%m_%d-%H_%M_%S")
    TEMPLATES = "templateFiles"
    make_dir_structures(root=ROOT)
    copy_templates_to_dirs(templates=TEMPLATES, root=ROOT)
    touch_empty_files(root=ROOT)
    print(f"Successfully created flask boilerplate inside- \n{ROOT}!!")

if __name__=="__main__":
    main()
