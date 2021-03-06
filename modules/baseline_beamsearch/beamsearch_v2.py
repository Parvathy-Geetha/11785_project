import torch
import numpy as np
from torch.utils.data import Dataset
import torch.utils.data as data_utils
from collections import defaultdict
import sys
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F
from keras.utils import to_categorical  
import math
 
class beamsearch_v2:
    def __init__(self, probs): 
           # Probs is a tensor
           #self.probs = probs
           self.probs = probs.data.cpu().numpy()     
          
    def decode(self):        
        probs = self.probs
        sequences = [[list(), 1.0]]
        #print "Shape I got is ", probs.shape
        for row in probs:
            #print "Row I got is ", row
            all_candidates = list()
            # expand each current candidate
            for i in range(len(sequences)):
                seq, score = sequences[i]
                for j in range(len(row)):
                    candidate = [seq + [j], score * -1.0 * math.log(row[j])]
                    all_candidates.append(candidate)
            # order all candidates by score
            ordered = sorted(all_candidates, key=lambda tup:tup[1])
            # select k best
            sequences = ordered[:13]
        #print "I am returning", sequences
        seq, score = sequences[0]
        return seq
