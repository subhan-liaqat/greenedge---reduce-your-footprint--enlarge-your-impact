import streamlit as st
from assistant import get_prompt

st.title("GreenEdge Assistant")
st.write("Ask your questions about eco-friendly living and reducing your carbon footprint.")

user_question = st.text_input("Enter your question:")

if st.button("Ask GreenEdge"):
  if user_question:
    response = get_prompt(user_question)
    if response:
      st.write(f"GreenEdge Assistant: {response}")
    else:
      st.error("An error occurred while processing your request.")
  else:
    st.warning("Please enter a question.")