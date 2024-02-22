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
# streamlit.write(df)

# display the colors in a list
color_list = df[0].values.tolist()
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

# query Snowflake for the image url, price, etc
my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option + "';") 
df2 = my_cur.fetchone() 
# display the product image, etc
streamlit.image( df2[0], width=400, caption= product_caption ) 
streamlit.write('Price: ', df2[1]) 
streamlit.write('Sizes Available: ',df2[2]) 
streamlit.write(df2[3])
