import streamlit as st
import utils
#from tensorflow import keras
#from keras.models import load_model

st.set_page_config(layout="wide")

st.title("Damage Estimation using Satellite Imagery")

#model = load_model("model.h5")

temp = st.file_uploader("Upload an image", type=[
                        "png", "jpg", "jpeg"])

if temp:
    est = utils.takeimage(temp)
    col1, mid, col2 = st.columns([5, 1, 5])
    with col1:
        st.image(temp, width=350)
    with col2:
        st.subheader('Damage Estimation')
        utils.passtomodel(est)
        st.subheader('{}%'.format(est))
