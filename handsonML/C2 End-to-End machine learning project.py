# -*- coding: utf-8 -*-

# -- Sheet --

# Setup
# Python ≥3.5 is required
import sys
assert sys.version_info >= (3, 5)

# Scikit-Learn ≥0.20 is required
import sklearn
assert sklearn.__version__ >= "0.20"

# Common imports
import numpy as np
import os

# To plot pretty figures
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

# Where to save the figures
PROJECT_ROOT_DIR = "."
CHAPTER_ID = "end_to_end_project"
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
os.makedirs(IMAGES_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

# # **Download the File**


import os  # The OS module in Python provides functions for interacting with the operating system. 
import tarfile  # Python library for zipping/unzipping file
import urllib.request  # Python library for retrieving files

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/" # create a variable for download root
HOUSING_PATH = os.path.join("datasets", "housing") 
# create a path join variable 
# os.path.join() method in Python join one or more path components intelligently. 
# This method concatenates various path components with exactly one directory separator (‘/’) following each non-empty
# part except the last path component. If the last path component to be joined is empty then 
# a directory seperator (‘/’) is put at the end. If a path component represents an absolute path, 
# then all previous components joined are discarded and joining 
# continues from the absolute path component.

HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz" # create a variable for the addtional download root

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH): # Some default parameters for the URL and storage path
    if not os.path.isdir(housing_path): # Check if "datasets/housing" exists
        os.makedirs(housing_path) # Make this directory
    tgz_path = os.path.join(housing_path,"housing.tgz") # "datasets/housing/housing.tgz" stringpath stored as a variable
    urllib.request.urlretrieve(housing_url,tgz_path) # Download from URL, store it in a stringpath
    housing_tgz = tarfile.open(tgz_path) # Opened file stored in a variable  
    housing_tgz.extractall(path=housing_path) # Extract all files into this path
    housing_tgz.close() # Close the file

fetch_housing_data()

# # **Load the data**


import pandas as pd
def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path,"housing.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data() # load housing data and store it as a housing variable
housing.head() # check the top five rows using the head() function 

housing.info()

housing["ocean_proximity"].value_counts()   # value_counts() for the 

housing.describe() # shows a summary of the numerical attributes 

# %matplotlib inline # only in a Jupyter notebook. It tells Jupyter to set up Matplotlib so it uses Jupyter's own backend. Plots 
# are then rendered within the notebook itself. Note that calling show() is optional in a jupyter notebook, as it will 
# automatically display plots when a cell is executed. 
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20,15)) # hist() method relies on Matplotlib, which in turn relies on a user-specified 
# graphical backend to draw. Before plot anything, you need to specify which backend matplotlib should use. The simplest option
# is to use Jupyter's magic comand %matplotlib inline. 
save_fig("attribute_histogram_plots")
plt.show()

# Median income has been scaled and capped at 15 for higher median incomes, at 0.5 for lower median incomes. 
# It represent roughly tens of thousands dollars
# Housing median age and median house value were also capped. Median house value cap can be serious problem, because your ML can learn that 
# prices never go beyond that limit. 

# # **Using Pandas iloc, loc, & ix to select rows and columns in DataFrames**
# 
# 1. Pandas iloc data selection
# The iloc indexer for Pandas Dataframe is used for integer-location based indexing / selection by position.
# 
# The iloc indexer syntax is data.iloc[<row selection>, <column selection>], which is sure to be a source of confusion for R users. “iloc” in pandas is used to select rows and columns by number, in the order that they appear in the data frame. You can imagine that each row has a row number from 0 to the total rows (data.shape[0])  and iloc[] allows selections based on these numbers. The same applies for columns (ranging from 0 to data.shape[1] )
# 
# There are two “arguments” to iloc – a row selector, and a column selector.  For example:


# Single selections using iloc and DataFrame

# Rows:
print(housing.iloc[0]) # first row of data frame (Aleshia Tomkiewicz) - Note a Series data type output.
print(housing.iloc[1]) # second row of data frame (Evan Zigomalas)
print(housing.iloc[-1]) # last row of data frame (Mi Richan)

# Columns:
print(housing.iloc[:,0]) # first column of data frame (first_name)
print(housing.iloc[:,1]) # second column of data frame (last_name)
print(housing.iloc[:,-1]) # last column of data frame (id)

