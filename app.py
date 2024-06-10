import streamlit as st
from langchain.llms import OpenAI

# Setting the title of the Streamlit application
st.title('Simple LLM-App 🤖')

# Creating a sidebar input widget for the OpenAI API key, input type is password for security
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Defining a function to generate a response using the OpenAI model
def generate_response(input_text):
    # Initializing the OpenAI model with a specified temperature and API key
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    # Displaying the generated response as an informational message in the Streamlit app
    st.info(llm(input_text))
    
#Low Temperature (0.0 - 0.5): This makes the model more deterministic and focused.
#Medium Temperature (0.5 - 1.0): Provides a balance between randomness and determinism.
#High Temperature (1.0 and above): Increases the randomness of the output.
# Higher values make the model more creative and diverse in its responses, 
#but this can also lead to less coherence and more nonsensical or off-topic outputs.

# Creating a form in the Streamlit app for user input
with st.form('my_form'):
    # Adding a text area for user input
    text = st.text_area('Enter text:', '')
    # Adding a submit button for the form
    submitted = st.form_submit_button('Submit')
    # Displaying a warning if the entered API key does not start with 'sk-'
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    # If the form is submitted and the API key is valid, generate a response
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)