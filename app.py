import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies_lists[movies_lists['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    
    top_movies = []
    for i in movie_list:
        top_movies.append(movies_lists.iloc[i[0]])
    
    return top_movies[1:6]

movies_lists = pickle.load(open('movies.pkl', 'rb'))
lists = movies_lists['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('The movie recommender system')

movie_name = st.selectbox('Which movie do you want to search?', lists)

if st.button('Recommend'):
    recommendations = recommend(movie_name)
    for movie in recommendations:
        st.write(movie['title'])