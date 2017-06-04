# Builtin imports
import sys
import shutil
import os

# Internal imports
import pyfav_utils

# External imports
import requests

filepath = os.path.dirname(os.path.abspath(__file__))

url = sys.argv[1]

name = sys.argv[2]

# Make a request to the webpage to find the icon
favicon_url = pyfav_utils.get_favicon_url(url)

site_name = name.replace(" ", "_").lstrip()

print(favicon_url)
# Download it
r = requests.get(favicon_url, stream=True)
if r.status_code == 200:
    final_name = site_name+"."+favicon_url.split(".")[-1]
    print (final_name)
    path = "images/{}".format(final_name)
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
else:
    print (r.status_code)
    sys.exit()


# Create the desktop entry
desktop_template = '''
[Desktop Entry]
Name={0}
Type=Application
Icon={1}
Exec=xdg-open {2}
'''

icon_path = "{0}/{1}".format(filepath, path)

final_template = desktop_template.format(site_name, icon_path, url)
print (final_template)

application_dir = os.path.expanduser("~/.local/share/applications")
f = open("{0}/{1}.desktop".format(application_dir, site_name), "w")
f.write(final_template)
f.close()
print ("Done")
