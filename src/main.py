import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    
    for root, dirs, files in os.walk(dir_path_content):
        for name in files:
            if name.endswith(".md"):
                rel_path = os.path.relpath(root, dir_path_content)
                output_path = os.path.join(dir_path_public, rel_path,name[:-3] + ".html")
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                generate_page(
                    os.path.join(root, name),
                    template_path,
                    output_path,
                    basepath
                )







main()