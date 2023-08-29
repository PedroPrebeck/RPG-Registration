import streamlit as st
from database import create_user, login_user, create_character, get_characters

def main():
    st.subheader("Home")
    username = st.text_input("User Name")
    password = st.text_input("Password", type='password')
    login_button = st.button("Login")
    register_button = st.button("Register")

    if login_button:
        user = login_user(username, password)
        if user is not None:
            st.success("Logged In Successfully")
            st.button("Logout")
            if st.button("Create Character"):
                st.subheader("Create Your Character")
                new_strength = st.slider("Strength", 1, 10)
                new_intelligence = st.slider("Intelligence", 1, 10)
                new_skin_color = st.selectbox("Skin Color", ["White", "Black", "Brown", "Yellow"])
                new_hair = st.selectbox("Hair", ["Blonde", "Black", "Brown", "Red"])
                if st.button("Create"):
                    if create_character(username, new_strength, new_intelligence, new_skin_color, new_hair):
                        st.success("Character Created Successfully")
                    else:
                        st.warning("You have already created a character")
            if st.button("View Character"):
                st.subheader("Your Character")
                character = get_characters(username)
                if character is not None:
                    st.write(f"Strength: {character[0][1]}")
                    st.write(f"Intelligence: {character[0][2]}")
                    st.write(f"Skin Color: {character[0][3]}")
                    st.write(f"Hair: {character[0][4]}")
                else:
                    st.warning("You have not created a character yet")
        else:
            st.warning("Incorrect Username/Password. If you're not registered, please register.")
    elif register_button:
        if create_user(username, password):
            st.success("User Created Successfully. Please login.")
        else:
            st.warning("User Already Exists. Please login.")

if __name__ == '__main__':
    main()
