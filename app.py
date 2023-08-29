import streamlit as st
from database import create_user, login_user, create_character, get_characters


def main():
    st.subheader("Entrar na conta")
    username = st.sidebar.text_input("Nome de Usuário")
    password = st.sidebar.text_input("Senha", type="password")
    if st.sidebar.checkbox("Entrar?"):
        user = login_user(username, password)
        if user is not None:
            st.success("Entrada com Sucesso!")
            user_menu = ["Criar Personagem", "Ver Personagem"]
            user_choice = st.sidebar.selectbox("Menu", user_menu)
            if user_choice == "Criar Personagem":
                st.subheader("Criar Personagem")
                new_strength = st.slider("Força", 1, 10)
                new_intelligence = st.slider("Inteligência", 1, 10)
                new_skin_color = st.selectbox(
                    "Cor da Pele", ["Branca", "Preta", "Parda", "Amarela"]
                )
                new_hair = st.selectbox(
                    "Cor do Cabelo", ["Loiro", "Preto", "Marrom", "Vermelho"]
                )
                if st.button("Criar"):
                    if create_character(
                        username,
                        new_strength,
                        new_intelligence,
                        new_skin_color,
                        new_hair,
                    ):
                        st.success("Personagem criado com sucesso!")
                    else:
                        st.warning("Você já tem um personagem criado!")
            elif user_choice == "Ver Personagem":
                st.subheader("Seu Personagem")
                character = get_characters(username)
                if character:
                    st.write(f"Força: {character[0][1]}")
                    st.write(f"Inteligência: {character[0][2]}")
                    st.write(f"Cor da Pele: {character[0][3]}")
                    st.write(f"Cor do Cabelo: {character[0][4]}")
                else:
                    st.warning("Você ainda não criou um personagem!")
        else:
            st.warning("Usurário ou senha incorretos. Tente registrar um novo usuário.")
    if st.sidebar.button("Registrar"):
        if create_user(username, password):
            st.success("Usuário criado com sucesso!")
        else:
            st.warning("Usuário já existe!")


if __name__ == "__main__":
    main()
