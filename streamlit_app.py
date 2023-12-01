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

#create pickup
streamlit.multiselect("Pick some fruilts:",list(my_fruit_list.index ))

#display table
streamlit.dataframe(my_fruit_list)
