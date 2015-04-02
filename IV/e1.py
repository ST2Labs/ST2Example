# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
e1.py - Example python coding from Hacking
Description: Run system command [ls -lsa]

Copyright 2015 Julian J. Gonzalez
www.st2labs.com | @ST2Labs | @rhodius | @seguridadxato2

This is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

This is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along it; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

www.seguridadparatodos.es > post about python hacking IV
"""
import subprocess

# Run a secure system commands

if __name__ == "__main__":

    command_line = 'ls -lsa'

    print 'Run Command %s' % command_line
    out_ = subprocess.check_output(command_line, shell=True)
    print out_