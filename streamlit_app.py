# Import python packages
import streamlit as st
import pandas as pd
from io import StringIO

# Write directly to the app
st.title("Streamlit file uploader")

file = st.file_uploader("upload a file")
if file is not None:
    # To convert to a string based IO:
    stringio = StringIO(file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(file)
    st.write(dataframe)