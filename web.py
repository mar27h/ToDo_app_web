from tabnanny import check

import streamlit as st
import functions #our backend

todos = functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"]+'\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] =""


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:#sprawdza czy ToDo jest znaznaczone
        print(f"start if  ")
        print(f"todos before pop - {todos}")
        todos.pop(index) #usuwamy z todos ToDo oznaczone
        print(f"todos after pop - {todos}")
        functions.write_todos(todos) #aktualizujemy plik todo.txt
        print(f"todos after write - {todos}")
        #del st.session_state[index]
        st.rerun() #odświeżenie apki webowej
st.text_input(label="Enter a todo", placeholder="Add new todo here",
              on_change=add_todo, key = 'new_todo')

st.session_state