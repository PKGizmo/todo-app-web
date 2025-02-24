import streamlit as st
import functions

todos = functions.read_file("todos.txt")


def add_todo():
    new_todo = st.session_state["todo_input"] + '\n'
    todos.append(new_todo)
    functions.write_file(todos)
    st.session_state["todo_input"] = ''
    st.rerun()


st.title("My To-Do App", anchor=False)
st.subheader("This is my to-do app.", anchor=False)
st.write("This app is to increase your productivity!")


for index, todo in enumerate(todos):
    key_name = f"todo_list_el_{index}"
    checkbox = st.checkbox(todo, key=key_name)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[key_name]
        st.session_state["todo_input"] = ''
        st.rerun()

st.text_input(label="Enter a new to-do:",
              placeholder="Add a new to-do...",
              on_change=add_todo,
              key="todo_input")
