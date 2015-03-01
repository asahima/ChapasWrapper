#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
from node import NodeFactory

import re
import subprocess

class ChaPAS(object):
    def __init__(self, chapas_pass, options = "-I RAW"):
        self.chapas_pass = chapas_pass
        self.options = options
    
    def parse(self, target):
        cmd = "echo {} | java -jar {} {}".format(
                                             target,
                                             self.chapas_pass,
                                             self.options
                                             )
        output = subprocess.check_output(cmd, shell=True).split("\n")

        objs = []
        obj = []
        
        for line in output[:-1]:
            if line[0] == "*" and len(obj) > 0:
                objs.append(NodeFactory.new(obj[1:]))
                obj = []
                obj.append(re.split("\s+", line))
            elif line[0] == "*":
                obj.append(re.split("\s+", line))
            elif line == "EOS":
                objs.append(NodeFactory.new(obj[1:]))
                obj = []
            else:
                obj.append(re.split("\s+", line))

        return objs
