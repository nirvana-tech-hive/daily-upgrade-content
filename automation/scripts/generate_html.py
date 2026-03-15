import os
import re
import markdown2

def convert_md_to_html(md_file, html_file):
    with open(md_file, "r") as f:
        md_content = f.read()
    html_content = markdown2.markdown(md_content)
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{md_content.split('\n')[0].replace('# ', '')}</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
            img {{ max-width: 100%; }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    with open(html_file, "w") as f:
        f.write(html_template)

content_dir = "content"
for root, _, files in os.walk(content_dir):
    for file in files:
        if file == "post.md":
            md_path = os.path.join(root, file)
            html_path = os.path.join(root, "post.html")
            convert_md_to_html(md_path, html_path)