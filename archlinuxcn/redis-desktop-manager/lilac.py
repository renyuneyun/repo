# Trimmed lilac.py
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *



def pre_build():
    aur_pre_build()
    add_makedepends(["python2"])



