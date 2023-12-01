import streamlit

streamlit.title("My first streamlit app ! :) ")
streamlit.header('Breakfast Menu') 
streamlit.text('🥣 Omega 3 & Oatmeal')
streamlit.text('🥗 Kale, SPinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boilde Free-Rage Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
#create pickup
fruits_selected = streamlit.multiselect("Pick some fruilts:",list(my_fruit_list.index),['Avocado','Strawberries','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display table
streamlit.dataframe(fruits_to_show)
