"""Convert electronic medical record text to PubTator format and run PhenoTagger """

import os

dirs = os.listdir('/home/qilei/eval/data')
for dir_name in dirs:
    if str(dir_name).startswith('level') or str(dir_name).startswith('phrase'):
        #path = '/local/fyh/NER/project/data/GSC+/corpus'
        #path = '/local/fyh/NER/project/data/68_clinical/corpus'
        path = '/home/qilei/eval/data/'+dir_name+'/corpus'
        #out_path = '/local/fyh/NER/project/other_methods/PhenoTagger/test/GSC+'
        #out_path = '/local/fyh/NER/project/other_methods/PhenoTagger/test/68_clinical'
        out_path = '/home/qilei/eval/PhenoTagger/test/'+dir_name+'/'
        if os.path.exists(out_path):
            pass
        else:
            os.makedirs(out_path)
        files= os.listdir(path)
        count = 0
        for file_name in files:
            str1 = f"{count}|t|\n{count}|a|"
            with open(path+'/'+file_name,'r') as f1:
                for line in f1:
                    str1 = str1 + line +"\n"
                str1 = str1+"\n"
            with open(out_path+'/'+file_name,'w', encoding = "utf-8") as f2:
                f2.write(str1)
            count += 1
        predict_path = '/home/qilei/eval/PhenoTagger/val/predict_'+ dir_name+'/'
        if os.path.exists(predict_path):
            pass
        else:
            os.makedirs(predict_path)
        os.system('. /home/qilei/tools/phenotagger/bin/activate')
        stdo = os.system('python /home/qilei/eval/PhenoTagger/src/PhenoTagger_tagging.py -i {} -o {}'.format(out_path,predict_path))
        print(stdo)