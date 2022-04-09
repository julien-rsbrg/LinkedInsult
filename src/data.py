categories = ['toxic', 'severe_toxic', 'obscene',
              'threat', 'insult', 'identity_hate']

# Format de dico_insultes (pas encore codé):
# dico_insultes = {'insulte1':[categorie,violence],
#                  'insulte2':[categorie,violence],
#                   ...                           }

dico_insultes = {'bigot': ['toxic', 3],
                 "commie": ['identity_hate', 2],
                 "coward": ['toxic', 5],
                 "douche": ['insult', 5],
                 "fool": ['toxic', 3],
                 "hippie": ['identity_hate', 1],
                 "idiot": ['severe_toxic', 6],
                 "jackass": ['severe_toxic', 6],
                 "loon": ['insult', 3],
                 "loser": ['severe_toxic', 5],
                 "moron": ['severe_toxic', 5],
                 "nutjob": ['toxic', 4],
                 "racist": ['insult', 3],
                 "scum": ['insult', 5],
                 "thug": ['insult', 2],
                 "poof": ['toxic', 4],
                 "fag": ['severe_toxic', 9],
                 "faggot": ['severe_toxic', 9],
                 "dyke": ['severe_toxic', 8],
                 "motherfucker": ['obscene', 6],
                 "bitch": ['obscene', 8],
                 "son of a bitch": ['obscene', 9],
                 "bastard": ['insult', 8],
                 "fucking": ['obscene', 8]}
