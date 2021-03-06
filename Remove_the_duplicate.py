#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#@File    :   Remove_the_duplicate.py
#@Time    :   2021/03/06 14:27:36
#@Author  :   Lei Qi 
#@Version :   1.0
#@Desc    :   Remove the duplicate of PhenoTagger results

import os 

out_path_root = '/local/qilei/project/NER/PhenoTagger_filter/'

predict_dirs = os.listdir('/local/qilei/project/NER/PhenoTagger_predict/PhenoTagger/')
for dir_name in predict_dirs:
    if dir_name.startswith('predict_level'):
        predict_dir_deep = '/local/qilei/project/NER/PhenoTagger_predict/PhenoTagger/'+dir_name
        out_dir_deep = out_path_root+dir_name
        if os.path.exists(out_dir_deep):
            pass
        else:
            os.makedirs(out_dir_deep)
        predict_file_names = os.listdir(predict_dir_deep)
        for file_name in predict_file_names:
            predict_file_path = predict_dir_deep +'/'+file_name
            out_file_path = out_path_root+dir_name+'/'+file_name
            with open(predict_file_path,'r') as f1:
                phrase_pos_dict = {}
                header = []
                for line in f1:
                    line_list = line.strip().split("\t")
                    
                    if len(line_list) ==7:
                        entity_type = line_list[4]
                        #header = 
                        if entity_type == "Phenotype":
                            start_pos = line_list[1]
                            end_pos = line_list[2]
                            phrase = line_list[3]
                            phrase_pos_dict[phrase] = [start_pos,end_pos,line]
                    else:
                        if line =='\n':
                            pass
                        else:
                            header.append(line)
                
                for phrase1,(start_pos1,end_pos1,line1) in phrase_pos_dict.items():
                    is_not_any_set = True
                    with open(out_file_path,'w') as f2:
                        f2.write(''.join(header))
                        for phrase2,(start_pos2,end_pos2,line2) in phrase_pos_dict.items():
                            range1_set = {i for i in range(int(start_pos1),int(end_pos1)+1)}
                            range2_set = {j for j in range(int(start_pos2),int(end_pos2)+1)}
                            phrase1_set = set(phrase1.strip().split(" "))
                            phrase2_set = set(phrase2.strip().split(" "))
                            if phrase1 == phrase2:
                                continue
                            else:
                                if phrase1_set.issubset(phrase2_set):
                                    if range1_set.issubset(range2_set):
                                        is_not_any_set = False
                                        f2.write(line2)
                                elif phrase2_set.issubset(phrase1_set):
                                    if range2_set.issubset(range1_set):
                                        is_not_any_set = False
                                        f2.write(line1)
                                
                        if is_not_any_set:
                            f2.write(line1)









