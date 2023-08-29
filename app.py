import streamlit as st
from database import create_user, login_user, create_character, get_characters
import SessionState

def main():
    session_state = SessionState.get(user_name="", password="", login_status=False)
    st.subheader("Home")
    if session_state.login_status:
        user = session_state.user_name
    else:
        user = st.text_input("User Name")
        session_state.user_name = user
        password = st.text_input("Password", type='password')
        session_state.password = password
        login_button = st.button("Login")
        register_button = st.button("Register")

    if not session_state.login_status:
        if login_button:
            user = login_user(session_state.user_name, session_state.password)
            if user is not None:
                session_state.login_status = True
                st.success("Logged In Successfully")
            else:
                st.warning("Incorrect Username/Password. If you're not registered, please register.")
        elif register_button:
            if create_user(session_state.user_name, session_state.password):
                st.success("User Created Successfully. Please login.")
            else:
                st.warning("User Already Exists. Please login.")
    else:
        if st.button("Logout"):
            session_state.login_status = False
        if st.button("Create Character"):
            st.subheader("Create Your Character")
            new_strength = st.slider("Strength", 1, 10)
            new_intelligence = st.slider("Intelligence", 1, 10)
            new_skin_color = st.selectbox("Skin Color", ["White", "Black", "Brown", "Yellow"])
            new_hair = st.selectbox("Hair", ["Blonde", "Black", "Brown", "Red"])
            if st.button("Create"):
                if create_character(session_state.user_name, new_strength, new_intelligence, new_skin_color, new_hair):
                    st.success("Character Created Successfully")
                else:
                    st.warning("You have already created a character")
        if st.button("View Character"):
            st.subheader("Your Character")
            character = get_characters(session_state.user_name)
            if character is not None:
                st.write(f"Strength: {character[0][1]}")
                st.write(f"Intelligence: {character[0][2]}")
                st.write(f"Skin Color: {character[0][3]}")
                st.write(f"Hair: {character[0][4]}")
            else:
                st.warning("You have not created a character yet")

if __name__ == '__main__':
    main()
