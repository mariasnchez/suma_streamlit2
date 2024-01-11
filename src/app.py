import streamlit as st

st.title('Suma tres números')

st.write('## Usando `st.number_input`')

n1 = st.number_input('Primer sumando:', step=1)
n2 = st.number_input('Segundo sumando:', step=1)
n3 = st.number_input('Tercer sumando:', step=1)

st.write("La suma de los tres números es", n1 + n2 + n3)


st.write('## Usando `st.slider`')

p1 = st.slider('Primer sumando:', step=1)
p2 = st.slider('Segundo sumando:', step=1)
p3 = st.slider('Tercer sumando:', step=1)

st.write("La suma de los tres números es", p1 + p2 + p3)

