#/user/bin/python
import sys
import re
from sys import  argv
def merge():
    ID2GO=open(argv[1],'r')
    out=open(argv[2],'w')
    GO_dict=dict()
    #str1=''
    #str2=''
    num=1
    geneID_this_raw='A0A021WW32'
    #GO_dict[geneID]=set()
    for line in ID2GO:
        terms=line.strip().split('\t')
        geneID=terms[0] #是gene ID
        #print(geneID)
        #GO_dict[geneID]=set()
        GOs=terms[1].strip().split(';')
        #print(GOs)
        #GO_dict[geneID]=set()
        if geneID_this_raw==geneID:
            if num==1:
                GO_dict[geneID]=set()
                for GO in GOs:
                    GO_dict[geneID].add(GO)
                    #out.write(str(geneID)+'\t'+str(GO_dict[geneID]))
            else:
                for GO in GOs:
                    GO_dict[geneID].add(GO)
                    #out.write(str(geneID)+'\t'+str(GO_dict[geneID])+'\n')
        else:
            #out.write(str(geneID)+'\t'+str(GO_dict[geneID])+'\n')

            GO_dict[geneID]=set()
            for GO in GOs:
                GO_dict[geneID].add(GO)

            #out.write(str(geneID)+'\t'+str(GO_dict[geneID])+'\n')
        geneID_this_raw=terms[0]
        num+=1
       # out.write(str(geneID)+'\t'+str(GO_dict[geneID]))
       # out.write('\n')
#    print(GO_dict)
    #for line in ID2GO:
        #terms=line.strip().split('\t')
    for k,v in GO_dict.items():
            #if terms[0] in k:
        out.write(str(k)+'\t'+str(v))
        out.write('\n')
        #print(str(k)+'\t'+str(v))
merge()

