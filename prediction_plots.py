#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:25:43 2019

@author: marissaeppes
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def prediction_plot(model, training_set, testing_set, p,d,q,P,D,Q,m):
    
    if m == 52:
        freq ='Week'
        lw = 2
    elif m == 12:
        freq = 'Month'
        lw = 4
    else:
        lw = 2
        freq = '(test)'
    
    order = f'({p},{d},{q})'
    seasonal_order = f'({P},{D},{Q},{m})'
    
    predict_train = model.predict()
    predict_test = model.forecast(len(testing_set))
    
    fig = plt.figure(figsize = (20,20))
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    
    ax1.plot(training_set.index,training_set['count'], lw = lw, color = 'mediumturquoise')
    ax1.plot(testing_set.index,testing_set['count'], lw = lw, color = 'blue')
    ax1.plot(training_set.index,predict_train, lw = lw, color = 'magenta')
    
    ax2.plot(training_set.index,training_set['count'], lw = lw, color = 'mediumturquoise')
    ax2.plot(testing_set.index,testing_set['count'], lw = lw, color = 'blue')
    ax2.plot(testing_set.index,predict_test, lw = lw, color = 'orange')
    
    ax1.set_xlabel('Date', fontsize = 20)
    ax1.set_ylabel('Count', fontsize = 20)
    
    ax2.set_xlabel('Date', fontsize = 20)
    ax2.set_ylabel('Count', fontsize = 20)
    
    ax1.set_title(f'Number of Bike Rentals per {freq} Time Series, SARIMA {order}{seasonal_order}', fontsize = 30)
    ax2.set_title(f'Number of Bike Rentals per {freq} Time Series, SARIMA {order}{seasonal_order}', fontsize = 30)
    
    ax1.legend(['Train','Test', 'Model Prediction on Training Set'],prop={'size': 24})
    ax2.legend(['Train','Test', 'Model Prediction on Testing Set'],prop={'size': 24})
    
def forecast_plot(model, master, n_forecast,p,d,q,P,D,Q,m):
    
    if m == 52:
        freq ='Week'
        lw = 2
    elif m == 12:
        freq = 'Month'
        lw = 4
    else:
        lw = 2
    
    order = f'({p},{d},{q})'
    seasonal_order = f'({P},{D},{Q},{m})'
    
    
    fig = plt.figure(figsize = (20,10))
    plt.plot(master.index, master['count'], lw = lw, color = 'mediumorchid')
    
    
    forecast = model.predict(len(master),len(master)+ n_forecast-1)
    
    forecast_dates = pd.date_range(master.index[-1], freq = 'm', periods=n_forecast + 1).tolist()[1:]

    plt.plot(forecast_dates, forecast, lw = 6, color = 'indigo')
    
    plt.xlabel('Date', fontsize = 20)
    plt.ylabel('Count', fontsize = 20)
    plt.legend(['Data','Prediction'],prop={'size': 24})
    plt.title(f'{n_forecast}-{freq} Prediction on Bike Rentals Using SARIMA {order}{seasonal_order}',fontsize = 30)
    
    
    
    
    
def prediction_plot_exog(model, training_df, testing_df, p,d,q,P,D,Q,m):
    
    if m == 52:
        freq ='Week'
        lw = 2
    elif m == 12:
        freq = 'Month'
        lw = 4
    else:
        lw = 2
        freq = '(test)'
    
    order = f'({p},{d},{q})'
    seasonal_order = f'({P},{D},{Q},{m})'
    
    exog_train = np.array([training_df['avg_temp'], training_df['avg_precips']]).T
    exog_test = np.array([testing_df['avg_temp'], testing_df['avg_precips']]).T
    
    predict_train = model.predict(exog = exog_train)
    predict_test = model.forecast(len(testing_df), exog = exog_test)
    
    fig = plt.figure(figsize = (20,20))
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    
    ax1.plot(training_df.index,training_df['count'], lw = lw, color = 'mediumturquoise')
    ax1.plot(testing_df.index,testing_df['count'], lw = lw, color = 'blue')
    ax1.plot(training_df.index,predict_train, lw = lw, color = 'magenta')
    
    ax2.plot(training_df.index,training_df['count'], lw = lw, color = 'mediumturquoise')
    ax2.plot(testing_df.index,testing_df['count'], lw = lw, color = 'blue')
    ax2.plot(testing_df.index,predict_test, lw = lw, color = 'orange')
    
    ax1.set_xlabel('Date', fontsize = 20)
    ax1.set_ylabel('Count', fontsize = 20)
    
    ax2.set_xlabel('Date', fontsize = 20)
    ax2.set_ylabel('Count', fontsize = 20)
    
    ax1.set_title(f'Number of Bike Rentals per {freq} Time Series, SARIMA {order}{seasonal_order}', fontsize = 30)
    ax2.set_title(f'Number of Bike Rentals per {freq} Time Series, SARIMA {order}{seasonal_order}', fontsize = 30)
    
    ax1.legend(['Train','Test', 'Model Prediction on Training Set'],prop={'size': 24})
    ax2.legend(['Train','Test', 'Model Prediction on Testing Set'],prop={'size': 24})
    
