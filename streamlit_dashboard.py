import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors

#df = pd.read_csv('test_over500.csv')
#df = pd.read_csv('test_over500_USnonUS.csv')
#df = pd.read_csv('test_over500_over5translation.csv')
df = pd.read_csv('maxi_filtered_df3000.csv')
df_US = df[df['origin']=='US']
df_NoUS = df[df['origin']=='Not US']
#Presentation of the dataframe
dashboard = st.sidebar.radio(
    "What dashboard do you want to see ?",
    ('Data visualisation', 'Our recommandation algorithm'))

if dashboard == 'Data visualisation':
     st.write('Not done yet')
elif dashboard == 'Our recommandation algorithm':
    st.title('Welcome to our recommandation algorithm page !')
    # Recommandation algorithm page     
    movie_title = st.selectbox("Please enter your favourite movie's title : ", (list(df['originalTitle'])))    
    num_sim = st.slider('How many similar movies do you want to see?', 1, 10, 5)
    database = st.radio(
    "Select the database to explore :",
    ('Anglophone', 'Non Anglophone', 'All'))
    
    if database == 'Anglophone':
        columns_of_interest = ['isAdult', 'runtimeMinutes', 'averageRating'] + list(df.iloc[:, -26:-4].columns)
        X= df_US[columns_of_interest]
        distanceKNN = NearestNeighbors(n_neighbors = num_sim+1).fit(X)
        coord = distanceKNN.kneighbors(df.loc[df['originalTitle']==movie_title, columns_of_interest])
        for i in range(1, num_sim+1):
            st.write('TOP', i, ':' , df_US['originalTitle'].iloc[coord[1][0][i]],'(',str(df_US['startYear'].iloc[coord[1][0][i]]),')')   
    elif database == 'Non Anglophone':
        columns_of_interest = ['isAdult', 'runtimeMinutes', 'averageRating'] + list(df.iloc[:, -26:-4].columns)
        X= df_NoUS[columns_of_interest]
        distanceKNN = NearestNeighbors(n_neighbors = num_sim+1).fit(X)
        coord = distanceKNN.kneighbors(df.loc[df['originalTitle']==movie_title, columns_of_interest])
        for i in range(1, num_sim+1):
            st.write('TOP', i, ':' , df_NoUS['originalTitle'].iloc[coord[1][0][i]],'(',str(df_NoUS['startYear'].iloc[coord[1][0][i]]),')')   
    else : 
        columns_of_interest = ['isAdult', 'runtimeMinutes', 'averageRating'] + list(df.iloc[:, -26:-4].columns)
        X= df[columns_of_interest]
        distanceKNN = NearestNeighbors(n_neighbors = num_sim+1).fit(X)
        coord = distanceKNN.kneighbors(df.loc[df['originalTitle']==movie_title, columns_of_interest])
        for i in range(1, num_sim+1):
            st.write('TOP', i, ':' , df['originalTitle'].iloc[coord[1][0][i]],'(',str(df['startYear'].iloc[coord[1][0][i]]),')')