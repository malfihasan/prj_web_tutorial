'''
dev     : 2024-21-01
author  : Alfi
template: streamlit-basic
'''

## importing libraries
import streamlit as st
import os 
import streamlit_antd_components as sac
from src.contact_me import contact_me
from src.analysis import analysis
from streamlit_lottie import st_lottie
import json
from PIL import Image
from pathlib import Path


## importing lotties gif  https://lottiefiles.com/animation/gif
def open_lottie(lotties_json = "data/sample_01.json"):
    with open(lotties_json, "r") as f:
        animation = json.load(f)
    return animation

def load_css(file_name:str = "style/style.css"):
    ## load csss ##
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



## Page Title ------
st.set_page_config(
    page_title="Streamlit Template 2024",
    page_icon=":world_map:️",
    layout="wide",
)

## Sidebar --------
st.markdown(f'''
    <style>
    .stApp .main .block-container{{
        padding:30px 50px
    }}
    .stApp [data-testid='stSidebar']>div:nth-child(1)>div:nth-child(2){{
        padding-top:50px
    }}
    iframe{{
        display:block;
    }}
    .stRadio div[role='radiogroup']>label{{
        margin-right:5px
    }}
    </style>
    ''', unsafe_allow_html=True)



def load_image(image_name: str) -> Image:
    """Displays an image.

    Parameters
    ----------
    image_name : str
        Local path of the image.

    Returns
    -------
    Image
        Image to be displayed.
    """
    return Image.open(f"{image_name}")

with st.sidebar.container():
    


    st.image(load_image("data/sample_logo.png"), use_column_width=True)

    # title
    # st.subheader(f'Streamlit Template 2024')
    st.markdown("<h1 style='text-align: center;'>Streamlit Template 2024</h1>", unsafe_allow_html=True)

    # menu
    # idea : https://nicedouble-streamlitantdcomponentsdemo-app-middmy.streamlit.app/ 
    menu = sac.menu(
        items=[
            sac.MenuItem('Home', icon='house-fill'),
            sac.MenuItem('Page Set', icon='book', children=[
                sac.MenuItem('Page 1'),
                sac.MenuItem('Page 2'),
            ]),
            sac.MenuItem('Contact',icon='phone', tag='contact')
        ],
        key='menu',
        open_all=False, indent=20,
        format_func='title',
    )

    ## Footer ------

    # footer="""<style>
    # a:link , a:visited{
    # color: blue;
    # background-color: transparent;
    # text-decoration: underline;
    # }

    # a:hover,  a:active {
    # color: red;
    # background-color: transparent;
    # text-decoration: underline;
    # }

    # .footer {
    # position: fixed;
    # left: 0;
    # bottom: 0;
    # width: 100%;
    # background-color: white;
    # color: black;
    # text-align: center;
    # }
    # </style>
    # <div class="footer">
    # <p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.heflin.dev/" target="_blank">Heflin Stephen Raj S</a></p>
    # </div>
    # """

    # st.markdown(footer,unsafe_allow_html=True)


def home():
    load_css()

    ## ----- Header ----- ##
    with st.container():
        st.subheader("Hi I am Alfi !! :wave: ")
        st.title("Welcome to my Streamlit Tutorial :smile:")
        st.write("I am a Data Scientist and a Python Developer. Trying to test my skills in web development using Streamlit.")

    ## ----- What I do ----- ##
    with st.container():
        st.write("-------")
        left_col, right_col = st.columns(2)
        with left_col:
            st.header("What I do :question:")
            st.write("""
                    Trying to open a buisness in Data Science and Python Development.
                    
                    - Data Science :bar_chart:
                    - Python Development :snake:
                    - Web Development :computer:

                    """)
        with right_col:
            animation = open_lottie()
            st_lottie(animation, speed=1, height=200, key="initial")

    ## ----- My Projects ----- ##
    with st.container():
        st.write("-------")
        st.header("My Projects :computer:")
        image_col, text_col = st.columns((1,2))
        with image_col:
            st.image("data/sample_01.jpeg")

        with text_col:
            st.subheader("Project 1 :bar_chart:")
            st.write("""
                    This is a project about data science.
                    """)
            st.markdown("[Link to the project](https://www.google.com)")

    ## ------ Contact Me ------ ##
    with st.container():
        contact_form = """
        <form action="https://formsubmit.co/mdalfihasan19@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="text" placeholder="Student of Knowledge!" required>
            <input type="email" name="email" placeholder="Email of me" required>
            <textarea name="text" placeholder="Random" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_col, right_col = st.columns(2)
        with left_col:
            st.write("-------")
            st.subheader("Contact Form")
            st.markdown(contact_form, unsafe_allow_html=True)

with st.container():

    if menu == 'Home':
        home()
    elif menu == 'Page 1':
        analysis()
    elif menu == 'Page 2':
        analysis()
    elif menu == 'Contact':
        contact_me()

 
