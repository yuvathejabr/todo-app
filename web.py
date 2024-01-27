import streamlit as st
import functions

todos = functions.get_todos()


def add_todos():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.write_todos(todos)


st.title("My todo app")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="add new todo...",
              key="new_todo", on_change=add_todos)


