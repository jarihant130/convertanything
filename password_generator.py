import random
import string
import streamlit as st

def generate_password(length, include_symbols=True, include_numbers=True, include_lowercase=True, include_uppercase=True, exclude_similar=True, exclude_ambiguous=True):
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
    # Create a Streamlit app
    st.title("Password Generator")
    st.sidebar.header("Password Options")

    # Get user input
    length = st.sidebar.slider("Password Length", 6, 2048, 12, 1)
    include_symbols = st.sidebar.checkbox("Include Symbols")
    include_numbers = st.sidebar.checkbox("Include Numbers")
    include_lowercase = st.sidebar.checkbox("Include Lowercase Characters")
    include_uppercase = st.sidebar.checkbox("Include Uppercase Characters")
    exclude_similar = st.sidebar.checkbox("Exclude Similar Characters")
    exclude_ambiguous = st.sidebar.checkbox("Exclude Ambiguous Characters")

    # Generate and print password
    if st.sidebar.button("Generate Password"):
        password = generate_password(length, include_symbols, include_numbers, include_lowercase, include_uppercase, exclude_similar, exclude_ambiguous)
        
        # Calculate the number of lines needed to display the password
        num_lines = (len(password) // 50) + 1  # Assuming 50 characters per line
        
        # Set the height of the text area based on the number of lines
        height = min(600, max(100, num_lines * 20))  # Minimum height of 100 and maximum height of 600, with 20 pixels per line
        
        # Display the generated password
        st.text_area("Generated Password: ", value=password, height=height)

