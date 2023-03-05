import random
import string
import re
import streamlit as st

def generate_password(length: int, include_symbols: bool = True, include_numbers: bool = True,
                      include_lowercase: bool = True, include_uppercase: bool = True,
                      exclude_similar: bool = True, exclude_ambiguous: bool = True) -> str:
    # Define character sets
    symbols = "@#$%&*-_+=?"
    numbers = "1234567890"
    lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
    uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    excluded_chars = "il1Lo0O{}[]()/\\'\"`~,;:.<>"

    # Remove excluded characters from character sets
    if exclude_similar:
        symbols = symbols.translate(str.maketrans('', '', 'O0o'))
        numbers = numbers.translate(str.maketrans('', '', 'il1Lo0O'))
        lowercase_chars = lowercase_chars.translate(str.maketrans('', '', 'il1Lo0O'))
        uppercase_chars = uppercase_chars.translate(str.maketrans('', '', 'il1Lo0O'))

    if exclude_ambiguous:
        symbols = symbols.replace("@", "")
        numbers = numbers.replace("1", "")
        lowercase_chars = lowercase_chars.replace("l", "").replace("i", "")
        uppercase_chars = uppercase_chars.replace("I", "").replace("L", "")

    # Select character sets based on user's choices
    char_set = ""
    if include_symbols:
        char_set += symbols
    if include_numbers:
        char_set += numbers
    if include_lowercase:
        char_set += lowercase_chars
    if include_uppercase:
        char_set += uppercase_chars

    # Generate password
    password = ""
    for i in range(length):
        password += random.choice(char_set)

    return password


def password_generator():
    st.set_page_config(page_title="Password Generator!!", page_icon=":closed_lock_with_key:", layout="wide")
    # add a title to the app
    
    st.title("Password Generator :closed_lock_with_key:")
    st.write("This is a simple application that helps you to create/generate best passwords using Python.")
    with st.expander('Password Options'):
        # Get user input
        length = st.slider("Password Length", 6, 2048, 12, 1)
        include_symbols = st.checkbox("Include Symbols (e.g. @#$%)")
        include_numbers = st.checkbox("Include Numbers (e.g. 1234567890)")
        include_lowercase = st.checkbox("Include Lowercase Characters (e.g. a-z)")
        include_uppercase = st.checkbox("Include Uppercase Characters (e.g. A-Z)")
        exclude_similar = st.checkbox("Exclude Similar Characters (e.g. i, l, 1, L, o, 0, O)")
        exclude_ambiguous = st.checkbox("Exclude Ambiguous Characters (e.g. { } [ ] ( ) / \\ \' \" ` ~ , ; : . < > )")

    # Generate and print password
    if st.button("Generate Password"):
        password = generate_password(length, include_symbols, include_numbers, include_lowercase, include_uppercase, exclude_similar, exclude_ambiguous)
        
        # Calculate the number of lines needed to display the password
        num_lines = (len(password) // 50) + 1  # Assuming 50 characters per line
        
        # Set the height of the text area based on the number of lines
        height = min(600, max(100, num_lines * 20))  # Minimum height of 100 and maximum height of 600, with 20 pixels per line
        
        # Display the generated password
        st.text_area("Generated Password: ", value=password, height=height)

password_generator()
