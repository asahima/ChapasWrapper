# coding: utf-8

from __future__ import print_function

import re
import subprocess

from Node import NodeFactory

class Chapas(object):
    def __init__(self, chapas_pass):
        self.objs = []
        self.obj = []
        self.chapas_pass = chapas_pass

    def parse(self, target_file):
        cmd = "cat {} | java -jar {} -I RAW".format(target_file, self.chapas_pass)
        output = subprocess.check_output(cmd, shell=True).split("\n")
        
        for line in output[:-1]:
            if line[0] == "*" and len(self.obj) > 0:
                self.objs.append(NodeFactory.new(self.obj[1:]))
                self.obj = []
                self.obj.append(re.split("\s+", line))
            elif line[0] == "*":
                self.obj.append(re.split("\s+", line))
            elif line == "EOS":
                self.objs.append(NodeFactory.new(self.obj[1:]))
                self.obj = []
            else:
                self.obj.append(re.split("\s+", line))

    def result(self):
        for items in self.objs:
            for item in items:
                print(item)