# Multiple row and column selections using iloc and DataFrame
housing.iloc[0:5] # first five rows of dataframe
housing.iloc[:, 0:2] # first two columns of data frame with all rows
housing.iloc[[0,3,6,24], [0,5,6]] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
housing.iloc[0:5, 5:8] # first 5 rows and 5th, 6th, 7th columns of data frame (county -> phone1).

# # **2. Pandas loc data selection**
# The Pandas loc indexer can be used with DataFrames for two different use cases:
# 
# a.) Selecting rows by label/index
# b.) Selecting rows with a boolean / conditional lookup
# The loc indexer is used with the same syntax as iloc: data.loc[<row selection>, <column selection>] .
# 
# 2a. Label-based / Index-based indexing using .loc
# Selections using the loc method are based on the index of the data frame (if any). Where the index is set on a DataFrame, using <code>df.set_index()</code>, the .loc method directly selects based on index values of any rows. For example, setting the index of our test data frame to the persons “last_name”:


print(housing.set_index("median_income", inplace=True)) #setting the index of our test data frame to the housing “median_income”
print(housing.head())

# Now with the index set, we can directly select rows for different “median_income” values using .loc[<label>]  – either singly, or in multiples. For example:


housing.loc[3.8462]

housing.loc[[7.2574,5.6431]]

print(housing.set_index("housing_median_age", inplace=True)) #setting the index of our test data frame to the housing “median_income”
print(housing.head())

# Select rows with index values 'Andrade' and 'Veness', with all columns between 'city' and 'email'
housing.loc[41:52, 'longitude':'latitude']


data.loc[['Andrade', 'Veness'], 'city':'email']

# Select same rows, with just 'first_name', 'address' and 'city' columns
housing.loc[41:52, ['longitude','latitude','median_house_value']]
 
# Change the index to be based on the 'id' column
housing.set_index('households', inplace=True)
# select the row with 'id' = 487
housing.loc[177.0]

# Select rows with first name Antonio, # and all columns between 'city' and 'email'
data.loc[data['first_name'] == 'Antonio', 'city':'email']
 
# Select rows where the email column ends with 'hotmail.com', include all columns
data.loc[data['email'].str.endswith("hotmail.com")]   
 
# Select rows with last_name equal to some values, all columns
data.loc[data['first_name'].isin(['France', 'Tyisha', 'Eric'])]   
       
# Select rows with first name Antonio AND hotmail email addresses
data.loc[data['email'].str.endswith("gmail.com") & (data['first_name'] == 'Antonio')] 
 
# select rows with id column between 100 and 200, and just return 'postal' and 'web' columns
data.loc[(data['id'] > 100) & (data['id'] <= 200), ['postal', 'web']] 
 
# A lambda function that yields True/False values can also be used.
# Select rows where the company name has 4 words in it.
data.loc[data['company_name'].apply(lambda x: len(x.split(' ')) == 4)] 
 
# Selections can be achieved outside of the main .loc for clarity:
# Form a separate variable with your selections:
idx = data['company_name'].apply(lambda x: len(x.split(' ')) == 4)
# Select only the True values in 'idx' and only the 3 columns specified:
data.loc[idx, ['email', 'first_name', 'company']]

# # **Create a Test Set**



# to make this notebook's output identical at every run
random = np.random.seed(42)
print(random)  # to make sure that 


import numpy as np

print(len(housing))

# For illustration only. Sklearn has train_test_split()
def split_train_test(data, test_ratio): # create a function for split train/test ratio, default parameters are (which) data? and 
# (what is the) test data set ratio?
    shuffled_indices = np.random.permutation(len(data)) # This function randomly permute a sequence, or return a permuted range. 
    #If x is a multi-dimensional array, it is only shuffled along its first index. 这个function把原来的数据中所有的数据的个数和排序都
    # shuffle了一遍. 而它shuffle的这个sequence是按照你之前的那个seed number来的。选的某个seed，那么shuffle之后的排序就会一摸一样。
    print(shuffled_indices) 
    test_set_size = int((len(data)) * test_ratio) # 计算出test这部分数据的size，即整个数据长度* test size ratio（即20%）
    test_indices = shuffled_indices[:test_set_size] # test indice 就是从0到test size的数，即0:4128，共4128个数据。
    train_indices = shuffled_indices[test_set_size:] # train indice就是从test size那个数到最后，即 4128:20640， 其中共16512个数据。
    return data.iloc[train_indices], data.iloc[test_indices] # iloc function is a purely integer-location based indexing 
    # for selection by position.
    # 这个是什么意思还要问一下？

train_set, test_set = split_train_test(housing, 0.2)
print(len(train_set))
print(len(test_set))

