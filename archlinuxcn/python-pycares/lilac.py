# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

#build_prefix = 'extra-x86_64'

def pre_build():
  pypi_pre_build(depends=['c-ares'], arch=('x86_64', 'i686'))

def post_build():
  pypi_post_build()

#if __name__ == '__main__':
#  single_main()
