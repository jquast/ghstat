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

Generate a personal access token, https://github.com/settings/applications,
enabling scope *repo:status* and *public_repo* or *private_repo*, respectively.

Use this token for the `--token` parameter.

Examples
--------

failing a build on github.com::

    ghstat.py set --token 0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d \
                  --commit 72b74be0de46392a05d8f470b64272b8036e63f8 \
                  --user jquast --repo ghstat --state success

retrieving the status of a commit::

   ghstat.py get --token 0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d \
                 --commit 72b74be0de46392a05d8f470b64272b8036e63f8 \
                 --user jquast --repo ghstat

linking to a private bamboo and github enterprise account::

    ghstat.py set --token 0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d0d \
                  --commit 0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a \
                  --user jquast \
                  --repo ghstat \
                  --state success \
                  --description 'build successful' \
                  --target-url 'https://bamboo.mycorp.com/browse/PROJ-BUILD10-1' \
                  --base-url 'https://github.mycorp.com/api/v3/'

Others
------

githubdate_: Same thing, only it uses an .ini file instead of cmd-line parameters.

Changes
-------

0.1.0
  * Initial release to pypi

.. _githubdate: https://github.com/brunobord/githubdate/
