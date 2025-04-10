import streamlit as st

st.session_state.tasks = []

st.title("Todo list")
def add_task():
    task = st.text_input("sisesta uus ülesanne" , key ="new_task_input")
    if st.button("lisa"):
        if task.strip():
            st.session_state.append("text":task,"done":False)
            st.rerun()
    else:
        st.warning("sisesta mitte tühi ülesanne")

add_task()
