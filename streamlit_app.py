import streamlit
import snowflake.connector
import pandas

# title for the web app
streamlit.title("Zena's Amazing Athleisure Catalog")

# connect to Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"]) 
my_cur = my_cnx.cursor() 

# query snowflake to get colors and styles
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

# get the data into a dataframe
df = pandas.DataFrame(my_catalog)
streamlit.write(df)

# display the colors in a list
color_list = df[0].values.tolist()
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))
