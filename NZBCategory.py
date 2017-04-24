#!/usr/bin/env python2
# -*- coding: iso-8859-15 -*-
#
# NZBFile Categoryparser scan script for NZBGET
#
# Author of the collected code snippets: <wusamba a@t gmail d.t com>
# NOTE: Adapted from NZBPass.py to NZBCategory.py by ProfDrLuigi
#
# $Revision: 140 $
# $Date: 2013-06-12 09:41:23 +0200 (Mon, 04 Aug 2014) $
# $File: pfftn_2x.py $
#
# Check first line "#!/usr/local/zy-pkgs/bin/python2.6" and maybe adjust it!
#
# Changelog:
#
# v1.4:
# - fix configuration definition to work with nzbget v13
# - shorter filename
#
# v1.3:
# - regex added to remove unwanted information in some filenames (only German)
#
# v1.2:
# - rewrite for python v2 (localisation problem on NSA325 with python v3)
#
# v1.1:
# - utf-8 fix
#
# v1.0:
# - inital version for nzbget v11 @ Windows

##############################################################################
### NZBGET SCAN SCRIPT                                                     ###

# Extract + replace category from filename and set Category @ nzbget.
#
# This script is setting the Category from the filename and removes it from NZB Name: file*[[category]]*.nzb
#
#
# NOTE: Adapted from NZBPass.py to NZBCategory.py by ProfDrLuigi
#
#
# NOTE: This script requires Python (v2 or later) to be installed on your system.
#
# NOTE: Many thanks to:
#
#   freem@n: http://nzbget.sourceforge.net/forum/viewtopic.php?p=5167#p5167 for his RegExp: ^.*?\[\[(.*?)\]\]
#
#   hugbug (Andrey Prygunkov): http://nzbget.sourceforge.net for nzbget, EMail.py and his documentation. I hope I can use a little bit from your code (EMail.py).
#   Autor: http://www.tutorialspoint.com/python/python_reg_expressions.htm for RegExp with Python.

### NZBGET SCAN SCRIPT                                                     ###
##############################################################################

import os, re, sys

# Code from EMail.py @ http://nzbget.sourceforge.net
# Exit codes used by NZBGet
POSTPROCESS_SKIP=95
POSTPROCESS_ERROR=94
POSTPROCESS_SUCCESS=93

# Code from EMail.py @ http://nzbget.sourceforge.net
# Check if the script is called from nzbget 13.0 or later
if not 'NZBOP_SCRIPTDIR' in os.environ:
    print('*** NZBGet post-processing script ***')
    print('This script is supposed to be called from nzbget (13.0 or later).')
    sys.exit(POSTPROCESS_ERROR)

if not 'NZBNP_NZBNAME' in os.environ:
    print('[WARN] Filename not found in environment')
    sys.exit(POSTPROCESS_ERROR)

# Code from EMail.py @ http://nzbget.sourceforge.net
#print('[INFO] Script successfully started')
#sys.stdout.flush()

fwp = os.environ['NZBNP_NZBNAME']

p = re.match( r'^.*?\[\[[ ]?(.*?)[ ]?\]\]', fwp)
f = re.sub( r'[ .]?[\[[ ]?(.*?)[ ]?\]\]', '', fwp)

if p:
   print('[NZB] CATEGORY=' + p.group(1))
   # Next line can be removed if wanted or set to [DETAIL] logging
   #print('[INFO] Password added to PP-Parameters')
   if f:
      print('[NZB] NZBNAME=' + f)
      # Next line can be removed if wanted or set to [DETAIL] logging
      #print('[INFO] ' + f)

sys.exit(POSTPROCESS_SUCCESS)