# you could compute a hash of each instance’s identifier, keep only the last byte of the hash, and put the instance in the test set if this value is lower or equal to 51 (~20% of 256). This ensures that the test set will remain consistent across multiple runs, even if you refresh the dataset. The new test set will contain 20% of the new instances, but it will not contain any instance that was previously in the training set.
# 
# The method uses a cyclic redundancy check, which is a method of checking that the raw blocks of memory have not been damaged/changed. It is a way to ensure data integrity, e.g. in network traffic - checking if a message way altered between being sent and received.
# 
# For train/test splits, it is checking the unique identifier of each sample. We have a column that gives each sample an ID - this should never be changed! Don't delete rows, only append to the end with new unique IDs.
# 
# In this part: test_ratio * 2**32, the part 232 represents the largest integer of a 32-bit system.
# 
# 0xFFFFFFFF is a large number; it's the hexadecimal representation of 232−1
# 
# To answer your questions:
# 
# What is the 3rd line doing:
# crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32
# 
# Based on the information I gave above, we see the crc32 function finds the checksum value in memory (of the unique identifier). If we know the unique ID has never changed, then We ensure that crc32(np.int64(identifier)) & 0xffffffff will always return exactly the same numeric value, across all Python versions and platforms.
# 
# Imagine we give IDs in the range 0-80 for train, and 81-100 for test. No we want to make sure a sample'd s ID falls in the first bucket. We check its ID is simple less that 81, right? Well the numeric value we made above is checked to be less than our test_ratio * 2**32, where 2**32 is the largest 32-bit number. It checks that the sample's ID is within the range of train data, not in the test bucket:: > test_ratio * 2**32.
# 
# What is the anonymous function doing in the 2nd to last line?
# lambda id_: test_set_check(id_, test_ratio)
# 
# This simply applies our test_set_check function to each sample's unique identifiers. Using the apply methd on a Pandas Series object (here it is one column of a Pandas DataFrame).


# Even if we set a random number generator's seed before calling np.random.permutation(), it will break next time when you fetch 
# an updated dataset. Solution: use each instance's identifier to decide whether or not it should go in the test set.


from zlib import crc32 # a software library used for data compression

def test_set_check(identifier, test_ratio):
    #print(np.int64(identifier)) # identifier, which later in the lambda is the ID column of each row of instance data
    #print(crc32(np.int64(identifier))) # making those identifier into unique 32 bit number
    #print(crc32(np.int64(identifier)) & 0xffffffff) # The result is always unsigned. To generate the same numeric value across all 
    # Python versions and platforms, use crc32(data) & 0xffffffff. (even in Python 2)
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32 



def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    print(ids)
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

import pandas as pd

housing = load_housing_data() # load housing data and store it as a housing variable

housing_with_id = housing.reset_index() # Pandas reset_index() is a method to reset index of a Data Frame.adds an 'index'column
# reset_index() method sets a list of integer ranging from 0 to length of data as index.
# DataFrame.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill=”)
train_set, test_set = split_train_test_by_id(housing_with_id,0.2,"index")

print(crc32(np.int64(0)))
print(crc32(np.int64(1)))
print(crc32(np.int64(0)))
print(crc32(np.int64(56789096)))


# The implementation of test_set_check() above works fine in both Python 2 and Python 3. In earlier releases, the following implementation was proposed, which supported any hash function, but was much slower and did not support Python 2:


import hashlib

def test_set_check(identifier, test_ratio, hash=hashlib.md5):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio

# The housing dataset doesn't have an identifier column. Simple solution is to use the ROW INDEX as the ID: 

import pandas as pd

housing = load_housing_data() # load housing data and store it as a housing variable

housing_with_id = housing.reset_index() # Pandas reset_index() is a method to reset index of a Data Frame.adds an 'index'column
# reset_index() method sets a list of integer ranging from 0 to length of data as index.
# DataFrame.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill=”)
train_set, test_set = split_train_test_by_id(housing_with_id,0.2,"index")


print(housing_with_id.head()) # check the top five rows using the head() function 
print(housing_with_id.info()) #果然多了列variable叫index，作为每个数据的编号

# Or use a district's latitude and longitude, and combine them into an ID like so: 

housing_with_id["id"] = housing["longitude"]*1000 + housing["latitude"]
train_set, test_set = split_train_test_by_id(housing_with_id,0.2, "id")

