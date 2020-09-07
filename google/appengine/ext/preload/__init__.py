#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#




"""Preloads many modules to reduce loading time of third-party code."""

















from future import standard_library
standard_library.install_aliases()
import os
_original_os_urandom = os.urandom
def os_urandom_replacement(n):
  raise NotImplementedError
os.urandom = os_urandom_replacement
import random



os.urandom = _original_os_urandom
random._urandom = _original_os_urandom


import six.moves.BaseHTTPServer
import Bastion
import six.moves.CGIHTTPServer
import six.moves.configparser
import six.moves.http_cookies
import xmlrpc.server
import six.moves.html_parser
import MimeWriter
import six.moves.queue
import six.moves.SimpleHTTPServer
import six.moves.xmlrpc_server
import six.moves.socketserver
import io
import UserDict
import collections
import collections
import aifc
import dbm.ndbm


import atexit
import audiodev
import base64
import bdb
import binhex
import bisect
import bz2

import calendar
import cgi
import cgitb
import chunk
import cmd
import code
import codecs
import codeop
import colorsys
import subprocess


import six.moves.http_cookiejar
import copy
import six.moves.copyreg
import csv
import datetime


import difflib
import dircache
import dis
import doctest
import dbm.dumb
import filecmp
import fileinput
import fnmatch
import formatter
import fpformat
import ftplib

import getopt
import getpass
import gettext
import glob

import gzip

import heapq
import hmac
import six.moves.html_entities
import htmllib
import six.moves.http_client

import imaplib
import imghdr
import imputil
import inspect
import keyword
import linecache
import locale
import logging
import macpath
import macurl2path
import mailbox
import mailcap
import _markupbase
import math
import md5
import mhlib
import mimetools
import mimetypes

import modulefinder
import multifile
import mutex
import netrc
import new
import nntplib
import ntpath
import nturl2path
import opcode
import optparse
import os2emxpath
import pdb
import pickle
import pickletools
import pipes
import pkgutil

import popen2
import poplib

import posixpath
import pprint
import profile
import pstats


import pyclbr
import pydoc
import quopri
import re
import six.moves.reprlib

import rfc822

import six.moves.urllib_robotparser

import sched
import sets
import sgmllib
import sha
import shelve
import shlex
import shutil
import site

import smtplib
import sndhdr
import socket




import stat
import statvfs
import string
import stringold
import stringprep
import struct

import sunau
import sunaudio
import symbol

import sys
import tabnanny
import tarfile
import telnetlib
import tempfile
import textwrap

import time
import timeit
import toaiff
import token
import tokenize
import trace
import traceback

import types
import unittest
import six.moves.urllib.request, six.moves.urllib.parse, six.moves.urllib.error
import six.moves.urllib.request, six.moves.urllib.error, six.moves.urllib.parse
import six.moves.urllib.parse

import uu
import uuid
import warnings
import wave
import weakref

import dbm.ndbm
import xdrlib
import xml.parsers.expat
import xml.dom
import xml.sax

import six.moves.xmlrpc_client
import zipfile
import zlib



import neo_cs
import neo_util
import webob
import wsgiref.handlers


from google.appengine.api import datastore
from google.appengine.api import files
from google.appengine.api import images
from google.appengine.api import mail
from google.appengine.api import memcache
from google.appengine.api import runtime
from google.appengine.api import taskqueue
from google.appengine.api import urlfetch
from google.appengine.api import users


from google.appengine.ext import bulkload
from google.appengine.ext import db
from google.appengine.ext import gql
from google.appengine.ext import search
from google.appengine.ext import webapp


from google.appengine.runtime import apiproxy

if __name__ == '__main__':
  pass
