import streamlit as st
import pandas as pd
import pickle
import base64
import requests
import json

def extract_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a7d35fbd6d62607f63c94bbd2206420e&language=en-US'.format(movie_id))
    poster_path = response.json()['poster_path']

    return 'https://image.tmdb.org/t/p/w500/' + poster_path

# Function to set the background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def main_engine(movie, df,similarity,n):
    movie_index = df[df['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x: x[1])[1:n+1]

    recommended_movies = []
    movie_posters = []
    for i in movies_list:
        recommended_movies.append(df.iloc[i[0]].title)
        movie_posters.append(extract_poster(df.iloc[i[0]].movie_id))
    return recommended_movies,movie_posters

movies_dataframe = pd.DataFrame(pickle.load(open('./movie_recommendation_system/data/movies_dataframe.pkl','rb')))
similarity_scores = pickle.load(open('D:\DevStudio\Python learning & projects\movie_recommendation_system\data\similarity_scores.pkl','rb'))

# code for background image
image_path = "./movie_recommendation_system/data/movie_background.jpg"
add_bg_from_local(image_path)

st.title('Content Based Movie Recommendation System')
select_movie = st.selectbox('Select your Movie',movies_dataframe['title'].values)
n = st.number_input('Number of recommendations', min_value=1, max_value=20, value=10)

if st.button('Recommend'):
    recommendations,posters = main_engine(select_movie,movies_dataframe,similarity_scores,n)
    for i in range(n) :
        st.image(posters[i])
        st.text(recommendations[i])
