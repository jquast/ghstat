.. image:: https://img.shields.io/pypi/v/ghstat.svg
    :alt: Latest Version

.. image:: https://pypip.in/license/ghstat/badge.svg
    :alt: License

.. image:: https://img.shields.io/pypi/dm/ghstat.svg
    :alt: Downloads


============
Introduction
============

This command-line application is mainly for continuous build and
integration environments.  It allows one to set provide all of the
details necessary to mark a commit, for pull requests, to read
"All is Well" or "Merge with Caution" with an optional hyperlink
to the CI build server, or description of build failure.

This is done using the Github v3 API.

This is not a very serious package, there are not any plans to advance
it further. It was authored because existing github python client
packages such as *pygithub3* did not offer the ability to communicate
with the 'statuses' api endpoints, and it is preferred to provide
well-readable command-line arguments in the build script than to use
curl directly.

Installation
------------

The stable version of this package is maintained on pypi, install using pip::

    pip install ghstat

Examples
--------

linking to a private bamboo and github enterprise account::
    ghstdt set --token 0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d \
               --commit 0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a \
               --user jquast \
               --repo ghstat \
               --state success \
               --description 'build successful' \
               --target-url 'https://bamboo.mycorp.com/browse/PROJ-BUILD10-1' \
               --base-url 'https://github.mycorp.com/api/v3/'

failing a free account build on github::
    ghstat set --token 0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d \
               --commit 0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a \
               --user jquast \
               --repo ghstat \
               --state failure \
               --description '10 Unit Tests failed'

retrieving the status of a commit::

   XXX


License
-------

::

    The MIT License (MIT)

    Copyright (c) 2014 <contact@jeffquast.com>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.

Changes
-------

0.1.0
  * Initial release to pypi
