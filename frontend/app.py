import os
import sys
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.engine import estimate_cost

st.title("💸 TrueCost AI")
st.write("Scopri quanto costa davvero un prodotto")

product = st.text_input("Nome prodotto")
price = st.number_input("Prezzo (€)", min_value=1.0)

category = st.selectbox(
    "Categoria",
    ["sneakers", "electronics", "cosmetics", "furniture", "apparel"]
)

brand = st.selectbox("Brand level", ["low", "medium", "premium"])
channel = st.selectbox("Canale vendita", ["direct", "retail"])

if st.button("Calcola"):
    data = estimate_cost(product, price, category, brand, channel)

    st.subheader("📊 Analisi costo")
    st.metric("💰 Costo reale stimato", f"{data['real_cost']} €")

    st.write("### Dettagli")
    st.write(f"Prezzo finale: {data['price_final']} €")
    st.write(f"Prezzo netto: {data['price_net']} €")

    st.write("### 💸 Quota non produttiva")
    st.progress(data["non_productive_share"])
    st.write(
        f"{data['non_productive_share'] * 100:.1f}% del prezzo è marketing, brand e distribuzione"
    )
