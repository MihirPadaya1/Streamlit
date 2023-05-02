import streamlit as st


st.title("iDQ - Intelligent Document Query")

st.write("This app will help you to ask Query from a PDF file")


st.subheader("Upload your PDF file")
uploaded_files = st.file_uploader("Choose multiple files", accept_multiple_files=True)


st.subheader("Ask your question")

form = st.form(key="user_settings")
with form:
  st.write("Enter a question related to the topic of the PDF file.")
  # User input - Question
  user_input = st.text_input("Question", key = "user_input")

  # Submit button to start generating answer
  generate_button = form.form_submit_button("Submit Question")
  num_input = 1
  if generate_button:
    if user_input == "":
      st.error("Question cannot be blank")
    else:
      my_bar = st.progress(0.05)
      st.subheader("Answer:")
      for i in range(num_input):
          st.markdown("""---""")
          def generate_output():
            ai_output = generate_output(user_input)
            st.write(ai_output)
            my_bar.progress((i+1)/num_input)

st.write( '')
hide="""
<style>
#MainMenu {visibility: hidden }
footer {visibility: hidden }
</style>
"""
st.markdown(hide, unsafe_allow_html=True)
