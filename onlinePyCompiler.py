import streamlit as st
import sys
import io

def run_compiler(code):
    # redirect the output of the code to a buffer
    code_out = io.StringIO()
    sys.stdout = code_out

    # run the code
    exec(code)

    # get the output from the buffer
    output = code_out.getvalue()

    # reset the buffer and the standard output
    code_out.close()
    sys.stdout = sys.__stdout__

    return output

def compiler_app():
    # add a title to the app
    st.title('Online Python Compiler')

    # add a text area for entering Python code
    if 'code' not in st.session_state:
        st.session_state.code = ''
    code = st.text_area('Enter your Python code:', height=300, key='code', value=st.session_state.code)

    # add a button to run the code
    if st.button('Run'):
        # run the code and display the output
        output = run_compiler(code)

        # add a text input field for the output
        output_text = st.text_input('Output:', value=output)

    # display the Python code
    st.write('Python code:')
    st.code(code)



# if __name__ == '__main__':
#     app()
