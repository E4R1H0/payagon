import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/f205d491-0c13-48d7-a85c-0e2542257f36/EdkWpXCvOK.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello, key="hello")

