import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Essen01')
streamlit.text('Essen02')
streamlit.text('Essen03')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('\N{baby bottle}')
streamlit.text('\N{bottle with popping cork}')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#Auswahlliste
streamlit.multiselect("pick some fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
