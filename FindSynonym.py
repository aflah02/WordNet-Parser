import pandas as pd
from parsers.indexParser import *
from parsers.dataParser import *
from parsers.senseIndexParser import *

indexdfverb = createIndexDF(f'dict/index.verb')
indexdfadj = createIndexDF(f'dict/index.adj')
indexdfnoun = createIndexDF(f'dict/index.noun')
indexdfadv = createIndexDF(f'dict/index.adv')
indexdf = pd.concat([indexdfverb[['lemma', 'pos', 'synset_offset']], indexdfadj[['lemma', 'pos', 'synset_offset']], 
        indexdfnoun[['lemma', 'pos', 'synset_offset']], indexdfadv[['lemma', 'pos', 'synset_offset']]], ignore_index=True)

lemma_synset_map = {}
synset_lemma_map = {}
lemmas = indexdf['lemma'].to_list()
synsets = indexdf['synset_offset'].to_list()
for lemma, synset in zip(lemmas, synsets):
    for s in synset:
        if lemma not in lemma_synset_map.keys():
            lemma_synset_map[lemma] = []
        if s not in synset_lemma_map.keys():
            synset_lemma_map[s] = []
        lemma_synset_map[lemma].append(s)
        synset_lemma_map[s].append(lemma)

def list_synonyms(lemma, lemma_synset_map = lemma_synset_map, synset_lemma_map = synset_lemma_map):
    lemma = lemma.lower()
    synonyms = []
    synsets = lemma_synset_map[lemma]
    for synset in synsets:
        synonyms.extend(synset_lemma_map[synset])
    return list(set(synonyms))

if __name__ == '__main__':
    while True:
        lemma = input('Enter a lemma: ')
        if lemma == 'exit':
            break
        synonyms = list_synonyms(lemma)
        print(synonyms)