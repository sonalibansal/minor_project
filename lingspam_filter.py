import os
import numpy as np
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer




def make_Dictionary(train_dir):
    emails = [os.path.join(train_dir,f) for f in os.listdir(train_dir)]    
    all_words = []       
    for mail in emails:    
        with open(mail) as m:
            for i,line in enumerate(m):
                if i == 0:
                    words = line.split()
		    
                    all_words += words
    
    dictionary = Counter(all_words)
    
    list_to_remove = dictionary.keys()
    for item in list_to_remove:
        if item.isalpha() == False: 
            del dictionary[item]
        elif len(item) == 1 or len(item)==2 or len(item)==3:
            del dictionary[item]

    dictionary = dictionary.most_common(20)
  
    return dictionary
    
def extract_features(mail_dir): 
    files = [os.path.join(mail_dir,fi) for fi in os.listdir(mail_dir)]
    features_matrix = np.zeros((len(files),20))
    docID = 0;
    for fil in files:
      with open(fil) as fi:
        for i,line in enumerate(fi):
          if i == 0:
            words = line.split()
            for word in words:
              wordID = 0
              for i,d in enumerate(dictionary):

                if d[0] == word:
                  wordID = i
                  features_matrix[docID,wordID] = words.count(word)
        docID = docID + 1     
    return features_matrix
    


# Create a dictionary of words with its frequency

train_dir = 'travel-nontravel/train-mails'
dictionary = make_Dictionary(train_dir)

# Prepare feature vectors per training mail and its labels

train_labels = np.zeros(100)
train_labels[50:99] = 1
train_matrix = extract_features(train_dir)

# Training SVM and Naive bayes classifier and its variants

model1 = LinearSVC()
model2 = MultinomialNB()

model1.fit(train_matrix,train_labels)
model2.fit(train_matrix,train_labels)

# Test the unseen mails for Spam

#print model1

test_dir = 'travel-nontravel/test-mails'
test_matrix = extract_features(test_dir)
test_labels = np.zeros(60)
test_labels[29:59] = 1

result1 = model1.predict(test_matrix)
result2 = model2.predict(test_matrix)


print confusion_matrix(test_labels,result1)
print confusion_matrix(test_labels,result2)

def extract_features_for_single_doc(doc_path): 
    features_matrix = np.zeros((1,20), dtype = np.int)
    f=open(doc_path, "r")
    if f.mode == 'r': 
      contents =f.read()
      #print contents

      words = contents.split()
      for word in words:
        wordID = 0
        for i,d in enumerate(dictionary):
          if d[0] == word:
            wordID = i
            features_matrix[wordID] = words.count(word)
      
    return features_matrix

test_dir1 = 'travel-nontravel/tr2.txt'
test_matrix1 = extract_features_for_single_doc(test_dir1)

result3 = model1.predict(test_matrix1)
if result3==0:
	print "non travel"
else:
	print "travel"