# ## Use Scikit-learn's "train_test_split" function to split datasets. 
# 
# 
# sklearn.model_selection.train_test_split(*arrays, test_size=None, train_size=None, random_state=None, shuffle=True, stratify=None)[source]¶
# 
# chek more from: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html?highlight=train%20test%20split#sklearn.model_selection.train_test_split


from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(housing,test_size=0.2, random_state=42,shuffle=True,)  #random_state works like set.seed()

test_set.head()

train_set.head()

# ### **pandas.cut** function (x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True)[source]
# Bin values into discrete intervals.
# 
# Use cut when you need to segment and sort data values into bins. This function is also useful for going from a continuous variable to a categorical variable. For example, cut could convert ages to groups of age ranges. Supports binning into an equal number of bins, or a pre-specified array of bins.


# 


housing["income_cat"] = pd.cut(housing["median_income"],bins=[0.,1.5,3.0,4.5,6.,np.inf], labels=[1,2,3,4,5])

# use pd.cut() function to create an income category attribute with 5 categories (labeled from 1 to 5)
# 为什么要这么做呢？因为most median income values are clustered around 1.5 to 6, but some median incomes go far beyond 6. It is 
# important to have a sufficient number of instances in your dataset for each stratum, or else the estimate of the stratum's 
# importance may be biased. Not too many strata, but each stratum should be large enough.

housing["income_cat"].head()


housing["income_cat"].hist() # 看一下histogram来判断这个数据的分区。

# Stratified sampling based on the income category.
# 
# Use Scikit-learn's **StratifiedShuffleSplit** class
# 
# class sklearn.model_selection.StratifiedShuffleSplit(n_splits=10, *, test_size=None, train_size=None, random_state=None)[source]
# Stratified ShuffleSplit cross-validator
# 
# Provides train/test indices to split data in train/test sets.
# 
# This cross-validation object is a merge of StratifiedKFold and ShuffleSplit, which returns stratified randomized folds. The folds are made by **preserving the percentage of samples for each class.**
# 
# Note: like the ShuffleSplit strategy, stratified random splits do not guarantee that all folds will be different, although this is still very likely for sizeable datasets.
# 
# n_splitsint, default=10
# Number of re-shuffling & splitting iterations.
# 
# test_sizefloat or int, default=None
# If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split. If int, represents the absolute number of test samples. If None, the value is set to the complement of the train size. If train_size is also None, it will be set to 0.1.
# 
# train_sizefloat or int, default=None
# If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the train split. If int, represents the absolute number of train samples. If None, the value is automatically set to the complement of the test size.
# 
# random_stateint, RandomState instance or None, default=None
# Controls the randomness of the training and testing indices produced. Pass an int for reproducible output across multiple function calls. 
# 
# Methods
# 
# get_n_splits([X, y, groups])
# 
# Returns the number of splitting iterations in the cross-validator
# 
# split(X, y[, groups])
# 
# Generate indices to split data into training and test set.


# Examples of using StratifiedShuffleSplit:

import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
X = np.array([[1, 2], [3, 4], [1, 2], [3, 4], [1, 2], [3, 4]])
y = np.array([0, 0, 0, 1, 1, 1])

print(X)
print(y)

sss = StratifiedShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
sss.get_n_splits(X, y)
print(sss)

StratifiedShuffleSplit(n_splits=5, random_state=0,)
for train_index, test_index in sss.split(X, y):
     print("TRAIN:", train_index, "TEST:", test_index)
     X_train, X_test = X[train_index], X[test_index]
     y_train, y_test = y[train_index], y[test_index]

from sklearn.model_selection import StratifiedShuffleSplit # from sklearn library import this class

split_data = StratifiedShuffleSplit(n_splits=1, test_size=0.2,random_state=42) # making an instance that returns some instance of 
# a class that makes stratified split

for train_index, test_index in split_data.split(housing,housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]
    print("TRAIN:",strat_train_set, "TEST:", strat_test_set) # view the splitted train and test data set



strat_test_set["income_cat"].value_counts()/len(strat_test_set)

strat_test_set["income_cat"].head()


def income_cat_proportions(data):
    return data["income_cat"].value_counts() / len(data)

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

compare_props = pd.DataFrame({
    "Overall": income_cat_proportions(housing),
    "Stratified": income_cat_proportions(strat_test_set),
    "Random": income_cat_proportions(test_set),
}).sort_index()
compare_props["Rand. %error"] = 100 * compare_props["Random"] / compare_props["Overall"] - 100
compare_props["Strat. %error"] = 100 * compare_props["Stratified"] / compare_props["Overall"] - 100

