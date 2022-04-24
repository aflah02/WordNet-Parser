from FindSynonym import *

SuffixRulesForNouns = {
    's' : [''],
    'ses' : ['s'],
    'xes' : ['x'],
    "zes" : ["z"],
    "ches" : ["ch"],
    "shes" : ["sh"],
    "men" : ["man"],
    "ies": ["y"],
}

SuffixRulesForVerbs = {
    "s" : [""],
    "ies": ["y"],
    "es": ["e", ""],
    "ed": ["e", ""],
    "ing": ["e", ""]
}

SuffixRulesForAdjectives = {
    "er" : ["e",""],
    "est": ["e", ""],
}

adjExceptionPath = r'dict\adj.exc'
advExceptionPath = r'dict\adv.exc'
nounExceptionPath = r'dict\noun.exc'
verbExceptionPath = r'dict\verb.exc'

with open(adjExceptionPath) as f:
    adjException = f.read().splitlines()
adjExceptionDict = {}
for i in range(len(adjException)):
    adjException[i] = adjException[i].split(' ')
    if adjException[i][0] not in adjExceptionDict.keys():
        adjExceptionDict[adjException[i][0].replace('-', ' ')] = []
    adjExceptionDict[adjException[i][0].replace('-', ' ')].append(adjException[i][1].replace('-', ' '))

with open(advExceptionPath) as f:
    advException = f.read().splitlines()
advExceptionDict = {}
for i in range(len(advException)):
    advException[i] = advException[i].split(' ')
    if advException[i][0] not in advExceptionDict.keys():
        advExceptionDict[advException[i][0].replace('-', ' ')] = []
    advExceptionDict[advException[i][0].replace('-', ' ')].append(advException[i][1].replace('-', ' '))

with open(nounExceptionPath) as f:
    nounException = f.read().splitlines()
nounExceptionDict = {}
for i in range(len(nounException)):
    nounException[i] = nounException[i].split(' ')
    if nounException[i][0] not in nounExceptionDict.keys():
        nounExceptionDict[nounException[i][0]] = []
    nounExceptionDict[nounException[i][0]].append(nounException[i][1].replace('-', ' '))

with open(verbExceptionPath) as f:
    verbException = f.read().splitlines()
verbExceptionDict = {}
for i in range(len(verbException)):
    verbException[i] = verbException[i].split(' ')
    if verbException[i][0] not in verbExceptionDict.keys():
        verbExceptionDict[verbException[i][0].replace('-', ' ')] = []
    verbExceptionDict[verbException[i][0].replace('-', ' ')].append(verbException[i][1].replace('-', ' '))

