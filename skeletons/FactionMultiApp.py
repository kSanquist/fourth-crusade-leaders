import streamlit as st
from streamlit_option_menu import option_menu
import abc


class FactionMultiApp:
    def __init__(self, title: str, icon=None, sidebar="auto", layout="wide"):
        st.set_page_config(
            page_title=title,
            page_icon=icon,
            initial_sidebar_state=sidebar,
            layout=layout
        )

    def run(self, options_list, sidebar_w: int):
        with st.sidebar:
            option = option_menu(  # Adds options to option menu
                menu_title="",
                options=options_list
            )
        st.markdown(  # Sets width of sidebar to width of largest String in options_list
            f"""
            <style>
                section[data-testid="stSidebar"] {{
                    width: {sidebar_w}px !important;
                }}
            </style>
            """,
            unsafe_allow_html=True
        )
        self.get_option(option)

    @abc.abstractmethod
    def get_option(self, option):
        st.toast("No option implementations!")


