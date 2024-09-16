import streamlit as st
import pandas as pd
import pickle

def main_engine(movie, df,similarity):
    movie_index = df[df['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x: x[1])[1:11]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(df.iloc[i[0]].title)
    return recommended_movies

movies_dataframe = pd.DataFrame(pickle.load(open('./movie_recommendation_system/data/movies_dataframe.pkl','rb')))
vector_tags = pickle.load(open('./movie_recommendation_system/data/vector_tags.pkl','rb'))
similarity_scores = pickle.load(open('D:\DevStudio\Python learning & projects\movie_recommendation_system\data\similarity_scores.pkl','rb'))

st.title('Content Based Movie Recommendation System')
select_movie = st.selectbox('Select your Movie',movies_dataframe['title'].values)

if st.button('Recommend'):
    recommendations = main_engine(select_movie,movies_dataframe,similarity_scores)
    for i in recommendations:
        st.write(i)