def WordNetSynonymFinder(word, pos):
    word = word.lower()
    searchWord = word.replace(' ', '_')
    if list_synonyms(searchWord) != []:
        return list_synonyms(searchWord)
    candidateWord = []
    if pos == 'noun':
        if word.count(' ') > 0:
            ls_word = word.split(' ')
            for i in range(len(ls_word)):
                if ls_word[i] in nounExceptionDict.keys():
                    for replacement in nounExceptionDict[ls_word[i]]:
                        candidateWord.append(ls_word[:i] + [replacement] + ls_word[i+1:])
            for word in candidateWord:
                if list_synonyms('_'.join(word)) != []:
                    return list_synonyms('_'.join(word))
            candidateWord = []
            for i in range(len(ls_word)):
                for suffix, replacement in SuffixRulesForNouns.items():
                    if ls_word[i].endswith(suffix):
                        for replacementWord in replacement:
                            candidateWord.append(ls_word[:i] + [ls_word[i][:-len(suffix)] + replacementWord] + ls_word[i+1:])
            for word in candidateWord:
                if list_synonyms('_'.join(word)) != []:
                    return list_synonyms('_'.join(word))
        elif word.count('-') > 0:
            ls_word = word.split('-')
            for i in range(len(ls_word)):
                if ls_word[i] in nounExceptionDict.keys():
                    for replacement in nounExceptionDict[ls_word[i]]:
                        candidateWord.append(ls_word[:i] + [replacement] + ls_word[i+1:])
            for word in candidateWord:
                if list_synonyms('_'.join(word)) != []:
                    return list_synonyms('_'.join(word))
            candidateWord = []
            for i in range(len(ls_word)):
                for suffix, replacement in SuffixRulesForNouns.items():
                    if ls_word[i].endswith(suffix):
                        for replacementWord in replacement:
                            candidateWord.append(ls_word[:i] + [ls_word[i][:-len(suffix)] + replacementWord] + ls_word[i+1:])
            for word in candidateWord:
                if list_synonyms('_'.join(word)) != []:
                    return list_synonyms('_'.join(word))
        else:
            if word in nounExceptionDict.keys():
                for replacementWord in nounExceptionDict[word]:
                    candidateWord.append(replacementWord)
            for word in candidateWord:
                if list_synonyms(word):
                    return list_synonyms(word)
            candidateWord = []
            for suffix, replacement in SuffixRulesForNouns.items():
                if word.endswith(suffix):
                    for replacementWord in replacement:
                        candidateWord.append(word[:-len(suffix)] + replacementWord)
            for word in candidateWord:
                if list_synonyms(word):
                    return list_synonyms(word)
        candidateWord = []
    elif pos == 'verb':
        if word.count(' ') > 0:
            ls_word = word.split(' ')
            for i in range(len(ls_word)):
                if ls_word[i] in verbExceptionDict.keys():
                    for replacement in verbExceptionDict[ls_word[i]]:
                        candidateWord.append(ls_word[:i] + [replacement] + ls_word[i+1:])
            for word in candidateWord:
                if list_synonyms('_'.join(word)) != []:
                    return list_synonyms('_'.join(word))
            candidateWord = []
            for i in range(len(ls_word)):
                for suffix, replacement in SuffixRulesForVerbs.items():
                    if ls_word[i].endswith(suffix):
                        for replacementWord in replacement:
                            candidateWord.append(ls_word[:i] + [ls_word[i][:-len(suffix)] + replacementWord] + ls_word[i+1:])
            for word in candidateWord:
                if list_synonyms('_'.join(word)) != []:
                    return list_synonyms('_'.join(word))
        elif word.count('-') > 0:
            ls_word = word.split('-')
            for i in range(len(ls_word)):
                if ls_word[i] in verbExceptionDict.keys():
                    for replacement in verbExceptionDict[ls_word[i]]:
                        candidateWord.append(ls_word[:i] + [replacement] + ls_word[i+1:])
            for word in candidateWord:
                if list_synonyms('_'.join(word)) != []:
                    return list_synonyms('_'.join(word))
            candidateWord = []
            for i in range(len(ls_word)):
                for suffix, replacement in SuffixRulesForVerbs.items():
                    if ls_word[i].endswith(suffix):
                        for replacementWord in replacement:
                            candidateWord.append(ls_word[:i] + [ls_word[i][:-len(suffix)] + replacementWord] + ls_word[i+1:])
            for word in candidateWord:
                if list_synonyms('_'.join(word)) != []:
                    return list_synonyms('_'.join(word))
        else:
            if word in verbExceptionDict.keys():
                for replacementWord in verbExceptionDict[word]:
                    candidateWord.append(replacementWord)
            for word in candidateWord:
                if list_synonyms(word):
                    return list_synonyms(word)
            candidateWord = []
            for suffix, replacement in SuffixRulesForVerbs.items():
                if word.endswith(suffix):
                    for replacementWord in replacement:
                        candidateWord.append(word[:-len(suffix)] + replacementWord)
            for word in candidateWord:
                if list_synonyms(word):
                    return list_synonyms(word)
            candidateWord = []
    elif pos == 'adj':
        if word.count(' ') > 0:
            ls_word = word.split(' ')
            for i in range(len(ls_word)):
                if ls_word[i] in adjExceptionDict.keys():
                    for replacement in adjExceptionDict[ls_word[i]]:
                        candidateWord.append(ls_word[:i] + [replacement] + ls_word[i+1:])
            for word in candidateWord:
                if list_synonyms('_'.join(word)) != []:
                    return list_synonyms('_'.join(word))
            candidateWord = []
            for i in range(len(ls_word)):
                for suffix, replacement in SuffixRulesForAdjectives.items():
                    if ls_word[i].endswith(suffix):
                        for replacementWord in replacement:
                            candidateWord.append(ls_word[:i] + [ls_word[i][:-len(suffix)] + replacementWord] + ls_word[i+1:])
            for word in candidateWord:
                if list_synonyms('_'.join(word)) != []:
                    return list_synonyms('_'.join(word))
        elif word.count('-') > 0:
            ls_word = word.split('-')
            for i in range(len(ls_word)):
                if ls_word[i] in adjExceptionDict.keys():
                    for replacement in adjExceptionDict[ls_word[i]]:
                        candidateWord.append(ls_word[:i] + [replacement] + ls_word[i+1:])
            for word in candidateWord:
                if list_synonyms('_'.join(word)) != []:
                    return list_synonyms('_'.join(word))
            candidateWord = []
            for i in range(len(ls_word)):
                for suffix, replacement in SuffixRulesForAdjectives.items():
                    if ls_word[i].endswith(suffix):
                        for replacementWord in replacement:
                            candidateWord.append(ls_word[:i] + [ls_word[i][:-len(suffix)] + replacementWord] + ls_word[i+1:])
            for word in candidateWord:
                if list_synonyms('_'.join(word)) != []:
                    return list_synonyms('_'.join(word))
        else:
            if word in adjExceptionDict.keys():
                for replacementWord in adjExceptionDict[word]:
                    candidateWord.append(replacementWord)
            for word in candidateWord:
                if list_synonyms(word):
                    return list_synonyms(word)
            candidateWord = []
            for suffix, replacement in SuffixRulesForAdjectives.items():
                if word.endswith(suffix):
                    for replacementWord in replacement:
                        candidateWord.append(word[:-len(suffix)] + replacementWord)
            for word in candidateWord:
                if list_synonyms(word):
                    return list_synonyms(word)
            candidateWord = []
    elif pos == 'adv':
        if word.count(' ') > 0:
            ls_word = word.split(' ')
            for i in range(len(ls_word)):
                if ls_word[i] in advExceptionDict.keys():
                    for replacement in advExceptionDict[ls_word[i]]:
                        candidateWord.append(ls_word[:i] + [replacement] + ls_word[i+1:])
            for word in candidateWord:
                if list_synonyms('_'.join(word)) != []:
                    return list_synonyms('_'.join(word))
            candidateWord = []
        elif word.count('-') > 0:
            ls_word = word.split('-')
            for i in range(len(ls_word)):
                if ls_word[i] in advExceptionDict.keys():
                    for replacement in advExceptionDict[ls_word[i]]:
                        candidateWord.append(ls_word[:i] + [replacement] + ls_word[i+1:])
            for word in candidateWord:
                if list_synonyms('_'.join(word)) != []:
                    return list_synonyms('_'.join(word))
            candidateWord = []
        else:
            if word in advExceptionDict.keys():
                for replacementWord in advExceptionDict[word]:
                    candidateWord.append(replacementWord)
            for word in candidateWord:
                if list_synonyms(word):
                    return list_synonyms(word)
            candidateWord = []
    return "Not Found"
    
if __name__ == '__main__':
    while True:
        word = input("Enter a word (Enter Empty String to Exit): ")
        if word == '':
            break
        pos = input("Enter a part of speech: ")
        print(WordNetSynonymFinder(word, pos))
