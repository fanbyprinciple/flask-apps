from sklearn.feature_extraction.text import HashingVectorizer
import re
import os
import pickle

cur_dir = os.path.dirname(os.path.abspath('__file__'))
stop = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'stopwords.pkl'),'rb'))



