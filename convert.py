#open the file
f = open("in.txt", "r", encoding="utf-8")
import json

for line in f:
    split = line.split("\t")
    id = split[0]
    document = split[1]
    datetime = split[2]
    text = split[3]
    o = open("json/" + document+ ".txt", "w", encoding="utf-8")
    #get json from text
    jsonObject = json.loads(text)
    o.write(text)
    #for block in jsonObject["blocks"]:
    #    o.write(block["text"])
    #    o.write("\n")
    o.close()