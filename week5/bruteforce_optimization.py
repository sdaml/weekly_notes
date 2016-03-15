import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

wines = pd.read_csv('wine_data.csv')

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

best_set_log = []
best_set_knn = []

best_score_log = 0
best_score_knn = 0

count = 0
for perm in perms:
    training_features, testing_features, training_target, testing_target = get_train_test_sets(wines, perm)
    
    log_model = LogisticRegression(random_state=123)
    log_model.fit(training_features, training_target)
    log_score = log_model.score(testing_features, testing_target)
    if log_score > best_score_log:
        best_score_log = log_score
        best_set_log = perm

    knn_model = KNeighborsClassifier(n_neighbors=142)
    knn_model.fit(training_features, training_target)
    knn_score = knn_model.score(testing_features, testing_target)
    if knn_score > best_score_knn:
        best_score_knn = knn_score
        best_set_knn = perm

    count += 1
    print "Finished %s/%s" % (count, len(perms))
print "Best posible score for knn:", best_score_knn
print "Best set of labels for knn", best_set_knn
print "Not included", set(data_labels) - set(best_set_knn)
print '\n'
print "Best posible score for log:", best_score_log
print "Best set of labels for log", best_set_log
print "Not included", set(data_labels) - set(best_set_log)