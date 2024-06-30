

import streamlit as st
def sum(a,b):
    return a+b
number_one = st.number_input("Insert a number", value=None, placeholder="Type a number...",key="number_one")

number_two = st.number_input("Insert a number", value=None, placeholder="Type a number...",key="number_two")
if st.button("ADD"):
    result=sum(number_one,number_two)
    st.title(result)