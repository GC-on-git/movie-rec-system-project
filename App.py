import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    api_key = #find and set api key from tmdb website
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def fetch_link(movie_id):
    movie_page_link = f"https://www.themoviedb.org/movie/{movie_id}"

    return movie_page_link

def recommend(movie):
    movie_index = movies[movies.title == movie].index[0]
    distance = similar[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]


    rec_movie_names = []
    rec_movie_posters = []
    rec_movie_links=[]

    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        movie_names = movies.iloc[i[0]].title
        rec_movie_posters.append(fetch_poster(movie_id))
        rec_movie_names.append(movie_names)
        rec_movie_links.append(fetch_link(movie_id))




    return rec_movie_names,rec_movie_posters,rec_movie_links


st.header('Movie Recommender System')
movies = pickle.load(open('movies_list.pkl','rb'))
similar = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters,recommended_movie_links = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        text1=recommended_movie_names[0]
        url1=recommended_movie_links[0]
        st.markdown(f"{text1} [link]({url1})", unsafe_allow_html=True)
        st.image(recommended_movie_posters[0])
    with col2:
        text2 = recommended_movie_names[1]
        url2 = recommended_movie_links[1]
        st.markdown(f"{text2} [link]({url2})", unsafe_allow_html=True)
        st.image(recommended_movie_posters[1])

    with col3:
        text3=recommended_movie_names[2]
        url3=recommended_movie_links[2]
        st.markdown(f"{text3} [link]({url3})", unsafe_allow_html=True)
        st.image(recommended_movie_posters[2])
    with col4:
        text4=recommended_movie_names[3]
        url4=recommended_movie_links[3]
        st.markdown(f"{text4} [link]({url4})", unsafe_allow_html=True)
        st.image(recommended_movie_posters[3])
    with col5:
        text5=recommended_movie_names[4]
        url5=recommended_movie_links[4]
        st.markdown(f"{text5} [link]({url5})", unsafe_allow_html=True)
        st.image(recommended_movie_posters[4])




