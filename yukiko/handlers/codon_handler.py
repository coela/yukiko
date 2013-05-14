#-*- coding:utf-8 -*-

import re

bases = ['T', 'C', 'A', 'G']
codons = [a + b + c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

def _tokenize(sequence):
    for i in range(0, len(sequence), 3):
        try:
            yield sequence[i:i+3]
        except:
            yield None

def translate(sequence):
    aa_sequence = ''
    for codon in _tokenize(sequence):
        if codon == None: 
            return None
        try:
            aa_sequence += codon_table[codon]
        except:
            return None
    return aa_sequence

def handle(msg, event):
    if event == u"RECEIVED":
        if re.match(u'\#TRANSLATE', msg.Body):
            sequence = msg.Body.split(' ')[1].rstrip()
            aa_sequence = translate(sequence)
            if aa_sequence == None:
                msg.Chat.SendMessage(u'TRANSLATION FAILED.')
            else:
                msg.Chat.SendMessage(aa_sequence)
