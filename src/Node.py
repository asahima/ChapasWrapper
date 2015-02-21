#!/usr/bin/env python
# coding: utf-8

class Node(object):
    def __init__(self):
        self.surface = ""
        self.pos = ""
        self._id = ""
        self.stype = ""
        self.o_case = ""
        self.ga_case = ""
        self.ni_case = ""
        self.read = ""
        self.default = ""

    def __str__(self):
        return "surface: {}, pos: {}, default: {}, type: {}, o: {}, ga: {}, id: {}".format(
            self.surface,
            self.pos,
            self.default,
            self.stype,
            self.o_case,
            self.ga_case,
            self._id
            )

class NodeFactory(object):

    @classmethod
    def new(cls, elems):
        nodes = []
        for elem in elems:
            nodes.append(cls.__set(elem))
        return nodes

    @classmethod
    def __set(cls, elem):
        node = Node()
        node.surface = elem[0]
        parse = elem[1].split(",")
        node.pos = parse[0]
        node.default = parse[6]
        
        if len(elem) > 2:
            cls.__check(elem, node)
        return node
    
    @classmethod
    def __check(cls, elem, node):
        stype  = cls.__type(elem, node)
        if stype != "":
            node.stype = stype

        ga_case = cls.__ga_case(elem, node)
        if ga_case != "":
            node.ga_case = ga_case

        o_case = cls.__o_case(elem, node)
        if o_case != "":
            node.o_case = o_case

        ni_case = cls.__ni_case(elem, node)
        if ni_case != "":
            node.ni_case = ni_case

        _id     = cls.__id(elem, node)
        if _id != "":
            node._id = _id

    @classmethod
    def __type(cls, elem, node):
        stype = ""
        if "type=" in elem[-1]:
            stype = elem[-1].replace("type=", "")
        elif "type=" in elem[-2]:
            stype = elem[-2].replace("type=", "")
        elif "type=" in elem[-3]:
            stype = elem[-3].replace("type=", "")
        elif "type=" in elem[-4]:
            stype = elem[-4].replace("type=", "")
        else:
            pass
        return stype

    @classmethod
    def __ga_case(cls, elem, node):
        ga_case = ""
        if "ga=" in elem[-1]:
            ga_case = cls.__format(elem, -1, "ga=")
        elif "ga=" in elem[-2]:
            ga_case = cls.__format(elem, -2, "ga=")
        elif "ga=" in elem[-3]:
            ga_case = cls.__format(elem, -3, "ga=")
        elif "ga=" in elem[-4]:
            ga_case = cls.__format(elem, -4, "ga=")
        else:
            pass
        return ga_case

    @classmethod
    def __o_case(cls, elem, node):
        o_case = ""
        if "o=" in elem[-1]:
            o_case = cls.__format(elem, -1, "o=")
        elif "o=" in elem[-2]:
            o_case = cls.__format(elem, -2, "o=")
        elif "wo=" in elem[-3]:
            o_case = cls.__format(elem, -3, "o=")
        elif "o=" in elem[-4]:
            o_case = cls.__format(elem, -4, "o=")
        else:
            pass
        return o_case

    @classmethod
    def __ni_case(cls, elem, node):
        ni_case = ""
        if "ni=" in elem[-1]:
            ni_case = cls.__format(elem, -1, "ni=")
        elif "ni=" in elem[-2]:
            ni_case = cls.__format(elem, -2, "ni=")
        elif "ni=" in elem[-3]:
            ni_case = cls.__format(elem, -3, "ni=")
        elif "ni=" in elem[-4]:
            ni_case = cls.__format(elem, -4, "ni=")
        else:
            pass
        return ni_case

    @classmethod
    def __id(cls, elem, node):
        _id = ""
        if "ID=" in elem[-1]:
            _id = cls.__format(elem, -1, "ID=")
        elif "ID=" in elem[-2]:
            _id = cls.__format(elem, -2, "ID=")
        elif "ID=" in elem[-3]:
            _id = cls.__format(elem, -3, "ID=")
        elif "ID=" in elem[-4]:
            _id = cls.__format(elem, -4, "ID=")
        else:
            pass
        return _id

    @classmethod
    def __format(cls, elem, index, target):
        return int(elem[index].replace(target, "").replace('\"', ""))