compare_props

# remove the stratified sample

for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat",axis=1, inplace=True)


# # Discover and visualize the data to gain insights
# **Visualizing Geographical Data**
# 
# First, you need to make sure you put the test  set aside, and only exploring the training set. 
# Also, if the training set is very large, you may want to sample an exploration set, to make manipulations easy and fast. 
# Let's create a copy to play without harming the training set: 


housing.plot(kind="scatter",x="longitude",y="latitude",alpha=0.1) # the alpha score make it easier to visualize the 
# high density data points

# For more details of maplotlib.pyplot
# See: 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html


housing.plot(kind="scatter",x="longitude", y="latitude",alpha=0.4, s=housing["population"]/100, label= "population", 
             figsize=(10,7), c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
             sharex=False)
plt.legend()
save_fig("housing_prices_scatterplot")

# the image shows that the housing price is very much related to the location (close to the ocena) and to the population density.


# # **Correlations**


corr_matrix=housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False)

# pandas.plotting.scatter_matrix
# pandas.plotting.scatter_matrix(frame, alpha=0.5, figsize=None, ax=None, grid=False, diagonal='hist', marker='.', density_kwds=None, hist_kwds=None, range_padding=0.05, **kwargs)
# 
# https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html


from pandas.plotting import scatter_matrix
attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
scatter_matrix(housing[attributes],figsize=(12,8))

# from correlation plots above, it's obvious the most promising attribute to predict the median house value is the median income

housing.plot(kind="scatter",x="median_income",y="median_house_value",alpha=0.1)

# # Experimenting with Attribute combinations
# 
# Some attributes have a tail-heavy distribution, you may want to transform them (e.g. by computing their logarithm).
# 
# It's also worthwhile to try out various attribute combinations. 


housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"] = housing["population"]/housing["households"]

corr_matrix = housing.corr() # first create an instance of correlation class 
corr_matrix["median_house_value"].sort_values(ascending=False)

# # Prepare the data for machine learning algorithms


# first revert to a clean training set(by copying strat_train_set), let's separate the predictors and the labels since we don't 
# necessarily want to apply the same transformations to the predictors and the target values :

housing = strat_train_set.drop("median_house_value",axis=1)  # note that drop() creates a copy of the data and does not 
# affect strat_train_set
housing_labels = strat_train_set["median_house_value"].copy()


# # Data Cleaning 


# Three ways to work with missing features. 

# 1 Remove missing values: DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)[source]
# 2 Remove the whole attribute: DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')[source]
# Drop specified labels from rows or columns. Remove rows or columns by specifying label names and corresponding axis, or by specifying directly index or column names. When using a multi-index, labels on different levels can be removed by specifying the level.
# 3 Set the values to some value(zero, the mean, the median, etc): DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)[source]
# Fill NA/NaN values using the specified method.


housing.dropna(subset=["total_bedrooms"]) # get rid of the corresponding districts
housing.drop("total_bedrooms",axis=1) #option 2 # axis{0 or ‘index’, 1 or ‘columns’} Axis along which to fill missing values.

median = housing["total_bedrooms"].median() #option 3 
housing["total_bedrooms"].fillna(median,inplace=True)  # inplace bool, default False
# If True, fill in-place. Note: this will modify any other views on this object (e.g., a no-copy slice for a column in a DataFrame).

# class sklearn.impute.SimpleImputer(*, missing_values=nan, strategy='mean', fill_value=None, verbose=0, copy=True, add_indicator=False)[source]
# 
# Imputation transformer for completing missing values.
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html?highlight=simple%20imputer#sklearn.impute.SimpleImputer


# Scikit-learn provides a handy class to take care of missing values: simple imputer

from sklearn.impute import SimpleImputer

# First, create a SimpleImputer class instance, specifying that you want to replace each attributes

imputer = SimpleImputer(strategy="median") # create an instance of the imputer class, specify strategy parameter

# Since the median can only be computed on numerical attributes, we need to create a copy of the data without the test attribute: 
# ocean_proximity
housing_num = housing.drop("ocean_proximity", axis=1)  # axis{0 or ‘index’, 1 or ‘columns’} Axis along which to fill missing values.

# fit the imputer instance to the training data using the fit() method:
imputer.fit(housing_num) # the imupter estimation itself is performed by fit() method, and it takes only a dataset as a parameter. 

# the imputer has simply computed the median of each attribute and stored the result in its statistics_ instance variable. 

imputer.statistics_




