## Functions
from sklearn import preprocessing
import pandas as pd
import numpy as np
import copy
import os 


"""Func Manual
모든 함수는 copy.deepcopy() 메소드를 활용하여 원본 dataframe 에 영향이 가지 않도록 설정
drop_features : c1~c10 까지(10개)의 컬럼과 dataframe 을 인자로 받아 c1~c10 컬럼을 drop 하는 함수
column_group : c2 를 c1 클래스로 평균-그룹핑하여 c3 인자값의 이름으로 컬럼을 생성, method="group_mean"(default) 
fillna_int : c1~c10 까지(10개)의 컬럼과 dataframe 을 인자로 받아 int type c1~c10 컬럼을 fillna 하는 함수, method="mean"(default)
fillna_oto : c1 의 컬럼상에 존재하는 NaN 값을 c2 컬럼의 rows 에 해당하는 값으로 replace 하는 함수, method="oto"(default)
fillna_str : c1~c10 까지(10개)의 컬럼과 dataframe 을 인자로 받아 str type c1~c10 컬럼을 fillna 하는 함수, method="mode"(default)
fillna_str2 : c1~c10 까지(10개)의 컬럼과 dataframe 을 인자로 받아 str type c1~c10 컬럼을 사용자 정의대로 fillna 하는 함수
get_outlier : dataframe 의 outlier 상하 기준과 outlier에 해당하는 index 번호와 value를 반환하는 함수, weight=1.5(default)
transform_outlier : dataframe의 outlier를 상하 기준에 맞추어 상하기준값으로 replace 하는 함수, method="both"(default)

#Visualizing functions are in 'Kaggle_Titanic.ipynb' script
"""




def drop_features(dataframe, c1="default", c2="default", c3="default", c4="default", c5="default",\
                  c6="default", c7="default", c8="default", c9="default", c10="default"):
    
    """
    c1~c10 = Column names droppping
    """
    
    df=copy.deepcopy(dataframe)
    colnames = [i for i in df.columns]
    bin=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
    
    for i in bin:
        if i != "default":
            if i in colnames:
                df.drop([i], axis=1, inplace=True)
            else:
                print("Operation failed with value %s : Check out your Dataframe or value" %i)
    return df



def column_group(dataframe, method="group_mean", c1="default", c2="default", c3="default"):
    
    """
    c1 = grouping index
    c2 = grouping object
    c3 = Column name created
    """
    
    df=copy.deepcopy(dataframe)
    colnames = [i for i in df.columns]
    
    if c1 != "default":
        if method=="group_mean":
            if c1 in colnames:
                df[c3] = df.groupby([c1])[c2].transform('mean')
            else:
                print("Operation failed with value %s : Check out your Dataframe or value" %i)      

    return df 



def fillna_int(dataframe, method="mean", c1="default", c2="default", c3="default", c4="default", c5="default",\
               c6="default", c7="default", c8="default", c9="default", c10="default"):
    
    """
    c1~c10 = Column names to 'fillna' work
    method = mean, mode
    """
    
    df=copy.deepcopy(dataframe)
    colnames = [i for i in df.columns]
    bin=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
    
    for i in bin:
        if i != "default":
            if method=="mean":
                if i in colnames:
                    df[i].fillna(df[i].mean(), inplace=True)
                else:
                    print("Operation failed with value %s : Check out your Dataframe or value" %i)              
                    
            if method=="mode":
                if i in colnames:
                    df[i].fillna(df[i].mode(), inplace=True)
                else:
                    print("Operation failed with value %s : Check out your Dataframe or value" %i)
    return df
   
                   
    
    
def fillna_oto(dataframe, method="oto", c1="default", c2="default"):
    
    """
    method = oto --> one to one
    c1 = Column name to 'fillna' work
    c2 = index column to 'fillna' work
    """
    
    df=copy.deepcopy(dataframe)
    colnames = [i for i in df.columns]
    
    if c1 != "default":
        if method=="oto":
            if c1 in colnames:
                df[c1].fillna(round(df[c2]), inplace=True)
            else:
                print("Operation failed with value %s : Check out your Dataframe or value" %i)      

    return df    



def fillna_str(dataframe, method="mode", c1="default", c2="default", c3="default", c4="default", c5="default",\
               c6="default", c7="default", c8="default", c9="default", c10="default"):
    
    """
    method = mode
    c1~c10 = Column names to 'fillna' work
    """
    
    df=copy.deepcopy(dataframe)
    colnames = [i for i in df.columns]
    bin=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
    
    for i in bin:
        if i != "default":
            if method=="mode":
                if i in colnames:
                    df[i].fillna(df[i].value_counts().idxmax(), inplace=True)
                else:
                    print("Operation failed with value %s : Check out your Dataframe or value" %i)
    return df


def fillna_str2(dataframe, value="User_Defined", c1="default", c2="default", c3="default", c4="default", c5="default",\
                c6="default", c7="default", c8="default", c9="default", c10="default"):
    
    """
    value = 'User_Defined' --> you can designate the word to 'fillna work'
    c1~c10 = Column names to 'fillna' work
    """
    
    df=copy.deepcopy(dataframe)
    colnames = [i for i in df.columns]
    bin=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
    
    for i in bin:
        if i != "default":
            if i in colnames:
                df[i].fillna(value, inplace=True)
            else:
                print("Operation failed with value %s : Check out your Dataframe or value" %i)
    return df




def get_outlier(dataframe=None, column=None, weight=1.5):
    df=copy.deepcopy(dataframe)
    
    #Object
    var1 = df[column]
    
    #25%, 75%  #numpy value ---> percentage
    quantile_25 = np.percentile(var1.values,25)
    quantile_75 = np.percentile(var1.values,75)
    
    #iqr
    iqr = quantile_75 - quantile_25
    iqr_weight = iqr *weight
    lowest_standard = quantile_25 - iqr_weight
    highest_standard = quantile_75 + iqr_weight
    
    #conditions
    outlier_index = var1[(var1<lowest_standard)|(var1>highest_standard)].index
    highest_index = var1[(var1>highest_standard)].index
    lowest_index = var1[(var1<lowest_standard)].index
    
    #Print options
    print("<Outliers>")
    print("highest_standard :", highest_standard)
    print("lowest_standard :", lowest_standard, end='\n\n')
    print("Count of outlier values :",len(outlier_index))    
    print(df[column][outlier_index])
    
    #Return
    return outlier_index, highest_index, lowest_index, highest_standard, lowest_standard 
    

def transform_outlier(dataframe=None, method="both", column=None, weight=1.5):
    df=copy.deepcopy(dataframe)
    
    #get values from funcion : get_outlier
    x, index1, index2, high_val, low_val = get_outlier(dataframe=df, column=column, weight=weight)
    
    if method=="both":
        df[column].iloc[index1] = high_val
        df[column].iloc[index2] = low_val
    if method=="high":
        df[column].iloc[index1] = high_val  #highest index
    if method=="low":
        df[column].iloc[index2] = low_val  #lowest index    
        
    return df