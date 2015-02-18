#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import re
import subprocess

from Node import NodeFactory

class ChaPAS(object):
    def __init__(self, chapas_pass):
        self.chapas_pass = chapas_pass

    def parse(self, target, ptype):
        assert self.__is_valid_cmd(ptype)
        ptype = "cat" if ptype == "file" else "echo"
        cmd = "{} {} | java -jar {} -I RAW".format(ptype, target, self.chapas_pass)
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

    def __is_valid_cmd(self, cmd):
        return True if cmd == "file" or cmd == "text" else False
