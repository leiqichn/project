#/user/bin/python
# -*- coding: utf-8 -*-
"""This programe read the obo file to extract the is_a relationship and 
append the child to father, it also return a dict store the alt_id of
GOs if exists.
"""

import re
import sys
import pandas as pd

class GOInfo(object):
    def __init__(self):
        self.alt_go_dict = {} # format: {alt_go: this_go, ...}
        self.go_child_dict = {} # format: {this_go: set(child_goes), ...}
        self.goes = set() # all the goes

    def read_obo(self, obo_file):
        info = open(obo_file).read().strip().split('[Term]')
        return info

    def extract_relationship(self, info):
        pattern_this_go = re.compile(r'(?m)^id:\s+(\w+:\d+)')
        pattern_alt_goes = re.compile(r'(?m)^alt_id:\s(\w+:\d+)')
        pattern_is_a = re.compile(r'(?m)^is_a:\s(\w+:\d+)')
        for t in info:
            this_go, alt_goes, is_a = '', [], []
            res_this_go = pattern_this_go.search(t)
            if res_this_go:
                this_go = res_this_go.group(1)
                alt_goes = pattern_alt_goes.findall(t)
                is_a = pattern_is_a.findall(t)
                self.goes.add(this_go)
                for alt_go in alt_goes:
                    self.alt_go_dict[alt_go] = this_go
                for father_go in is_a:
                    try:
                        self.go_child_dict[father_go].add(this_go)
                    except KeyError as e:
                        self.go_child_dict[father_go] = set([this_go])
            else:
                continue

    def child_append(self):
        """Append the child go to all the father goes"""
        go_leaf_up_layer = {} # the layer up from the leaf
        go_leaf = self.goes - set(self.go_child_dict) # the leaf go does not have a child, so it no in the go_child_dict
        for go in go_leaf:
            go_leaf_up_layer[go] = 0
            self.go_child_dict[go] = set([go]) # if a go is a leaf, we assign itself to its child go
        go_left = self.goes - set(go_leaf_up_layer)
        loop = 0
        print(loop, len(self.goes))
        while go_left:
            loop += 1
            print(loop, len(go_left))
            for go in go_left:
                layer = 0
                try:
                    for child in self.go_child_dict[go]:
                        layer = max(layer, go_leaf_up_layer[child])
                except KeyError as e:
                    continue
                go_leaf_up_layer[go] = layer + 1
                childs = set()
                for child in self.go_child_dict[go]:
                    childs.add(child)
                    childs |= self.go_child_dict[child]
                self.go_child_dict[go] = childs
            go_left = self.goes - set(go_leaf_up_layer)


def go_child_fill(obo_file):
    go_info = GOInfo()
    obo_info = go_info.read_obo(obo_file)
    go_info.extract_relationship(obo_info)
    go_info.child_append()
    return go_info.go_child_dict, go_info.alt_go_dict


if __name__ == '__main__':
	go_child_dict, alt_go_dict = go_child_fill('/home/qilei/omics_final/go.obo')
    #assert('GO:2001314' in go_child_dict['GO:0009227'])
    #assert('GO:2001314' in go_child_dict['GO:0034655'])
    #assert('GO:2001314' in go_child_dict['GO:0008150']) # GO:0008150 is the BP root
    #assert('GO:2001314' not in go_child_dict['GO:0044421']) # GO:0044421 is the CC root
    #assert('GO:2001314' not in go_child_dict['GO:0003674']) # GO:0003674 is the MF root
#print(go_child_dict)
#    input_golist =open("/home/qilei/omics_final/go_term.list",'r')
	
#print(alt_go_dict)
	#Only select 30 BP in level1
#	level1=set()
#	mapfile=open('/home/qilei/omics_final/go_term.list')
#	with mapfile as f:
#		for line in f:
#			item=line.strip().split('\t')
#			level1.add(item[0])
#	level1_dict = {key: value for key, value in go_child_dict.items() if key in level1}
	#print(level1_dict)
#	out=open('data/anno_GO_clt/BP_level1.obo','w')
#	for key in level1_dict:
#		out.write(key+'\t')
#		out.write('\t'.join(level1_dict[key]))
#		out.write('\n')
#	out.close()

	#retrive specific BP to 30 general term
	fisher_res=open("/home/qilei/omics_final/temp/go_term.list",'r')
	fo=open('/home/qilei/omics_final/retrive_go.res','w') 
	for line in fisher_res.readlines():
		terms=line.strip().split('\t')
		for k,v in go_child_dict.items():
			if terms[0] in k:
				fo.write(str(terms[0])+'\t'+str(v))
				fo.write('\n')
	fo.close()
	

