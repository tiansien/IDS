import streamlit as st
from home import show_home
from page1 import show_page1
from page2 import show_page2

def main():
    st.sidebar.title("Navigation to More")
    pages = {
        "🏫 Home": show_home,
        "😊 Normal Hepler": show_page1,
        "😷 Professional Assistant": show_page2
    }
    selected_page = st.sidebar.radio("Go to", list(pages.keys()))
    pages[selected_page]()

if __name__ == "__main__":
    main()
