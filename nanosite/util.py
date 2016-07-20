import os
import markdown
import shutil
import subprocess

def same_path(a, b):
    return os.path.abspath(a).lower() == os.path.abspath(b).lower()

# compile markdown to HTML, returning (html, meta_info) tuple
def compile_markdown(md_text):
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    html = md.convert(md_text)
    try:
        meta = {k: "".join(v) for k, v in md.Meta.items()} \
           if md.Meta is not None else {}
    except AttributeError:
        meta = {}
    return (html, meta)

def clean_output_dir(site_dir, output_dir):
    path = os.path.join(site_dir, output_dir)
    if os.path.isdir(path):
        shutil.rmtree(path)
        print("Cleaned output directory.")
    else:
        print("Nothing to clean.")
        
def delete_site_dir(top):
    for f in os.listdir(top):
        path = os.path.join(top, f)
        if os.path.isfile(path):
            os.unlink(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
    
def publish_site(top, meta_dir):
    cur_dir = os.getcwd()
    os.chdir(top)
    # run publish script from site top directory
    subprocess.call(os.path.join(top, meta_dir, "publish"))
    os.chdir(cur_dir)
    print("Finished running publish script.")
