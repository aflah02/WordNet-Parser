## Custom Parser for WordNet

Design Choice for Synonym Parsing:

    - Pointers Considered for Noun Synonym are: 
      - + Derivationally related form
      - ;c Domain of synset - TOPIC
      - -c Member of this domain - TOPIC 
      - ;r Domain of synset - REGION 
      - -r Member of this domain - REGION 
      - ;u Domain of synset - USAGE 
      - -u Member of this domain - USAGE 
    - Pointers Considered for Verb Synonym are:
      - + Derivationally related form
      - ;c Domain of synset - TOPIC 
      - ;r Domain of synset - REGION 
      - ;u Domain of synset - USAGE 
    - Pointers Considered for Adjective Synonym are:
      - & Similar to
      - \ Pertainym (pertains to noun)
      - ;c Domain of synset - TOPIC 
      - ;r Domain of synset - REGION 
      - ;u Domain of synset - USAGE 
    - Pointers Considered for Adverb Synonym are:
      - ;c Domain of synset - TOPIC 
      - ;r Domain of synset - REGION 
      - ;u Domain of synset - USAGE 


To download database files run:

`wget http://wordnetcode.princeton.edu/3.0/WNdb-3.0.tar.gz`

To extract database files run:

`tar -xf WNdb-3.0.tar.gz`

Data Source - 
- https://wordnet.princeton.edu/download/current-version

Data Format Sources - 
- https://wordnet.princeton.edu/documentation/wndb5wn 
- https://wordnet.princeton.edu/documentation/senseidx5wn
