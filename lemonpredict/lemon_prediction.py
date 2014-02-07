import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression, RidgeClassifierCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import Imputer
from sklearn import preprocessing

class LemonCarFeaturizer():
  def __init__(self):
    vectorizer = None
    self._imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
    self._binarizer = preprocessing.Binarizer()
    self._scaler = preprocessing.StandardScaler()
    self._preprocs = [self._imputer,
                      #self._scaler, 
                      #self._binarizer 
                      ]

  def _fit_transform(self, dataset):
    for p in self._preprocs:
      dataset = self._proc_fit_transform(p, dataset)
    return dataset

  def _transform(self, dataset):
    for p in self._preprocs:
      dataset = p.transform(dataset)

    return dataset

  def _proc_fit_transform(self, p, dataset):
    p.fit(dataset)
    dataset = p.transform(dataset)
    return dataset

  def create_features(self, dataset, training=False):
    data = dataset[ [ 
                  'VehOdo',
                  'VehYear',
                  'MMRAcquisitonRetailCleanPrice', 
                  'MMRCurrentAuctionAveragePrice', 
                  'MMRCurrentAuctionCleanPrice',
                  'MMRCurrentRetailAveragePrice',
                  'VehBCost',
                  'BYRNO',
                  'WarrantyCost',
                  'WheelTypeID',
                  'MMRCurrentRetailCleanPrice'] 
          ]

    data['MPY'] = data.VehOdo/ (data.VehYear - data.VehYear.min())
    data['RetailAuctionDiff'] = data.MMRAcquisitonRetailCleanPrice - data.MMRCurrentRetailCleanPrice

    actype = pd.get_dummies(dataset['AUCGUART'])
    data = pd.concat([data, actype], axis=1)

    nation = pd.get_dummies(dataset['Nationality'])
    data = pd.concat([data, nation], axis=1)

    prime = pd.get_dummies(dataset['PRIMEUNIT'])
    data = pd.concat([data, prime], axis=1)

    size = pd.get_dummies(dataset['Size'])
    data = pd.concat([data, size], axis=1)

    topthree = pd.get_dummies(dataset['TopThreeAmericanName'])
    data = pd.concat([data, topthree], axis=1)
    #make = pd.get_dummies(dataset['Make'])
    #data = pd.concat([data, make], axis=1)
    #IF training - save set of makes
    # Top 20 makes - and use that
    topbuyer = set(dataset.BYRNO.value_counts()[:20])
    dataset['TopBuyer'] = dataset.BYRNO.map(lambda x: x if x in topbuyer else 'other')
    topbuyers = pd.get_dummies(dataset['TopBuyer'])
    data = pd.concat([data, topbuyers], axis=1)

    print data.head()

    if training:
      data = self._fit_transform(data)
    else:
      data = self._transform(data)
    return data

def train_model(X, y):
  model = GradientBoostingClassifier(n_estimators=170, max_depth=5)
  #model = RidgeClassifierCV(alphas=[ 0.1, 1., 10. ])
  #model = LogisticRegression()
  #model = DecisionTreeClassifier() 
  #model = RandomForestClassifier(n_estimators=200, bootstrap=False,n_jobs=2)
  model.fit(X, y)
  #print model.coef_
  #Build models and average - 
  #Build models on subset of data - prices below/above pricepoint
  #Tiberius
  #Group by feature and outcome on the dataset

  return model

def predict(model, y):
  return model.predict(y)

def create_submission(model, transformer):
  submission_test = pd.read_csv('data/inclass_test.csv') # The test data set file
  predictions = pd.Series([x[1]
    for x in model.predict_proba(transformer.create_features(submission_test))])

  submission = pd.DataFrame({'RefId': submission_test.RefId, 'IsBadBuy': predictions}) # The output results data set file
  #submission.sort_index(axis=1, inplace=True)
  submission.to_csv('data/submission.csv', index=False)



def main():
  data = pd.read_csv('data/inclass_training.csv')
  featurizer = LemonCarFeaturizer()
  
  print "Transforming dataset into features..."
  X = featurizer.create_features(data, training=True)
  y = data.IsBadBuy

  print "Training model..."
  model = train_model(X,y)

  print "Cross validating..."
  print np.mean(cross_val_score(model, X, y, scoring='roc_auc'))

  print "Create predictions on submission set..."
  create_submission(model, featurizer)


if __name__ == '__main__':
  main()