# Use this "trained" imputer to transform the training set by replacing missing values by the learned medians. 

housing_num.median().values


# Use this "trained" imputer to transform the training set by replacing missing values by the learned medians. 

X = imputer.transform(housing_num)

# the result is a plain Numpy array containing 

housing_tr = pd.DataFrame(X, columns=housing_num.columns)

# # Handling Text and Categorical Attributes


housing_cat = housing["ocean_proximity"]

housing_cat.head(20) #enter number there to specify how many first lines you would like to view

# Since most ML algorithms prefer to work with numbers, so let's convert these categories from text to numbers. 
# 
# # **sklearn.preprocessing.OrdinalEncoder**
# class sklearn.preprocessing.OrdinalEncoder(*, categories='auto', dtype=<class 'numpy.float64'>, handle_unknown='error', unknown_value=None)[source]
# 
# Encode categorical features as an integer array.
# 
# The input to this transformer should be an array-like of integers or strings, denoting the values taken on by categorical (discrete) features. The features are converted to ordinal integers. This results in a single column of integers (0 to n_categories - 1) per feature.



from sklearn.preprocessing import OrdinalEncoder

ordinal_encoder = OrdinalEncoder() # first create an instance of the encoder
housing_cat_x = housing_cat.values.reshape(-1,1) # Most scikit learn estimators need a 2D array rather than a 1D array
# use x.values.reshape(-1,1) to reshape the form to be compatible.

housing_cat_encoded = ordinal_encoder.fit_transform(housing_cat_x)

housing_cat_encoded[:10]

ordinal_encoder.categories_

ordinal_encoder.get_params(deep=True)

# Since ML algorithms will assume that two nearby values are more similar than two distant values. However, this ocean_proximity variable is not the case. 
# 
# categories 0 1H OCEAN are more similar to categories 4 Near Ocean.
# 
# therefore, we can use **one-hot encoding** to create **dummy attributes** for binary attribute per category


from sklearn.preprocessing import OneHotEncoder

cat_encoder = OneHotEncoder()
housing_cat_x = housing_cat.values.reshape(-1,1) # need to transform from 1D array to 2D array
housing_cat_1hot = cat_encoder.fit_transform(housing_cat_x) 
housing_cat_1hot

housing_cat_1hot.toarray()

cat_encoder.categories_

# # **Custom Transformers**
# 
# Since Scikit-Learn relies on **duck typing**(not inheritance), all you need to do is create a class and implement three methods. 
# 
# **Duck typing** in computer programming is an application of the duck test—"If it walks like a duck and it quacks like a duck, then it must be a duck"—to determine whether an object can be used for a particular purpose. With normal typing, suitability is determined by an object's type.
# 
# Write your own transformers for tasks such as custom cleanup operations or combining specific attributes.
# 
# You will want (such as pipelines), and since Scikit-Learn relies on duck typing (not inheritance), : fit() (returning self), transform(), and fit_transform().
# 
# You can get the last one for free by simply adding **TransformerMixin** as a base class.
# If you add BaseEstimator as a base class (and avoid *args and **kwargs in your constructor), you will also get two extra methods (get_params() and set_params()) that will be useful for automatic hyperparameter tuning.


# *args and **kwargs allow you to pass multiple arguments or keyword arguments to a function. Basically, instead of passing a list of positional or keyword argument, you can allow python to just 
# 
# see more at: https://realpython.com/python-kwargs-and-args/
# 
# In this case, you have to bear in mind that order counts. Just as non-default arguments have to precede default arguments, so *args must come before **kwargs.
# 
# To recap, the correct order for your parameters is:
# 
# Standard arguments
# *args arguments
# **kwargs arguments


from sklearn.base import BaseEstimator, TransformerMixin

rooms_idx, bedrooms_idx, population_idx, households_idx = 3, 4, 5, 6


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    """A small transformer adds the combined attributes."""
    # no *args or **kwargs for getting two extra methods: `get_params()` and `set_params()`
    def __init__(self, add_bedrooms_per_room=True):  # often helpful to provide sensible defaults
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self  # nothing else to do

    def transform(self, X):
        rooms_per_household = X[:, rooms_idx] / X[:, households_idx]
        population_per_houshold = X[:, population_idx] / X[:, households_idx]

        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_idx] / X[:, rooms_idx]
            return np.c_[X, rooms_per_household, population_per_houshold,
                         bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_houshold]


attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
housing_extra_attributes = attr_adder.transform(housing.values)

housing.shape, housing_extra_attributes.shape


