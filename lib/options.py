 #!/usr/bin/python
# -*- coding: utf-8 -*-
"""options"""
import argparse


parser = argparse.ArgumentParser(description='Mixtape Application')
parser.add_argument('input', metavar='Input', type=str, nargs='+', help='Input JSON file consists of a set of users, songs, and playlists that are part of a music service')
parser.add_argument('changefile', metavar='Changefile', type=str, nargs='+', help='JSON file consists all desired changes')
parser.add_argument('output', metavar='Output', type=str, nargs='+',help='File name for a JSON file consists of changes provided in changefile.')


class Options(object):
    """options class"""
    def __new__(cls):
        args = vars(parser.parse_args())
        return args