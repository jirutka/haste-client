CLI Haste client ![pypi](http://badge.fury.io/py/haste-client.png)
================

A simple client for [Haste server](https://github.com/seejohnrun/haste-server) written in Python.


## Installation

Use pip or easy_install:

    pip install haste-client

Haste client needs Python 2.6+ or 3.x (it was tested on 2.7 and 3.3) and following modules:

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
