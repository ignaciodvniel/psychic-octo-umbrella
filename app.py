import streamlit as st
from streamlit.components.v1 import html

cards = [
    {"id": "card-2025-09-13", "title": "13-09-2025", "content": " "},
    {"id": "card-2025-09-14", "title": "14-09-2025", "content": "Texto de la carta del 14-09-2025. Aquí va el contenido que no debe ser seleccionable ni copiable."}
]

st.markdown("""
<style>
:root {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
html, body, .stApp {
  -webkit-user-select: none !important;
  -moz-user-select: none !important;
  -ms-user-select: none !important;
  user-select: none !important;
}
.nav {
  position: sticky;
  top: 0;
  background: rgba(255,255,255,0.95);
  padding: 10px;
  z-index: 1000;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  align-items: center;
  border-bottom: 1px solid rgba(0,0,0,0.06);
}
.nav a { text-decoration: none; }
.nav button {
  padding: 8px 12px;
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 6px;
  background: transparent;
  cursor: pointer;
  font-weight: 600;
}
.card {
  border-radius: 8px;
  padding: 20px;
  margin: 24px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  background: #ffffff;
}
.card h3 {
  margin: 0 0 8px 0;
  font-size: 18px;
}
.card-content {
  white-space: pre-wrap;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
</style>
""", unsafe_allow_html=True)

nav_html = '<div class="nav">'
for c in cards:
    nav_html += f'<a href="#{c["id"]}"><button>{c["title"]}</button></a>'
nav_html += '</div>'

st.markdown(nav_html, unsafe_allow_html=True)

for c in cards:
    st.markdown(
        f'''
        <div class="card" id="{c["id"]}" oncopy="return false" oncut="return false" onpaste="return false" oncontextmenu="return false" draggable="false" unselectable="on">
          <h3>{c["title"]}</h3>
          <div class="card-content">{c["content"]}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )