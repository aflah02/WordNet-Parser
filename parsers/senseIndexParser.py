import pandas as pd

def createSenseIndexDF(filePath):
    with open(filePath) as f:
        senseIndexDump = f.readlines()
    senseIndexLines = []
    for i in senseIndexDump:
        if i[0] == "." or i[0] == "'":
            continue
        senseIndexLines.append(i.split())
    df = pd.DataFrame(senseIndexLines, columns = ['sense_key', 'synset_offset', 'sense_number', 'tag_cnt'])
    return df