import streamlit as st
import pickle
import pandas as pd


def recommend(serie):
    index = series[series['Series_Title'] == serie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_series = []
    for i in movie_list:
        series_info = series[series['id'] == i[0]]
        recommended_series.append({
            'Series_Title': series_info['Series_Title'].values[0],
            'Poster_Link': series_info['Poster_Link'].values[0]
        })

    return recommended_series


series_dict = pickle.load(open('series.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
series = pd.DataFrame(series_dict)
st.title("Series Recommender System")

selected_series_name = st.selectbox(
    'Which Series recommendation do you want?',
    series['Series_Title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_series_name)
    st.write("### Recommended Series")

    cols = st.columns(5)  # Create 5 columns for displaying recommended series
    for idx, rec in enumerate(recommendations):
        with cols[idx]:
            st.image(rec['Poster_Link'], caption=rec['Series_Title'], use_column_width=True)
