import numpy as np
import math
import pandas as pd

class NaiveBayes():


  def __init__(self):

    """ Setup useful datastructures
        Feel free to change this
    """
    self._word_counts = {} # Word counts of various words
    self._class_counts = {} # Class counts
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
      for (x,c) in zip(X,y):
        self._fit_instance(x,y)
    self._fit_priors()

  def _fit_priors(self):
    """Set priors based on data"""
    # Take how often single class appears over total number. 1/n for n classes
    ##TODO##

  def _fit_instance(self, instance, y):
    """Train based on single samples       

     Parameters
        ----------
        instance : string = a line of text or single document
        "This is not an insult" "You are a big moron"
        y = 0/1, class1, class2
        y : int = class of instance

        count of words per class - 
        for class 0 - for this class - increment word by 1
        increment count of class by 1  
      """

      ##TODO##


  def predict(self, X):
    """ Return array of class predictions for samples
      Parameters
      ----------
        X : array-like of shape = [n_samples]
            The test input samples.

        Returns
        -------
          : array[int] = class per sample
          return [self._predict_instance(x) for x in X]
    """

    ##TODO##


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
          For every class, count words per class, probabilities
          Array has two values
    """
    ##TODO##
    # return[self._compute_class_probability(instance,c) for all_classes]

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

    ##TODO##

if __name__ == '__main__':
  data = pd.read_csv('train-utf8.csv')
  model = NaiveBayes()
  #print type(data.Comment) - Type is series
  model.fit(data.Comment, data.Insult)

  print model.predict_proba(["This is not an insult", "You are a big moron"])
