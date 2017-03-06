CLI Haste client
================
[![version](https://img.shields.io/pypi/v/haste-client.svg?style=flat)](https://pypi.python.org/pypi/haste-client)

A simple client for [Haste server](https://github.com/jirutka/haste-server) written in Python.


## Installation

Use pip or easy_install:

    pip install haste-client

Gentoo users can use [haste-client](https://github.com/cvut/gentoo-overlay/tree/master/www-apps/haste-client) ebuild from [CVUT Overlay](https://github.com/cvut/gentoo-overlay).

Haste client needs Python 2.6+ or 3.x (it was tested on 2.7, 3.3 and 3.4) and following modules:

*  [requests](https://github.com/kennethreitz/requests)
*  [docopt](https://github.com/docopt/docopt) >= 0.3.0


## Usage

Text can be passed to `haste` via stdin or a file. TTY is also supported.

    haste FILE
    cat FILE | haste

URL of the created entry is then printed to STDOUT.


## Configuration

Haste client reads configuration variables from `~/.hastec` and `/etc/hastec.conf` (in this order, first wins). When no such file or the particular variable exists, then default values are used:

    server_url = http://hastebin.com
    timeout = 3


## License

This project is licensed under [MIT license](http://opensource.org/licenses/MIT).
