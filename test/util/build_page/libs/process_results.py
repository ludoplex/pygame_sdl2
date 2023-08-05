from __future__ import with_statement

import os 

from pywebsite.escape import ehtml
from helpers import relative_to, norm_le
from build_client.helpers import create_zip

def process_zip(rz, results_dir):
    ########################################################################
    # Dump out results and installer for /index.php
    #

    installer_name = rz.installer

    txts = ('prebuilt', 'buildresults')
    for f in (f for f in txts if f in rz.namelist()):
        fname = relative_to(__file__, f'../{f}_{rz.platform_id}.txt')
        with open(fname, 'w') as fh:
            fh.write(rz.read(f))

    if installer_name:
        with open(relative_to(__file__, f'../{installer_name}'), 'wb') as fh:
            fh.write(rz.read(installer_name))

    ########################################################################
    # Archive The Text
    #

    archive_zip = os.path.join(
        results_dir, 'archives', f'{rz.platform_id}_{rz.latest_rev}.zip'
    )

    rz.archive_text(archive_zip)