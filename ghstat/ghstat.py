#!/usr/bin/env python
"""
Sets github status of commit-id by given command-line parameters.

Used by CI to report into a pull request.

Usage:
  gh-status.py set (-u <user>   | --user=<user>)
                   (-r <repo>   | --repo=<repo>)
                   (-c <sha>    | --commit=<sha>)
                   (-s <state>  | --state=<failure|success|pending>)
                   [(-t <token> | --token=<token>)]
                   [(-d <desc>  | --description=<desc>)]
                   [(-l <url>   | --target-url=<url>)]
                   [(-b <url>   | --base-url=<url>)]
  gh-status.py get (-u <user>   | --user=<user>)
                   (-r <repo>   | --repo=<repo>)
                   (-c <sha>    | --commit=<sha>)
                   [(-t <token> | --token=<token>)]
                   [(-b <url>   | --base-url=<url>)]
  gh-status.py -h | --help

Options:
  -h --help               Display program usage.
  -t --token=<token>      Github api authorization token.
  -u --user=<user>        Repository owner name.
  -r --repo=<repo>        Repository name.
  -c --commit=<sha>       Git sha commit-id.
  -s --state=<state>      Build status, one of: failure, success, pending.
  -d --description=<desc> Description when setting commit status.
  -b --base-url=<url>     Api base url [default: https://api.github.com/].
  -l --target-url=<url>   Build status referral url.
"""
from __future__ import print_function

# std imports
try:
    # python2
    from urlparse import urlparse
except ImportError:
    # pylint: disable=E0611
    #         No name 'parse' in module 'urlib'
    # python3
    from urllib.parse import urlparse
import json
import os
import sys

# 3rd-party
from docopt import docopt
import requests


def validate_args(args):
    # validate --token or GITHUB_APP_TOKEN,
    args['--token'] = os.getenv('GITHUB_APP_TOKEN',
                                args.get('--token'))
    assert args['--token'], (
        'A github application token should be supplied as either cmd-line '
        'parameter --token or OS Environment key GITHUB_APP_TOKEN')

    # validate --base-url,
    uri = urlparse(args['--base-url'])
    assert uri.scheme in ('http', 'https',), args['--base-url']

    # validate --target-url,
    if args['--target-url']:
        uri = urlparse(args['--target-url'])
        assert uri.scheme in ('http', 'https',), args['--target-url']

    # coerce: remove trailing '/' from --base-url
    if args['--base-url'].endswith('/'):
        args['--base-url'] = args['--base-url'].rstrip('/')

    # validate --commit,
    int(args['--commit'], 16)

    # validate --state,
    if args['set']:
        state = args['--state']
        assert state in ('failure', 'success', 'pending'), args['--state']

    # validate --description,
    if '--description' in args and len(args['--description']) > 140:
        sys.stderr.write('warning: length of --description is length {0}, '
                         'but maximum allowed length is 140.  '
                         'It will be truncated.\n'
                         .format(len(args['--description'])))
        marker = ' (...)'
        trimmed = slice(0, 140 - len(marker))
        args['--description'] = args['--description'][trimmed]

    # doctopt already handles --help, remove
    del args['--help']

    # remove all the prefixing '--', change base-url -> base_url
    return dict((key.lstrip('-').replace('-', '_'), value)
                for key, value in args.items())


def main(args):
    url = ('{args[base_url]}/repos/'
           '{args[user]}/'
           '{args[repo]}/statuses/'
           '{args[commit]}'.format(args=args))

    headers = {'Authorization': 'token {args[token]}'.format(args=args)}

    if args['set']:
        data = json.dumps({
            'state': args['state'],
            'description': args['description'] or '',
            'target_url': args['target_url'] or ''})
        resp = requests.post(url=url, data=data, headers=headers)
        assert resp.status_code == 201, (resp.status_code, resp.text)

    elif args['get']:
        resp = requests.get(url=url, headers=headers)
        assert resp.status_code == 200, (resp.status_code, resp.text)
        # the first item of the array is the most recent.
        first = resp.json()[:1]
        print(json.dumps(first, indent=2))
    return 0

if __name__ == '__main__':
    exit(main(validate_args(docopt(__doc__))))
