# -*- coding: utf-8 -*-
#*****************************************************************************
#       Copyright (C) 2006  Michael Graz. <mgraz@plan10.com>
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#*****************************************************************************
from pyreadline.modes.emacs import *
from pyreadline import keysyms
from pyreadline.lineeditor import lineobj

class MockReadline:
    def __init__ (self):
        self.l_buffer=lineobj.ReadLineTextBuffer("")
        self._history=history.LineHistory()

    def add_history (self, line):
        self._history.add_history (lineobj.TextLine (line))

    def _print_prompt (self):
        pass

    def _bell (self):
        pass

    def insert_text(self, string):
        '''Insert text into the command line.'''
        self.l_buffer.insert_text(string)


class MockConsole:
    def __init__ (self):
        self.bell_count = 0
        self.text = ''

    def size (self):
        return (1, 1)

    def cursor(self, visible=None, size=None):
        pass

    def bell (self):
        self.bell_count += 1

    def write (self, text):
        self.text += text




class Event:
    def __init__ (self, char):
        self.char = char

def keytext_to_keyinfo_and_event (keytext):
    keyinfo = keysyms.key_text_to_keyinfo (keytext)
    if len(keytext) == 3 and keytext[0] == '"' and keytext[2] == '"':
        event = Event (keytext[1])
    else:
        event = Event (chr (keyinfo [3]))
    return keyinfo, event