housing_extra_attributes = pd.DataFrame(
    housing_extra_attributes,
    columns=list(housing.columns)+['rooms_per_household', 'population_per_household'],
    index=housing.index)
housing_extra_attributes.head(2)

# # **4.4 Feature scaling**
# One of the most important transformations you need to apply to your data is **feature scaling. With few exceptions, ML algorithms don’t perform well when the input numerical attributes have very different scales.**
# 
# Two common ways to get all attributes to have the same scale:
# 
# * values are shifted and rescaled so that they end up ranging from 0 to 1 by subtracting the min value and dividing by the max minus the min.
#    
#    *1）change the `feature_range` if you do not want 0-1*
# sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1))
# 
#    *2）The transformation is given by:*
# min, max = feature_range
# X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
# X_scaled = X_std * (max - min) + min
# 
#    *3）The transformation is calculated as:*
#     X_scaled = scale * X + min - X.min(axis=0) * scale
#     where scale = (max - min) / (X.max(axis=0) - X.min(axis=0))
# 
# - it subtracts the mean value (so standardized values always have a zero mean), and then it divides by the standard deviation so that the resulting distribution has unit variance.
# sklearn.preprocessing.StandardScaler(copy=True, with_mean=True, with_std=True)
# 
# 
# - Unlike min-max scaling, standardization does not bound values to a specific range, which may be a problem for some algorithms (e.g., neural networks often expect an input value ranging from 0 to 1).


# # **4.5 Transformation pipelines**
# 
# Scikit-Learn provides the Pipeline class to help with such sequences of transformations , which can help you make many data transformation steps executed in the right order.


# 



from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# a small pipeline for the numerical attributes
# List of (name, transform) tuples (implementing fit/transform) that are chained,
# in the order in which they are chained, with the last object an estimator.
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('attribs_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler())
])
housing_num_tr = num_pipeline.fit_transform(housing_num)


housing_num.shape, housing_num_tr.shape

# 
# The Pipeline constructor takes a list of name/estimator pairs defining a sequence of steps. All but the last estimator must be transformers (i.e., they must have a fit_transform() method).
# The names can be anything you like (as long as they are unique and don’t contain double underscores, __); they will come in handy later for hyperparameter tuning.
# 
# 
# When you call the pipeline’s fit() method, it calls fit_transform() sequentially on all transformers, passing the output of each call as the parameter to the next call until it reaches the final estimator, for which it calls the fit() method.
# 
# The pipeline exposes the same methods as the final estimator. In this example, the last estimator is a StandardScaler, which is a transformer, so the pipeline has a transform() method that applies all the transforms to the data in sequence (and of course also a fit_transform() method, which is the one we used).


# It works great with pandas DataFrames
from sklearn.compose import ColumnTransformer

# Create one transformer to handle all columns, applying the appropriate
# transformations to each column
num_attribs = list(housing_num)
cat_attribs = ['ocean_proximity']

# Requires a list of tuples, where each tuple contains a name, a transformer, and a list of names (or indices) of columns that 
# the transformer should be applied to.

full_pipeline = ColumnTransformer([
    ('num', num_pipeline, num_attribs),
    ('cat', OneHotEncoder(), cat_attribs)
], remainder='drop')
# It applies each transformer to the appropriate columns and
# concatenates the outputs along the second axis.
# The transformers must return the same number of rows.
housing_prepared = full_pipeline.fit_transform(housing)  #transformed whole dataset stored in housing_prepared

# - remainder='drop' (default): only the specified columns in transformers are transformed and combined in the output, and the non-specified columns are dropped.
# 
# - remainder='passthrough': all remaining columns that were not specified in transformers will be automatically passed through. This subset of columns is concatenated with the output of the transformers.
# 
# - remainder=estimatror: the remaining non-specified columns will use the remainder estimator. The estimator must support fit() and transform(). Note that using this feature requires that the DataFrame columns input at fit and transform have identical order.


housing.shape, housing_prepared.shape #这个housing_prepared variable里面到底是什么东西？哦，就是整个数据都在里面。

housing.values

housing_prepared

# Note that the OneHotEncoder returns a **sparse matrix**, while the num_pipeline returns a **dense matrix**. When there is such a mix of sparse and dense matrices, the ColumnTransformer estimates the density of the final matrix (i.e., the ratio of nonzero cells), and it returns a sparse matrix if the density is lower than a given threshold (by default, sparse_threshold=0.3).
# 
# 
# https://machinelearningmastery.com/sparse-matrices-for-machine-learning/
# 
# about dense and sparse matrix


