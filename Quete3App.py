import pandas as pd
import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

df = pd.read_csv("https://github.com/KhaPy39/quete3/blob/main/comptes.csv")

dict = {"usernames": {}}

for _, row in df.iterrows():
    dict["usernames"][row['username']] = {
        "name": row['name'],
        "password": row['password'],
        "email": row['email'],
        "failed_login_attempts": int(row['failed_login_attempts']),
        "logged_in": row['logged_in'] == 'True',
        "role": row['role']
    }


authenticator = Authenticate(
    dict,
    "cookie name",
    "cookie key",
    30,
)

authenticator.login()

def accueil():
    with st.sidebar:
        authenticator.logout("Déconnexion")
        st.write(f"Bienvenue {st.session_state['username']}")
        selection = option_menu(
                                menu_title=None,
                                options = ["🤩 Accueil", "😻 Les photos de mon chat"]
                                )
        
    if selection == "🤩 Accueil":
        st.title("Bienvenue sur ma page")
        st.image("https://c0.lestechnophiles.com/www.madmoizelle.com/wp-content/uploads/2015/08/gif-chat-mouille.gif?resize=150")
        
    elif selection == "😻 Les photos de mon chat":
        st.title("Bienvenue dans l'album photo de mon chat 😽")
        col1, col2, col3 = st.columns(3)
        with col1:
                st.image("https://p0.itc.cn/q_70/images03/20221101/6cb9b1e699214213b843226a8025d13f.gif")
        with col2:
                st.image("https://www.letribunaldunet.fr/wp-content/uploads/2022/05/chat-le-saviez-vous.jpg")
        with col3:
                st.image("https://th.bing.com/th/id/R.bf9e28d9df8dbe6c88bbb39d1c42fde0?rik=ezkzZnukwlPsqw&riu=http%3a%2f%2flepassetempsderose.l.e.pic.centerblog.net%2f347c6c7e.gif&ehk=CdFk%2fu65aQG2%2bebQlSQ7Ds8u64g3xaKqzMTBQxYZ%2fPo%3d&risl=1&pid=ImgRaw&r=0")


  

        

if st.session_state["authentication_status"]:
  accueil()

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')