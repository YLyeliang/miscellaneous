import json
import math

results=[]
with open("D:/层高提取解析/15-13#图纸-2-拆分后图纸13#.json",'r',encoding='utf-8') as f:
    load_dict=json.load(f)
    tables=load_dict['tables'][0]
    texts=tables['texts']
    texts.insert(6,{"text":'-1(夹层)'})
    for i in range(math.ceil(len(texts)/3)):
        texts_=texts[3*i:3*i+3]
        result=[]
        for j in range(len(texts_)):
            text=texts_[j]['text']
            result.append(text)
        if len(result) <3:
            for _ in range(3-len(result)):
                result.append('')
        results.append(result)

print(results)
with open("D:/层高提取解析/15-13.txt",'w') as f:
    for i in results:
        f.write(i[0]+" "+i[1]+' '+i[2]+'\n')


debug=1

