import os
from setuptools import setup, find_packages

# :==> Fill in your project data here
version = '0.0.5'
library_name = 'dt-mooc'
library_webpage = 'https://github.com/duckietown/lib-dt-mooc'
maintainer = 'Andrea F. Daniele'
maintainer_email = 'afdaniele@ttic.edu'
short_description = 'Python library for the "Self-Driving Cars with Duckietown" course on edX'
full_description = """
Python library to support student activities in the "Self-Driving Cars with Duckietown" 
course on edX. 
"""
# <==: Fill in your project data here

# read project dependencies
dependencies_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dependencies.txt')
with open(dependencies_file, 'rt') as fin:
    dependencies = list(filter(lambda line: not line.startswith('#'), fin.read().splitlines()))

# compile description
underline = '=' * (len(library_name) + len(short_description) + 2)
description = """
{name}: {short}
{underline}

{long}
""".format(name=library_name, short=short_description, long=full_description, underline=underline)

# setup package
setup(name=library_name,
      author=maintainer,
      author_email=maintainer_email,
      url=library_webpage,
      install_requires=dependencies,
      package_dir={"": "include"},
      packages=find_packages('./include'),
      long_description=description,
      version=version,
      include_package_data=True)
