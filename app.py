import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x: x[1]) [1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.markdown("<h1>Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<h4>Made By: Vraj Shah</h4>", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
'How would you like to be connected',
movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)