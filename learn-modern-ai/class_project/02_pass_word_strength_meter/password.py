

import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits  # 0123456789
    if use_special_chars:
        characters += string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    return ''.join(random.choice(characters) for i in range(length))

st.title("🔒 Password Generator")

# User input controls
length = st.slider("Choose length of password", min_value=6, max_value=12, value=8)
use_digits = st.checkbox("Include digits")
use_special_chars = st.checkbox("Include special characters")

# Generate password on button click
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special_chars)
    st.write(f"**Generated Password:** `{password}`")
    st.write("---")
    st.write("Built with ❤️ by [Erum Azeemi Qaimkhani](https://github.com/erumQaimkhani/password__genrated.git)")