def forecast_plot(model, master, n_forecast,p,d,q,P,D,Q,m):
    
    if m == 52:
        freq ='Week'
        lw = 2
    elif m == 12:
        freq = 'Month'
        lw = 4
    else:
        lw = 2
    
    order = f'({p},{d},{q})'
    seasonal_order = f'({P},{D},{Q},{m})'
    
    
    fig = plt.figure(figsize = (20,10))
    plt.plot(master.index, master['count'], lw = lw, color = 'mediumorchid')
    
    
    forecast = model.predict(len(master),len(master)+ n_forecast-1)
    
    forecast_dates = pd.date_range(master.index[-1], freq = 'm', periods=n_forecast + 1).tolist()[1:]

    plt.plot(forecast_dates, forecast, lw = 6, color = 'indigo')
    
    plt.xlabel('Date', fontsize = 20)
    plt.ylabel('Count', fontsize = 20)
    plt.legend(['Data','Prediction'],prop={'size': 24})
    plt.title(f'{n_forecast}-{freq} Prediction on Bike Rentals Using SARIMA {order}{seasonal_order}',fontsize = 30)
       
        
    
    
    


def auto_prediction_plot(automodel, training_set, testing_set):
    
    if automodel.seasonal_order[3] == 52:
        freq ='Week'
        lw = 2
    elif automodel.seasonal_order[3] == 12:
        freq = 'Month'
        lw = 4
    else:
        pass
    
    order = str(automodel.order)
    seasonal_order = str(automodel.seasonal_order)
    
    predict_train = automodel.predict_in_sample()
    predict_test = automodel.predict(len(testing_set))
    
    fig = plt.figure(figsize = (20,20))
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    
    ax1.plot(training_set, lw = lw, color = 'mediumturquoise')
    ax1.plot(testing_set, lw = lw, color = 'blue')
    ax1.plot(training_set.index,predict_train, lw = lw, color = 'magenta')
    
    ax2.plot(training_set, lw = lw, color = 'mediumturquoise')
    ax2.plot(testing_set, lw = lw, color = 'blue')
    ax2.plot(testing_set.index,predict_test, lw = lw, color = 'orange')
    
    ax1.set_xlabel('Date', fontsize = 20)
    ax1.set_ylabel('Count', fontsize = 20)
    
    ax2.set_xlabel('Date', fontsize = 20)
    ax2.set_ylabel('Count', fontsize = 20)
    
    ax1.set_title(f'Number of Bike Rentals per {freq} Time Series, SARIMA {order}{seasonal_order}', fontsize = 30)
    ax2.set_title(f'Number of Bike Rentals per {freq} Time Series, SARIMA {order}{seasonal_order}', fontsize = 30)
    
    ax1.legend(['Train','Test', 'Model Prediction on Training Set'],prop={'size': 24})
    ax2.legend(['Train','Test', 'Model Prediction on Testing Set'],prop={'size': 24})
    
def auto_forecast_plot(automodel, master, n_forecast):
    
    if automodel.seasonal_order[3] == 52:
        freq ='Week'
        lw = 2
    elif automodel.seasonal_order[3] == 12:
        freq = 'Month'
        lw = 4
    else:
        pass
    
    order = str(automodel.order)
    seasonal_order = str(automodel.seasonal_order)
    
    fig = plt.figure(figsize = (20,10))
    plt.plot(master, lw = lw, color = 'mediumorchid')
    
    
    diff = len(master) - len(automodel.predict_in_sample())
    predict_next = automodel.predict(diff + n_forecast)
    forecast = predict_next[-n_forecast:]
    
    forecast_dates = pd.date_range(master.index[-1], freq = 'm', periods=n_forecast + 1).tolist()[1:]

    plt.plot(forecast_dates, forecast, lw = 6, color = 'indigo')
    
    plt.xlabel('Date', fontsize = 20)
    plt.ylabel('Count', fontsize = 20)
    plt.legend(['Data','Prediction'],prop={'size': 24})
    plt.title(f'{n_forecast}-{freq} Prediction on Bike Rentals Using SARIMA {order}{seasonal_order}',fontsize = 30)
    
    
    
        
    
    
    