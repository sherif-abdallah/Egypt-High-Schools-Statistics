import streamlit as st
import datetime
import pandas as pd


def form():
    st.set_page_config(page_title='Statistics For High School for scientific and literary', page_icon='icon.png')

    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            button[title="View fullscreen"] {
             display: none;
            }
            button[title="View fullscreen"]:hover {
            display: none;
            }
            summary{
                display: none;
            }
            summary:hover{
                display: none;
            }
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    year = datetime.date.today().year
    title = f"""
            <style>
                .center{{
                    font-size:14px;
                }}
                @media screen and (min-width: 800px) {{
                    .center{{
                        font-size:20px;
                    }}
                }}  
            </style> 
            <center class="center">({year} - {year + 2}) استبيان لطلاب ثانوي عام في مصر</center><br>
            <center><a href="https://forms.gle/fa3e9VuiniYzR68H8" target="_blank">شاركنا في الاستبيان</a></center>
            """
    st.markdown(title, unsafe_allow_html=True)


