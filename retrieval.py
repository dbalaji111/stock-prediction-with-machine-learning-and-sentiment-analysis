# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:38:07 2019

@author: balaj
"""

import pandas as pd
import numpy as np
import itertools
from collection import Counter

def clean_nonmetric_data(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()

def load_data_and_labels(positive_data_file, negative_data_file):
     """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    positive_examples = list(open(positive_data_file,r).readlines())
    positive_examples = [s.strip() for s in positive_examples]    
    negative_examples = list(open(negative_data_file,r).readlines())
    negative_examples = [s.strip() for s in negative_examples]    
    # Split by words
    x_text = positive_examples+negative_examples
    
    
    
    