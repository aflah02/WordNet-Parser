import pandas as pd

def createIndexDF(filePath):
    with open(filePath) as f:
        Indexdump = f.readlines()
    indexLines = []
    for i in Indexdump:
        if i[0] == " " or i[0] == ".":
            continue
        else:
            indexLines.append(i.strip())
    for i in range(len(indexLines)):
        splitLine = indexLines[i].split()
        if (len(splitLine) == 8):
            indexLines[i] = splitLine
            continue
        ls = []
        ls.extend(splitLine[0:4])
        p_cnt = int(ls[-1])
        ls.append(splitLine[4:4 + p_cnt])
        sense_cntIndex = 4 + p_cnt
        ls.append(splitLine[sense_cntIndex])
        tagsense_cntIndex = sense_cntIndex + 1
        ls.append(splitLine[tagsense_cntIndex])
        remainingStartIndex = tagsense_cntIndex + 1
        ls.append(splitLine[remainingStartIndex:])
        indexLines[i] = ls
    df = pd.DataFrame(indexLines, columns = ['lemma', 'pos', 'synset_cnt', 'p_cnt', 'ptr_symbol', 'sense_cnt', 'tagsense_cnt', 'synset_offset'])
    return df