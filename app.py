import streamlit as st
import random

# Configurazione pagina
st.set_page_config(page_title="Area Riservata Fabio ❤️", page_icon="🌶️")

# CSS semplificato e leggibile (Testo scuro su sfondo chiaro)
st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
    }
    h1, h2, h3, p {
        color: #1a1a1a !important;
    }
    .stButton>button {
        border-radius: 20px;
        background-color: #ff4b4b;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Gestione stati
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- STEP 1 ---
if st.session_state.step == 1:
    st.title("🔒 Area ad Alto Rischio 🔒")
    st.write("### Attenzione Fabio! ⚠️")
    st.write("Il contenuto potrebbe causare annebbiamento dei sensi. Sei pronto?")
    
    if st.button('Entra a tuo rischio e pericolo... 🔥'):
        st.session_state.step = 1.5
        st.rerun()

# --- STEP 1.5 ---
elif st.session_state.step == 1.5:
    st.title("😇 Aspetta un attimo...")
    st.info("Nessuna mia foto nuda qui dentro. Mi spiace deluderti! 😂")
    st.write("Però c'è qualcosa di dolce che ti aspetta... 🍬")
    
    if st.button('Ok, proseguiamo... 🙄'):
        st.session_state.step = 2
        st.rerun()

# --- STEP 2 ---
elif st.session_state.step == 2:
    st.title("🌹 La Proposta Indecente 🌹")
    st.write("### Fabio, vuoi essere il mio Valentino? 🍒")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button('SÌ, assolutamente! 😍'):
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button('No... 🤔'):
            messaggi_no = [
                "Errore: Fabio non può dire di no.❌",
                "Input non valido. Il server accetta solo: 'Sì'! 🙏",
                "Il tasto 'No' è rotto. È un segno del destino! 😂",
                "Errore 69: Autorizzazione negata 🚫"
            ]
            st.error(random.choice(messaggi_no))

# --- STEP 3 ---
elif st.session_state.step == 3:
    st.balloons()
    st.title("🎉 OTTIMA SCELTA! 🎉")
    st.write("### Hai sbloccato il pacchetto 'VIP' 🥂")
    
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJueGZ3bmZqZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCBmcm9tX2dpZl9zZWFyY2gmY3Q9Zw/l41lH4ADRtAYnGsLe/giphy.gif")
    
    st.write("---")
    st.write("### 🎁 Scegli il tuo premio:")
    
    premio = st.radio("", 
        ["Maratona 🔞",
         "Un'ora di coccole e relax 🧸",
         "Un massaggio 'full optional' 🧖‍♂️",
         "Tutte le precedenti"])
    
    if st.button('Conferma il premio 🎟️'):
        st.success(f"Prenotazione confermata: **{premio}**!")
        st.write("💌 *Spero tu abbia molta energia... ci vediamo dopo.* 😉")
