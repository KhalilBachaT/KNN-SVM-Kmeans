# KNN-SVM-Kmeans algorithms



## Table of content
* [Introduction](#introduction)
* [KNN]
* [SVM]
* [Kmeans]
* [Technologies](#technologies)
* [Setup](#setup)

## Introduction
A small application to which, we provide a knowledge base (fact base + rule base) and which enriches the fact base with other deductible facts using the rule base. 
An expert system must work in "forward chaining" and "backward chaining". We recall the general principle of the 2 types of chaining: 

## KNN
The k-nearest neighbors (KNN) algorithm is a simple, easy-to-implement supervised machine learning algorithm that can be used to solve both classification and 
regression problems.
### Description
we will discuss the KNN (K nearest neighbors) algorithm, and automatically determine the best number of neighbors to use for a given problem.
*Version 1
The training and test data are randomly drawn according to a centered and reduced normal distribution, in dimension d.
The labels are computed according to the membership or not of the point to a ball of radius R (e.g.: the points inside the ball are labeled 1 and the others 2.
*Version 2
the characteristics are identical but a noise is introduced in the training data: 5% of the labels are 'swapped'.
of the labels are exchanged. We do not modify the test data.
iris dataset : http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data




## SVM
Support Vector Machine” (SVM) is a supervised machine learning algorithm that can be used for both classification or regression challenges. However,  it is 
mostly used in classification problems. In the SVM algorithm, we plot each data item as a point in n-dimensional space (where n is a number of features you have) 
with the value of each feature being the value of a particular coordinate. Then, we perform classification by finding the hyper-plane that differentiates the 
two classes very well.
### Description
We will take the same data from the previous KNN exercise (take only 2 classes) and apply the linear SVM on it.


## Kmeans
Kmeans algorithm is an iterative algorithm that tries to partition the dataset into Kpre-defined distinct non-overlapping subgroups (clusters) where each data 
point belongs to only one group
## Description
We will now focus on the K-means algorithm for non-supervised classification.
The dataset used is the following : http://archive.ics.uci.edu/ml/datasets/Student+Academics+Performance
* Classify the data with the K-means method
* Find the K that gives the best performance.

## Technologies 
Project is created with:
* Python

## Setup
To run this project, you have to:
* Run main.py (python KNN.py)
* Enter parameters.
* The application will shows the classification's results.
