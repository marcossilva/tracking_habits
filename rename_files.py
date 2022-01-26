import glob
import os
import re
from datetime import datetime
files = glob.glob("*/*.md")
for f in files:
    date_start = f.split('/')[-1].split('_')[0]
    if not re.search("\d", date_start):
        destination = '/'.join(f.split('/')[:-1])
        title = datetime.today().strftime('%Y%m%d') + '_' + open(f, 'r').readline()[1:].strip().lower().replace(' ', '_').replace('-', '_') + '.md'
        destination = os.path.join(destination, title)
        os.rename(f, destination)

