
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np

wines = pd.read_csv('wine_data.csv')


# In[2]:

wines[:5]


# In[3]:

# Shuffle the data set
wines.reindex(np.random.permutation(wines.index))
# Choose the labesl
feature_labels = ['alcohol', 'density', 'sulphates', 'residual sugar', 'pH', 'fixed acidity']
# Get the features and target
features = np.array(wines[feature_labels])
target = np.array(wines['quality'])

# Set the pivot
pivot = len(wines) * .8

# Split into test and training
training_features = features[:pivot]
testing_features = features[pivot:]
training_target = target[:pivot]
testing_target = target[pivot:]


# In[5]:

from sklearn.linear_model import LogisticRegression


# In[6]:

model = LogisticRegression(random_state=123)
model.fit(training_features, training_target)


# In[7]:

# With logistic regression we can also see how sure the alg is of a piece of data belonging to a catagory
print model.predict(testing_features)[:10]
prediction = model.predict_proba(testing_features)
print prediction[0]


# In[8]:

print model.score(testing_features, testing_target)


# In[9]:

# its useful if we have a generic function for this
def get_train_test_sets(data, feature_labels):
    features = np.array(data[feature_labels])
    target = np.array(data['quality'])
    # Set the pivot
    pivot = len(data) * .8

    # Split into test and training
    training_features = features[:pivot]
    testing_features = features[pivot:]
    training_target = target[:pivot]
    testing_target = target[pivot:]
    
    return (training_features, testing_features, training_target, testing_target)


# In[10]:

from itertools import combinations

# Automate finding the best combination (only works because this dataset is small)
data_labels = list(wines.columns.values) # get the labels of our dataset
data_labels.remove('quality')            # remove quality so we dont get contamination
perms = []

# (This would work and eventually compute the best value based on every single combination, 
# but it takes, like, more than 10 minutes
for i in range(1, len(data_labels)):
    for perm in combinations(data_labels, i):
        perms.append(perm)
perms = [list(p) for p in perms]

# This doesn't give us all the perms but we can kinda get a view what works best
# for i in range(1, len(data_labels)):
#     perms.append(data_labels[:i])
# for i in reversed(range(1, len(data_labels))):
#     perms.append(data_labels[:i])

print len(data_labels) # who wants to bet the best combination is all labels?
    
best_set = []
best_score = 0
count = 0
for perm in perms:
    training_features, testing_features, training_target, testing_target = get_train_test_sets(wines, perm)
    model = LogisticRegression(random_state=123)
    model.fit(training_features, training_target)
    score = model.score(testing_features, testing_target)
    if score > best_score:
        best_score = score
        best_set = perm
    count += 1
    print "Finished %s/%s" % (count, len(perms))
print "Best posible score:", best_score
print "Best set of labels", best_set
print "Not included", set(data_labels) - set(best_set)

