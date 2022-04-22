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
        adjExceptionDict[adjException[i][0]] = []
    adjExceptionDict[adjException[i][0]].append(adjException[i][1].replace('-', ' '))

with open(advExceptionPath) as f:
    advException = f.read().splitlines()
advExceptionDict = {}
for i in range(len(advException)):
    advException[i] = advException[i].split(' ')
    if advException[i][0] not in advExceptionDict.keys():
        advExceptionDict[advException[i][0]] = []
    advExceptionDict[advException[i][0]].append(advException[i][1].replace('-', ' '))

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
        verbExceptionDict[verbException[i][0]] = []
    verbExceptionDict[verbException[i][0]].append(verbException[i][1].replace('-', ' '))

def WordNetLemmatizer(word, pos):
    candidateWord = []
    if pos == 'noun':
        for suffix, replacement in SuffixRulesForNouns.items():
            if word.endswith(suffix):
                for replacementWord in replacement:
                    candidateWord.append(word[:-len(suffix)] + replacementWord)
        if word in nounExceptionDict.keys():
            for replacementWord in nounExceptionDict[word]:
                candidateWord.append(replacementWord)
    elif pos == 'verb':
        for suffix, replacement in SuffixRulesForVerbs.items():
            if word.endswith(suffix):
                for replacementWord in replacement:
                    candidateWord.append(word[:-len(suffix)] + replacementWord)
        if word in verbExceptionDict.keys():
            for replacementWord in verbExceptionDict[word]:
                candidateWord.append(replacementWord)
    elif pos == 'adj':
        for suffix, replacement in SuffixRulesForAdjectives.items():
            if word.endswith(suffix):
                for replacementWord in replacement:
                    candidateWord.append(word[:-len(suffix)] + replacementWord)
        if word in adjExceptionDict.keys():
            for replacementWord in adjExceptionDict[word]:
                candidateWord.append(replacementWord)
    elif pos == 'adv':
        if word in advExceptionDict.keys():
            for replacementWord in advExceptionDict[word]:
                candidateWord.append(replacementWord)
    
