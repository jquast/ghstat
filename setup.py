#!/usr/bin/env python
from __future__ import print_function
import os
import setuptools
import setuptools.command.develop
import setuptools.command.test

here = os.path.dirname(__file__)

def main():
    import codecs
    setuptools.setup(
        name='ghstat',
        version='0.1.0',
        description=("Command-line application to get or set "
                     "github commit status."),
        long_description=open(
            os.path.join(here, 'README.rst'), 'r').read(),
        author='Jeff Quast',
        author_email='contact@jeffquast.com',
        license='MIT',
        scripts=['ghstat/ghstat.py'],
        url='https://github.com/jquast/ghstat',
        include_package_data=True,
        keywords=['github', 'client', 'ci', 'rest', 'bamboo',
                  'travis', 'jenkins', 'teamcity', 'command'
                  ],
        install_requires=['docopt', 'requests'],
    )

if __name__ == '__main__':
    main()
