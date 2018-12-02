# coding: utf-8


with open('xyj.txt', 'r') as fr:
    l = ['　', ' ', '、', '\t', '\n', '。', '.', '，', ',', '（', '）', '；', '“', '”', '......', '？', '！', '：', '(', ')', '/', '\\', '?']
    stat = {}
    lines = fr.readlines()
    for line in lines:
        for word in line:
            if word in stat.keys():
                stat[word] += 1
            else:
                if word not in l:
                    stat[word] = 1
    print("一共出现了%d个汉字"%len(stat))

stat = sorted(stat.items(), key=lambda d:d[1], reverse=True)

with open('total_word.csv', 'w') as fw:
    for i in stat:
        fw.write(i[0] + ',' + str(i[1]) + '\n')



        
