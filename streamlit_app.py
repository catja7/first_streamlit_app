import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#Auswahlliste
fruits_selected = streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    #take the json version of the response an normalize it
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#new section to import fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would You like Information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    #output as a table
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
  
#streamlit.write('The User entered', fruit_choice)




#streamlit.text(fruityvice_response.json()) # just writes the data to the screen



streamlit.stop()

#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


# new text entry box
streamlit.header(' new text entry box')
fruit_add = streamlit.text_input('What fruit would You like to add?', 'Kiwi')
streamlit.write('Thanks for adding', fruit_add)

my_cur.execute("insert into fruit_load_list values('from streamlit')")
import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_add)
#streamlit.text(fruityvice_response.json()) # just writes the data to the screen
