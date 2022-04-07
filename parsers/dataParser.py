import pandas as pd
def createDataDF(filePath, Isverb=False):
    with open(filePath) as f:
        Datadump = f.readlines()
    dataLines = []
    for i in Datadump:
        if i[0] == " " or i[0] == ".":
            continue
        else:
            dataLines.append(i.strip())
    for i in range(len(dataLines)):
        splitLine = dataLines[i].split()
        ls = []
        ls.extend(splitLine[:4])
        wordCount = int(ls[-1], 16)
        currIndex = 4
        ls_words_and_lexids = []
        for j in range(wordCount):
            ls_words_and_lexids.append([splitLine[currIndex],splitLine[currIndex+1]])
            currIndex += 2
        ls.append(ls_words_and_lexids)
        p_cnt = splitLine[currIndex]
        ls.append(p_cnt)
        currIndex += 1
        ptrList = []
        for j in range(int(p_cnt)):
            ptrList.append([splitLine[currIndex],splitLine[currIndex+1],splitLine[currIndex+2],splitLine[currIndex+3]])
            currIndex += 4
        ls.append(ptrList)
        if (Isverb):
            f_cnt = int(splitLine[currIndex])
            currIndex += 2
            ls.append(f_cnt)
            ls_fnum_wnum = []
            for j in range(f_cnt):
                ls_fnum_wnum.append([splitLine[currIndex],splitLine[currIndex+1]])
                currIndex += 3
            ls.append(ls_fnum_wnum)
        ls.append(" ".join(splitLine[currIndex:]))
        dataLines[i] = ls
    if (Isverb):
        df = pd.DataFrame(dataLines, columns = ['synset_offset', 'lex_filenum', 'ss_type', 'w_cnt', 'word with lex_id', 'p_cnt', 'ptr', 'f_cnt', 'frame', 'gloss'])
    else:
        df = pd.DataFrame(dataLines, columns = ['synset_offset', 'lex_filenum', 'ss_type', 'w_cnt', 'word with lex_id', 'p_cnt', 'ptr', 'gloss'])
    return df