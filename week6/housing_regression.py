import pandas as pd
from sklearn import linear_model
import numpy as np
import sys
from itertools import combinations
import pickle


def get_train_test_sets(data, feature_labels):
    features = np.array(data[feature_labels])
    target = np.array(data['price'])
    # Set the pivot
    pivot = len(data) * .8

    # Split into test and training
    training_features = features[:pivot]
    testing_features = features[pivot:]
    training_target = target[:pivot]
    testing_target = target[pivot:]
    
    return (training_features, testing_features, training_target, testing_target)


def brute_force_model(data_set, target):
    '''
    Args:
        data_set: a pandas dataframe of the data set
        target: the feature to optimize the model for (price, quality) 
    returns:
        best model from optimization
    '''
    labels = list(data_set.columns.values)
    labels.remove(target)
    perms = []
    
    # Generate permutations of the labels
    for i in range(1, len(labels)):
        for perm in combinations(labels, i):
            perms.append(perm)
    perms = [list(p) for p in perms]
    
    best_train_set = []
    best_test_set = []
    best_score = 0
    count = 0
    
    # lets ignore how this basically generates a false positive due to lack of validation set
    for perm in perms:
        (training_features,
         testing_features,
         training_target,
         testing_target) = get_train_test_sets(data_set, perm)

        model = linear_model.LinearRegression()
        model.fit(training_features, training_target)
        score = model.score(testing_features, testing_target)

        if score > best_score:
            best_score = score
            best_train_set = training_features
            best_test_set = testing_target

        count +=1
        
        if count % 1000 == 0:
            progress = (float(count) / len(perms)) * 100
            print "%s percent complete" % str(progress)

    best_model = linear_model.LinearRegression(best_train_set,
                                               best_test_set)
    return best_model, best_score


def simple_model(data_set, target):
    pivot = int(0.8 * len(data_set))

    data_set.reindex(np.random.permutation(data_set.index))
    feature_labels = ['sqft_living', 'sqft_lot', 'sqft_basement', 'sqft_above']

    pd_features = data_set[feature_labels]
    features = np.array(pd_features)
    targets = np.array(data_set['price'])

    pivot = len(features) * .8
    train_features, test_features = features[:pivot], features[pivot:]
    train_target, test_target = targets[:pivot], targets[pivot:]

    model = linear_model.LinearRegression()
    model.fit(train_features, train_target)
    score = model.score(test_features, test_target)
    
    return model, score


def main():
    BRUTE_FORCE = False
    if len(sys.argv) > 1 and sys.argv[1] == '--force':
        BRUTE_FORCE = True

    houses = pd.read_csv('housing_data.csv')
    houses = houses.drop(['date', 'id'], 1)

    if BRUTE_FORCE:
        model, score = brute_force_model(houses, 'price')
        print "Brute forced a score of", score
    else:
        model, score = simple_model(houses, 'price')
        print "Simple got a score of", score

    with open('housing_model.pkl', 'wb') as f:
        out = pickle.dump(model, f)


if __name__ == "__main__":
    main()