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

# display the data in a dataframe
df = pandas.DataFrame(my_catalog)
streamlit.write(df)
