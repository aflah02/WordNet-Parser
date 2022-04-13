import pandas as pd
from parsers.indexParser import *
from parsers.dataParser import *
from parsers.senseIndexParser import *

fileExtensions = ['verb', 'adj', 'noun', 'adv']

for extension in fileExtensions:
    indexdf = createIndexDF(f'dict/index.{extension}')
    if (extension == 'verb'):
        datadf = createDataDF(f'dict/data.{extension}', True)
    else:
        datadf = createDataDF(f'dict/data.{extension}')
    indexdf.to_csv(f'ParsedCSVs/index_{extension}.csv')
    datadf.to_csv(f'ParsedCSVs/data_{extension}.csv')

senseindexdf = createSenseIndexDF('dict/index.sense')
senseindexdf.to_csv('ParsedCSVs/senseIndex.csv')