# # 5. Select and train a model
# ## 5.1 Train and evaluate on the training set


from sklearn.linear_model import LinearRegression

# first revert to a clean training set(by copying strat_train_set), let's separate the predictors and the labels since we don't 
# necessarily want to apply the same transformations to the predictors and the target values :

housing = strat_train_set.drop("median_house_value",axis=1)  # note that drop() creates a copy of the data and does not 
# affect strat_train_set
housing_labels = strat_train_set["median_house_value"].copy()

housing_prepared.view() # what we use to predict is transformed whole dataset

# %matplotlib inline # only in a Jupyter notebook. It tells Jupyter to set up Matplotlib so it uses Jupyter's own backend. Plots 
# are then rendered within the notebook itself. Note that calling show() is optional in a jupyter notebook, as it will 
# automatically display plots when a cell is executed. 
import matplotlib.pyplot as plt
housing_prepared.hist(bins=50, figsize=(20,15)) # hist() method relies on Matplotlib, which in turn relies on a user-specified 
# graphical backend to draw. Before plot anything, you need to specify which backend matplotlib should use. The simplest option
# is to use Jupyter's magic comand %matplotlib inline. 
save_fig("attribute_histogram_plots")
plt.show()

# Median income has been scaled and capped at 15 for higher median incomes, at 0.5 for lower median incomes. 
# It represent roughly tens of thousands dollars
# Housing median age and median house value were also capped. Median house value cap can be serious problem, because your ML can learn that 
# prices never go beyond that limit. 

housing_labels.view() # what we need to predict y is median house value

# train a linear regression model
lin_reg = LinearRegression() # create an instance of linear regression
lin_reg.fit(housing_prepared, housing_labels) # fit the linear regression model, x=housing_prepared, y= housing_labels

# Try the full preprocessing pipeline on a few training instances
some_data = housing.iloc[:5]
some_labels = housing_labels[:5]
some_data_prepared = full_pipeline.transform(some_data)

print('Predictions:', lin_reg.predict(some_data_prepared)) # linear regression is a predictor, get the prediction value for 
#each of the 

print('True labels:', list(some_labels))

housing_predictions = lin_reg.predict(housing_prepared)

housing_predictions.view()

# Plot outputs

plt.scatter(housing_labels, housing_predictions,  color='black')


plt.plot(housing_prepared, housing_predictions, color='blue', linewidth=3)



plt.show()

from sklearn.metrics import mean_squared_error
housing_predictions = lin_reg.predict(housing_prepared)
lin_mse = mean_squared_error(housing_labels, housing_predictions)
lin_rmse = np.sqrt(lin_mse)
lin_rmse

from sklearn.metrics import mean_absolute_error, mean_squared_error

def root_mean_squared_error(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    return rmse

housing_preds = lin_reg.predict(housing_prepared) #先做完linear regression prediction, stored in a variable,然后再用这个rms function
lin_rmse = root_mean_squared_error(housing_labels, housing_preds) 
lin_rmse

lin_mae = mean_absolute_error(housing_labels, housing_preds)
lin_mae

# **Underfitting!** 
# 
# Most districts’ median_housing_values range between 120,000 and 265,000, so a typical prediction error of 68,628 is not very satisfying.


from sklearn.tree import DecisionTreeRegressor

# DT is a powerful model, capable of finding complex nonlinear relationships in the data.
tree_reg = DecisionTreeRegressor(random_state=42)
tree_reg.fit(housing_prepared, housing_labels)

housing_preds = tree_reg.predict(housing_prepared)
tree_rmse = root_mean_squared_error(housing_labels, housing_preds)
tree_rmse

# Bad overfitting. There is no error. 
# 
# As we saw earlier, you don't want to touch the test set until you are ready to launch a model you are confident about, so you need to use part of the training set for training and part of it for model validation.


# # **5.2 Better evaluation using cross-validation**
# 
# To evaluate the DT model,
# 
# way 1: use the train_test_split() to split the training set into a smaller training set and a validation set, then train your models against the smaller training set and evaluate them against the validation set.
# a great alternative way: use Scikit-Learn’s K-fold cross-validation feature.


from sklearn.model_selection import cross_val_score


scores = cross_val_score(
    estimator=tree_reg,
    X=housing_prepared,
    y=housing_labels,
    scoring='neg_mean_squared_error',
    cv=10)
tree_rmse_scores = np.sqrt(-scores)

