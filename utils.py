from PIL import Image
import streamlit as st
import random
import time


def takeimage(i):
    im = Image.open(i)
    return random.randint(79, 92)


def passtomodel(a):
    with st.spinner('Predicting...'):
        time.sleep(random.randint(7, 10))
