#!/usr/bin/env python

"""
haste - a CLI client for Haste server.

Usage:
    haste [-r] [-]
    haste [-r] FILE

-             read from stdin.
FILE          read from a file.

-h --help     show this message.
-v --version  show version information.
-r --raw      return a URL to the raw paste data.
"""

import json
import requests
from docopt import docopt
from os.path import expanduser
from requests.exceptions import Timeout
from sys import stdout, stdin, exit

CONFIGS = [expanduser('~/.hastec'), '/etc/hastec.conf']
DEFAULTS = {
    'server_url': "http://hastebin.com",
    'timeout': 3
}

kwargs = docopt(__doc__, version='haste 1.0')


def run(**kwargs):
    config = load_config()
    filesrc = kwargs['FILE'] and kwargs['FILE'] != '-'
    data = read_file(kwargs['FILE']) if filesrc else read_stdin()
    url = create_snippet(data, config['server_url'], config['timeout'], kwargs['--raw'])
    stdout.write(url + '\n')


def create_snippet(data, baseurl, timeout, raw):
    """
    Creates snippet with the given data on the haste server specified by the
    baseurl and returns URL of the created snippet.
    """
    try:
        response = requests.post(baseurl + "/documents", data, timeout=timeout)
    except Timeout:
        exit("Error: connection timed out")

    dockey = json.loads(response.text)['key']
    return baseurl + ("/raw/" if raw else "/") + dockey


def read_stdin():
    return "".join(stdin.readlines()).strip()


def read_file(path):
    try:
        with open(path, 'r') as f:
            return "".join(f.readlines()).strip()
    except:
        exit("Error: file '%s' is not readable!" % path)


def load_config():
    """
    Loads configuration from the first readable file specified by the CONFIGS
    list and merges it with DEFAULTS. If any of the files is not readable, then
    it simply returns DEFAULTS.
    """
    config = {}
    for path in CONFIGS:
        try:
            config = parse_config(path)
            break
        except: pass

    # merge and override tuples from DEFAULTS by config
    return dict(DEFAULTS, **config)


def parse_config(path):
    """
    Parses key=value pairs from the given file and returns them as dict.
    Lines that starts with '#' (leading whitespaces are stripped) or doesn't
    contain '=' are ignored. Whitespaces around keys and values are stripped.
    """
    with open(path, 'r') as f:
        return { k.strip(): v.strip()
                for k, v in (
                    line.split('=', 1) for line in f
                    if '=' in line and line.strip()[:1] != '#') }


def main():
    run(**kwargs)


if __name__ == "__main__":
    run(**kwargs)
