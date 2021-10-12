# Import Custom Module
import pathlib
import sys
sys.path.append(str(pathlib.Path().absolute()).split("/src")[0] + "/src")

import streamlit as st


def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


st.set_page_config(
    page_title="Meli App - Registro en Jira",
    layout="wide",
    page_icon="src/media/meli.png",
) 

load_css("src/style.css")






def main():

    query_params = st.experimental_get_query_params()
    query_option = query_params['code'][0]

    st.markdown(f"""
    # <span style="">Mercado Libre App</span>

   Herramienta creada por <span style="font-family:'monkvetica'; font-weight:1000">Media</span>.<span class="nothing">Monks</span> <i>Buenos Aires </i> para el proceso de migracion de tablas 

    """,  unsafe_allow_html=True
    ) # <i>Buenos Aires :flag-ar:</i> 

    st.subheader('Código de autorización de TEMPO')

    st.markdown(f"""
        Por favor, copiá el código y pegalo en la App para poder acceder a Jira con tu usuario
        """,  unsafe_allow_html=True
        ) 

    st.code(query_option, language='Python')


if __name__ == "__main__":
    main()