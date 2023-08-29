import streamlit as st
from database import create_user, login_user, create_character, get_characters

def main():
    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.button("Login"):
            user = login_user(username, password)
            if user is not None:
                st.success("Logged In Successfully")
                st.sidebar.empty()
                if st.sidebar.button("Logout"):
                    username = ""
                    password = ""
                    st.sidebar.empty()
                if st.sidebar.button("Create Character"):
                    choice = "Create Character"
                if st.sidebar.button("View Character"):
                    choice = "View Character"
            else:
                st.warning("Incorrect Username/Password")
        if st.sidebar.button("Register"):
            user = create_user(username, password)
            if user:
                st.success("User Created Successfully")
            else:
                st.warning("User Already Exists")
    elif choice == "Login":
        st.subheader("Login Section")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login"):
            user = login_user(username, password)
            if user is not None:
                st.success("Logged In Successfully")
                user_menu = ["Home", "Create Character", "View Character"]
                user_choice = st.sidebar.selectbox("Menu", user_menu)
                if user_choice == "Create Character":
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
                elif user_choice == "View Character":
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
                st.warning("Incorrect Username/Password")
    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')

        if st.button("Signup"):
            if create_user(new_user, new_password):
                st.success("User Created Successfully")
            else:
                st.warning("User Already Exists")

if __name__ == '__main__':
    main()
