import streamlit as st #pip install streamlit
import sqlite3  # o tu base de datos

#executo aquest fent: python -m streamlit run boton6.py 

# CSS personalizado para botones más grandes y azules
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #1a6fb5;
        color: white;
        height: 80px;
        width: 100px;
        font-size: 18px;
        border-radius: 10px;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #0d4f8c;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

def crear_bd():
    conn = sqlite3.connect("datos.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articulos (
            codigo TEXT PRIMARY KEY,
            descripcion TEXT,
                   foto TEXT
        )
    """)
    articulos = [
        ("A1", "Descripción artículo A1","copa.png"),
        ("A2", "Descripción artículo A2","copa2.png"),
        ("A3", "Descripción larga A3","copa3.png"),
        ("A4", "Descripción artículo A4","copa4.png"),
        ("B1", "Descripción artículo B1",""),
        ("B2", "Descripción artículo B2",""),
        ("B3", "Descripción artículo B3",""),
        ("B4", "Descripción artículo B4",""),
        ("C1", "Descripción artículo C1",""),
        ("C2", "Descripción artículo C2",""),
        ("C3", "Descripción artículo C3","copa2.png"),
        ("C4", "Descripción artículo C4",""),

    ]
    cursor.executemany("INSERT OR IGNORE INTO articulos VALUES (?, ?, ?)", articulos)
    conn.commit()
    conn.close()

# Cargar datos
conn = sqlite3.connect("datos.db")#tu_base.db
cursor = conn.execute("SELECT codigo FROM articulos")#("SELECT nombre FROM tabla")
filas = cursor.fetchall()

items = [row[0] for row in conn.execute("SELECT codigo FROM articulos").fetchall()]


# Tus datos (aquí de ejemplo, reemplaza con tu base de datos)
#items = ["Item 1", "Item 2", "Item 3", "Item 4",
#         "Item 5", "Item 6", "Item 7", "Item 8",
#         "Item 9", "Item 10", "Item 11", "Item 12"]

#print(items)
#print(filas)

# Mostrar botones
#for fila in filas:
#    if st.button(fila[0]):
#        st.write(f"Pulsaste: {fila[0]}")


# Crear botones en 3 filas x 4 columnas
for fila in range(3):#range(3):
    columnas = st.columns(4)
    for col in range(4):
        indice = fila * 4 + col
        if indice < len(items):#items
            with columnas[col]:
                if st.button(items[indice], key=f"btn_{indice}"):
                    seleccion = items[indice]
                    st.session_state["seleccion"] = seleccion


# Mensaje centrado AL FINAL, fuera del grid de botones
#st.markdown("---")
if "seleccion" in st.session_state:
    st.markdown(
        f"<h3 style='text-align: center; color: #1a6fb5;'>✅ Pulsaste: {st.session_state['seleccion']}</h3>",
        unsafe_allow_html=True
    )