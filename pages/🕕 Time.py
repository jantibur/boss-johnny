import streamlit as st
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import io
from random import randint
from datetime import datetime

# Constants 

cities = [
    "Cabanatuan City",
    "Bongabon",
    "Sta. Rosa",
    "Pantabangan",
    "Rizal",
    "Laur",
    "Gabaldon",
    "Palayan",
    "Dingalan", # Aurora
    "Alfonso", # Nueva Vizcaya
    "Tarlac City" # Tarlac
]

# Utilities

def get_province(city):
    match(city):
        case "Dingalan":
            return "Aurora"
        case "Alfonso":
            return "Nueva Vizcaya"
        case "Tarlac City":
            return "Tarlac"
        case _:
            return "Nueva Ecija"

# Script Parameter

with st.sidebar:
    with st.container(border=True):
        st.markdown("### 📆 Chronos")
        with st.container():
            date_data = st.date_input(label="Date", format="DD/MM/YYYY")
            time_data = st.time_input(label="Time", step=60)

with st.sidebar:
    with st.container(border=True):
        st.markdown("### 📍 Location")
        with st.container():
            city_data = st.selectbox(label="City", options=cities)
            province_data = get_province(city_data)
            st.caption(province_data)

process_now = st.sidebar.button(label="Process", icon="🧠", width="stretch")

uploaded_image = st.file_uploader(label="Image Upload", type=["jpg", "jpeg", "png"])

def process_image():
    if uploaded_image is None:
        st.sidebar.warning("Error: No Image is Uploaded!", icon="🚨")
        return
    

    image = Image.open(uploaded_image)
    image_width, image_height = image.size

    time_data_with_fake_seconds = str(time_data)[:6] + str(randint(10, 60))


    updated_date = date_data.strftime("%d %b %Y")
    
    time_data_object = datetime.strptime(time_data_with_fake_seconds, "%H:%M:%S")

    updated_time = time_data_object.strftime("%I:%M:%S %P")

    date_time_data = f"{updated_date} {updated_time}"

    font_size = 42

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("NotoSans-Regular.ttf", font_size)  
   
    central_luzon_width = draw.textlength("Central Luzon", font=font)
    province_width = draw.textlength(province_data, font=font)
    city_width = draw.textlength(city_data, font=font)
    date_time_width = draw.textlength(date_time_data, font=font)

    image_margin = 8

    central_luzon_x = image_width - central_luzon_width - image_margin
    province_x = image_width - province_width - image_margin
    city_x = image_width - city_width - image_margin 
    date_time_x = image_width - date_time_width - image_margin

    central_luzon_y = image_height - font_size - image_margin * 1.5
    province_y = image_height - font_size * 2 - image_margin * 3
    city_y = image_height - font_size * 3 - image_margin * 4.25
    date_time_y = image_height - font_size * 4 - image_margin * 5.35 


    draw.text((central_luzon_x, central_luzon_y), "Central Luzon", (255, 255, 255), font=font) 
    draw.text((province_x, province_y), province_data, (255, 255, 255), font=font)
    draw.text((city_x, city_y), city_data, (255, 255, 255), font=font)
    draw.text((date_time_x, date_time_y), date_time_data, (255, 255, 255), font=font)


    processed_image = io.BytesIO()
    image.save(processed_image, format="JPEG")

    st.image(processed_image.getvalue())

    st.download_button(label="Download Processed Image", data=processed_image, 
            file_name=f"{updated_date}:{updated_time}.jpg", width="stretch")

if process_now:
    process_image() 
