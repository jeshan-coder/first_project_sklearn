#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:06:57 2025

@author: jeshan
"""
from datapreprocessing import Xdf,Ydf

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer

categorical_columns=['blue', 'dual_sim', 'four_g', 'three_g', 'touch_screen', 'wifi']

# y values mapping
dict_for_mapping={'high':0,'low':1,'medium':2,'very_high':3}

Ydf=Ydf.map(dict_for_mapping)


X_train,X_test,Y_train,Y_test=train_test_split(Xdf,Ydf,train_size=0.7)

#making pipeline

#knn imputer

from sklearn.impute import KNNImputer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer #if you want to do some encoding in particular columns
from sklearn.ensemble import RandomForestClassifier

#------------------------------------pipeline for random forest---------------------------------------------------------
model_pipeline=Pipeline(
    [
     
     ("transform_encoder",ColumnTransformer(
         transformers=[
             ("encoder",OrdinalEncoder(),categorical_columns)
             ],
         remainder='passthrough'
         )),
     ('imputer',KNNImputer()),
     ('model',RandomForestClassifier())
     ])


#fit to pipeline
model_pipeline.fit(X_train,Y_train)


#calculate score
from sklearn.metrics import classification_report
predicted=model_pipeline.predict(X_test)

score=classification_report(Y_test,predicted)

#now, make dataframe of predicted and actual
import pandas as pd
df_test=pd.DataFrame({'Actual':Y_test,'Predicted':predicted})


#map 1,2,3 into labels of y
labeling_map={0:'high',1:'low',2:'medium',3:'very_high'}

#now, label df_test
df_test['Actual']=df_test['Actual'].map(labeling_map)
df_test['Predicted']=df_test['Predicted'].map(labeling_map)


#save model to directory
import pickle
save_main_path="/home/jeshan/intern_projects/first_project_sklearn/models/"
model_name="random_forest"
file = open(save_main_path+model_name+".pkl", 'wb')
pickle.dump(model_pipeline, file)



#------------------------------------ pipeline for support vector---------------------------------------------------------
from sklearn.svm import SVC
model_pipeline=Pipeline(
    [
     
     ("transform_encoder",ColumnTransformer(
         transformers=[
             ("encoder",OrdinalEncoder(),categorical_columns)
             ],
         remainder='passthrough'
         )),
     ('imputer',KNNImputer()),
     ('model',SVC())
     ])


#fit to pipeline
model_pipeline.fit(X_train,Y_train)


#calculate score
from sklearn.metrics import classification_report
predicted=model_pipeline.predict(X_test)

score_svc=classification_report(Y_test,predicted)

#now, make dataframe of predicted and actual
import pandas as pd
df_test=pd.DataFrame({'Actual':Y_test,'Predicted':predicted})


#map 1,2,3 into labels of y
labeling_map={0:'high',1:'low',2:'medium',3:'very_high'}

#now, label df_test
df_test['Actual']=df_test['Actual'].map(labeling_map)
df_test['Predicted']=df_test['Predicted'].map(labeling_map)


#save model to directory
import pickle
save_main_path="/home/jeshan/intern_projects/first_project_sklearn/models/"
model_name="svc"
file = open(save_main_path+model_name+".pkl", 'wb')
pickle.dump(model_pipeline, file)







