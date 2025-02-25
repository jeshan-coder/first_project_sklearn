#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:30:17 2025

@author: jeshan
"""
import pickle
import numpy as np
import pandas as pd
def load_model(path:str)-> any:
    """
    Arguments:
        path: path of model where you have saved pickle file
    """
    file=open(path,'rb')
    model=pickle.load(file)
    return model

def get_result(label:int)-> str:
    if 0:
        return 'high'
    if 1:
        return 'low'
    if 2:
        return 'medium'
    if 3:
        return 'very_high'

def inference(data: np.array)-> str:
    model=load_model("/home/jeshan/intern_projects/first_project_sklearn/models/random_forest.pkl")
    
    predicted=model.predict(data)
    result=get_result(predicted[0])
    print(result)
    return result

#{0:'high',1:'low',2:'medium',3:'very_high'}
        

    