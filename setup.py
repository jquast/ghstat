#!/usr/bin/env python
from __future__ import print_function
import os
import setuptools
import setuptools.command.develop
import setuptools.command.test

here = os.path.dirname(__file__)


def main():
    setuptools.setup(
        name='ghstat',
        version='0.3.0',
        description=("Command-line application to get or set "
                     "github commit status."),
        long_description=open(
            os.path.join(here, 'README.rst'), 'r').read(),
        author='Jeff Quast',
        author_email='contact@jeffquast.com',
        license='MIT',
        zip_safe=True,
        scripts=['ghstat/ghstat.py'],
        url='https://github.com/jquast/ghstat',
        include_package_data=True,
        keywords=['github', 'status', 'api', 'json', 'client',
                  'ci', 'rest', 'bamboo', 'travis', 'jenkins',
                  'teamcity', 'command'
                  ],
        install_requires=['docopt', 'requests'],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Topic :: Software Development :: Build Tools',
            'Topic :: Software Development :: Quality Assurance',
            'Topic :: Utilities',
        ]
    )

if __name__ == '__main__':
    main()
