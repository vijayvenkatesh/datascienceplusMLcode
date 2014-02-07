import numpy as np
import math
import pandas as pd

class NaiveBayes():


  def __init__(self):

    """ Setup useful datastructures
        Feel free to change this
    """

    self._word_counts = {0:{},1:{}}  # Dict of {} - Insult = 1; Not insult = 0
    self._class_counts = {0:0,1:0} # Dict of {class:counts}
    self._priors = {}


  def fit(self, X, Y):
    """Fit a Multinomial NaiveBayes model from the training set (X, y).

        Parameters
        ----------
        X : array-like of shape = [n_samples]
            The training input samples.

        y : array-like, shape = [n_samples]

        Returns
        -------
        self : object
            Returns self.
    """
    for (x, y) in zip(X, Y):
      self._fit_instance(x, y)

      self._fit_priors()

  def _fit_priors(self):
    """Set priors based on data"""
    ##TODO##
    #total = self._class_counts[i] for i in self._class_counts.keys()
    #print len(self._class_counts.keys())
    for i in self._class_counts.keys():
      #print self._priors[i]
      self._priors[i] = self._class_counts[i] / float(sum(self._class_counts.values()))
    #print self._priors

  def _fit_instance(self, instance, y):
    """Train based on single samples       

     Parameters
        ----------
        instance : string = a line of text or single document
                   instance =  "This is not an insult"
                   instance = "You are a big moron"
        y : int = class of instance
                = 0 , 1 , class1, class2

    """
    for word in instance.split():
        #print y
        #print word
        #print word+str(y)
        # More elegant - self._word_couns[(word, y)] = self._word_counts.get((word, y)) + 1
        if word in self._word_counts[y]:
          self._word_counts[y][word] += 1
        else:
          self._word_counts[y][word] = 1

    self._class_counts[y] += 1  
    #self._class_counts[y] = self.classcounts.get(y,0) + 1


  def predict(self, X):
    """ Return array of class predictions for samples
      Parameters
      ----------
        X : array-like of shape = [n_samples]
            The test input samples.

        Returns
        -------
          : array[int] = class per sample
    """

    return [self._predict_instance(x) for x in X]


  def predict_proba(self, X):
    """ Return array of class predictions for samples
      Parameters
      ----------
        X : array-like of shape = [n_samples]
            The test input samples.

        Returns
        -------
          : array[array[ float, float ... ], ...] =  class probabilities per sample 
    """
    return [ self._predict_instance(instance) for instance in X ]

  def _predict_instance(self, instance):
    """ Return array of class predictions for samples
      Parameters
      ----------
        instance : string = a line of text or single document

        Returns
        -------
          : array[ float, float ... ] =  class probabilities 
    """
    return [ self._compute_class_probability(instance, c) for c in [0,1]]

  def _prior_prob(self, c):
    return self._priors[c]

  def _compute_class_probability(self, instance, c):
    """ Compute probability of instance under class c
        Parameters
        ----------
        instance : string = a line of text or single document

        Returns
        -------
          p : float =  class probability

      HINT : Often times, multiplying many small probabilities leads to underflow, a common numerical tricl
      is to compute the log probability.

      Remember, the log(p1 * p2 * p3) = log p1 + log p2 + log p3

    """
    sum = 0.0 #- because using log trick otherwise 1
    for word in instance.split():
        #if word in self._word_counts[c]:
        sum += math.log(self._word_counts[c][word] / float(self._class_counts[c]))
    #print sum
    return np.exp(sum + math.log(self._priors[c]))
    ##TODO##
    """"
    p_instance_c=1
    for word in instance.split():
      if word in self._word_counts.keys() \
      and c in self._word_counts[word]:
        p_word_c = float(self._word_counts[c][word]) / self._class_counts[c]
        p_instance_c *= p_word_c

      #Smoothing - another form of regularization
      #try:
      #  p_word_c = float(self._word_counts[c][word]) / self._class_counts[c]
      #except KeyError:
      #  p_word_c = 1.0/100000 #lambda smoothing (plus one or plus lambda)
      #p_instance_c *= p_word_c
      #return p_instance_c
      """

if __name__ == '__main__':
  data = pd.read_csv('data/train-utf8.csv')
  model = NaiveBayes()
  #print data.Insult.unique()
  model.fit(data.Comment, data.Insult)
  #print len(data.Insult)
  #print model._word_counts[0] - Print the dictionary with insult = 0
  #print model._class_counts

  print model.predict_proba(["This is a damn insult", "This is not an insult"])
