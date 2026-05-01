import streamlit as st
import pandas as pd
import numpy as np

# Product Sold Data 

vinegar_sold  = pd.DataFrame([{"60mL": 0, "100mL": 0, "200mL": 0, "350mL": 0, "1000mL": 0}], dtype=int)
soy_sauce_sold = pd.DataFrame([{"60mL": 0, "100mL": 0, "200mL": 0, "350mL": 0, "1000mL": 0}], dtype=int)
banana_ketchup_sold = pd.DataFrame([{"25g": 0, "100g": 0, "325g": 0, "550g": 0, "1000g": 0}], dtype=int)

# Product Price List

vinegar_price  = pd.DataFrame([{"60mL": 3.75, "100mL": 6, "200mL": 8.25, "350mL": 18, "1000mL": 45}], dtype=float)
soy_sauce_price = pd.DataFrame([{"60mL": 4.50, "100mL": 6.75, "200mL": 10.75, "350mL": 19.75, "1000mL": 55.50}], dtype=float)
banana_ketchup_price = pd.DataFrame([{"25g": 3.67, "100g": 11, "325g": 27, "550g": 46, "1000g": 72}], dtype=float)

# Script Parameter

with st.sidebar:
    with st.container(border=True):
        st.write("### 🪙 PRICE")
        
        with st.container():
            st.markdown("#### 🎍 Vinegar")
            vinegar_price_editor = st.data_editor(vinegar_price, 
                    column_config={
                        "60mL": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                        "100mL": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                        "200mL": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                        "350mL": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                        "1000mL": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                    },
                    hide_index=True, 
                    key="vinegar_price",
                )
        
        with st.container():
            st.markdown("#### 🫘 Soy Sauce")
            soy_sauce_price_editor = st.data_editor(soy_sauce_price, 
                    column_config={ "60mL": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                        "100mL": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                        "200mL": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                        "350mL": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                        "1000mL": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                    },
                    hide_index=True, 
                    key="soy_sauce_price",
                )
        
        with st.container(): 
            st.markdown("#### 🍌 Banana Ketchup")
            banana_ketchup_price_editor = st.data_editor(banana_ketchup_price, 
                    column_config={
                        "25g": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                        "100g": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                        "325g": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                        "550g": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                        "1000g": st.column_config.NumberColumn(min_value=0, format="₱%.2f"),
                    },
                    hide_index=True, 
                    key="banana_ketchup_price",
                )
    
    with st.container(border=True):
        st.write("### 📈 SOLD")
        
        with st.container():
            st.markdown("#### 🎍 Vinegar")
            vinegar_sold_editor = st.data_editor(vinegar_sold, 
                    column_config={
                        "60mL": st.column_config.NumberColumn(min_value=0),
                        "100mL": st.column_config.NumberColumn(min_value=0),
                        "200mL": st.column_config.NumberColumn(min_value=0),
                        "350mL": st.column_config.NumberColumn(min_value=0),
                        "1000mL": st.column_config.NumberColumn(min_value=0),
                    },
                    hide_index=True, 
                    key="vinegar_sold",
                )

        with st.container():
            st.markdown("#### 🫘 Soy Sauce")
            soy_sauce_sold_editor = st.data_editor(soy_sauce_sold, 
                    hide_index=True, 
                    key="soy_sauce_sold",
                )

        with st.container(): 
            st.markdown("#### 🍌 Banana Ketchup")
            banana_ketchup_sold_editor = st.data_editor(banana_ketchup_sold, 
                    hide_index=True, 
                    key="banana_ketchup_sold",
                )

number_of_split = st.sidebar.number_input(min_value=1, 
        max_value=60, 
        label="Number of Splits", 
        step=1, 
        icon="🧾",
    )

split_now = st.sidebar.button(width="stretch", 
        label="Split", 
        icon="🧾",
    )

# Utility Functions

def drop_zero_columns(data_frame):
    zero_columns = data_frame.columns[(data_frame == 0).all()]
    no_zero_data_frame = data_frame.drop(labels=zero_columns, axis=1) 

    return no_zero_data_frame

def find_highest_number_of_split(vinegar_sold_data, soy_sauce_sold_data, banana_ketchup_sold_data):
    highest_number_of_split = 0
  
    values_array = []

    values_array.append(vinegar_sold_data.values.tolist()[0])
    values_array.append(soy_sauce_sold_data.values.tolist()[0])
    values_array.append(banana_ketchup_sold_data.values.tolist()[0])
    
    for values in values_array:
        for value in values:
            if value > highest_number_of_split:
                highest_number_of_split = value
    
    if highest_number_of_split == 0:
        highest_number_of_split = "None" 


    return highest_number_of_split

def split_value(x, split_size):
    splitted_value = np.zeros(split_size) 

    while sum(splitted_value) != x:
        for i in range(split_size):
            if sum(splitted_value) != x:
                splitted_value[i] = splitted_value[i] + 1

    return splitted_value.tolist()

