#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : cli.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 04/23/2018
#
# This file is part of Jacinle.
# Distributed under terms of the MIT license.

import os
import os.path as osp
import sys

import jac.jacinle.io as io
from jac.jacinle.cli.git import git_revision_hash

__alL__ = ['escape_desc_name', 'ensure_path', 'dump_metainfo']


def escape_desc_name(filename):
    basename = osp.basename(filename)
    if basename.endswith('.py'):
        basename = basename[:-3]
    name = basename.replace('.', '_')
    return name


def ensure_path(path):
    if not osp.exists(path):
        print('Creating directory: "{}".'.format(path))
        os.makedirs(path, exist_ok=True)
    return path


def dump_metainfo(metainfo=None, **kwargs):
    if metainfo is None:
        metainfo = {}
    metainfo.update(kwargs)
    metainfo.setdefault('_cmd', ' '.join(sys.argv))
    metainfo.setdefault('_git', git_revision_hash())
    return io.dumps_json(metainfo, compressed=False)

