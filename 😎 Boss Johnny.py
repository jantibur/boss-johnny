import streamlit as st

def main():
    st.set_page_config(
        page_title="Boss Johnny",
        page_icon="😎",
    )
    
    st.title("😎 Boss Johnny")

    st.sidebar.success("Select the tool above")

    st.write("A simple tool for simple and repetitive task.")
    st.markdown("**Choose the tool in the left sidebar**")

if __name__ == "__main__":
    main()