def get_product_price(product_name, product_size, product_sold):
    match(product_name):
        case "VINEGAR":
            return vinegar_price_editor[product_size].item() * product_sold
        case "SOY SAUCE": 
            return soy_sauce_price_editor[product_size].item() * product_sold
        case "BANANA KETCHUP":
            return banana_ketchup_price_editor[product_size].item() * product_sold

def split_product_dictionary(product_dictionary, number_of_split, product_name):
    if product_dictionary == None:
        return None

    splitted_product_array = []

    for key, value in product_dictionary.items(): 
        splitted_value = split_value(value, number_of_split)
       
        splitted_product_size = []
        
        for value in splitted_value:
            splitted_product_dictionary = {}
            splitted_product_dictionary["PRODUCT_NAME"] = product_name
            splitted_product_dictionary["PRODUCT_SIZE"] = key 
            splitted_product_dictionary["QUANTITY"] = value
            splitted_product_dictionary["PRICE"] = get_product_price(product_name, key, value)
    
            splitted_product_size.append(splitted_product_dictionary)

        splitted_product_array.append(splitted_product_size)

    return splitted_product_array 

def distribute_splitted_sold_dictionaries(number_of_split, splitted_sold_dictionaries):
    distributed_splitted_product_sold = []
    
    for i in range(number_of_split):
        distributed_products = []
        
        for product in range(len(splitted_sold_dictionaries)):
            if splitted_sold_dictionaries[product] == None:
                continue

            for product_size in splitted_sold_dictionaries[product]:
                distributed_products.append(product_size[i])
        
        distributed_splitted_product_sold.append(distributed_products)

    return distributed_splitted_product_sold

# Script Main Function

vinegar_sold_data = drop_zero_columns(vinegar_sold_editor)
soy_sauce_sold_data = drop_zero_columns(soy_sauce_sold_editor)
banana_ketchup_sold_data = drop_zero_columns(banana_ketchup_sold_editor)

highest_number_of_split = find_highest_number_of_split(vinegar_sold_data, 
            soy_sauce_sold_data, 
            banana_ketchup_sold_data)

def split(n=number_of_split):
    if type(highest_number_of_split) == str:
        st.sidebar.warning("Error: No Product Sold!", icon="🚨")
        return

    if n > highest_number_of_split: 
        st.sidebar.warning(f"Error: Valid Number of Split n<{highest_number_of_split + 1}", icon="🚨")
        return

    try:
        vinegar_sold_dictionary = vinegar_sold_data.to_dict(orient="records")[0] 
    except IndexError:
        vinegar_sold_dictionary = None
    
    try:
        soy_sauce_sold_dictionary = soy_sauce_sold_data.to_dict(orient="records")[0] 
    except IndexError:
        soy_sauce_sold_dictionary = None

    try:
        banana_ketchup_sold_dictionary = banana_ketchup_sold_data.to_dict(orient="records")[0] 
    except IndexError:
        banana_ketchup_sold_dictionary = None

    vinegar_sold_dictionaries = split_product_dictionary(vinegar_sold_dictionary, n, "VINEGAR")
    soy_sauce_sold_dictionaries = split_product_dictionary(soy_sauce_sold_dictionary, n, "SOY SAUCE")
    banana_ketchup_sold_dictionaries = split_product_dictionary(banana_ketchup_sold_dictionary, n, "BANANA KETCHUP") 

    splitted_sold_dictionaries = []
    splitted_sold_dictionaries.append(vinegar_sold_dictionaries)
    splitted_sold_dictionaries.append(soy_sauce_sold_dictionaries)
    splitted_sold_dictionaries.append(banana_ketchup_sold_dictionaries)

    distributed_splitted_sold_dictionaries = distribute_splitted_sold_dictionaries(n, splitted_sold_dictionaries)
     
    invoices_prices = []

    for invoice in range(n):
        with st.container(border=True):
            st.markdown(f"### 🧾 Invoice {invoice + 1}")
            
            product_data = pd.DataFrame(distributed_splitted_sold_dictionaries[invoice])
            filtered_product_data = product_data[product_data["QUANTITY"] != 0]
            
            st.dataframe(filtered_product_data, hide_index=True, column_config = {
                "PRODUCT_NAME": st.column_config.Column(alignment="center"),
                "PRODUCT_SIZE": st.column_config.Column(alignment="center"),
                "QUANTITY": st.column_config.Column(alignment="center"),
                "PRICE": st.column_config.NumberColumn(alignment="center", format="₱%.2f"),
            })

            st.markdown(f"**TOTAL: ₱{sum(filtered_product_data["PRICE"]):.2f}**", text_alignment="right")
            invoices_prices.append(sum(filtered_product_data["PRICE"]))

    invoices_total_price = sum(invoices_prices)
    
    st.markdown(f"**TOTAL: ₱{invoices_total_price:.2f}**", text_alignment="center")

if split_now:
    split()

