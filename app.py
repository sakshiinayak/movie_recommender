import pandas as pd
import streamlit as st
import pickle

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)

st.title('movie recommender')

selected_movie_name =st.selectbox('which movie would u like to choose?',movies['title'].values)

if st.button('recommend'):
    recommendations= recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
