        background-color: #ff4b4b !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Gestione stati
# --- STEP 1: L'ACCESSO (Rischio) ---
if 'step' not in st.session_state:
    st.session_state.step = 1

if st.session_state.step == 1:
    st.markdown("<h1 class='main-title'>🔒 Area ad Alto Rischio 🔒</h1>", unsafe_allow_html=True)
    st.write("### Attenzione Fabio! ⚠️")
    st.write("Il contenuto che stai per vedere potrebbe causare infarto, convulsioni, annebbiamento dei sensi. Sei pronto?")
    
    if st.button('Entra a tuo rischio e pericolo... 🔥'):
        st.session_state.step = 1.5 # Nuovo mini-step!
        st.rerun()

# --- STEP 1.5: IL "DISCLAIMER" (La doccia fredda) ---
elif st.session_state.step == 1.5:
    st.markdown("<h1 class='main-title'>😇 Aspetta un attimo...</h1>", unsafe_allow_html=True)
    st.write("### Ebbene sì...")
    st.info("Nessuna mia foto nuda qui dentro. Mi spiace deluderti, so già a cosa stavi pensando! 😂")
    st.write("Però c'è qualcosa di dolce e carino che ti aspetta... 🍬")
    
    if st.button('Ok, superiamo la delusione e proseguiamo... 🙄'):
        st.session_state.step = 2
        st.rerun()

# --- STEP 2: LA DOMANDA CON IL TRUCCO ---
elif st.session_state.step == 2:
    st.markdown("<h1 class='main-title'>🌹 La Proposta Indecente 🌹</h1>", unsafe_allow_html=True)
    st.subheader("Fabio, vuoi essere il mio Valentino? (E magari anche il mio dessert?) 🍒")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button('SÌ, non vedo l\'ora! 😍'):
            st.session_state.step = 3
            st.rerun()
            
    with col2:
        # Un classico: il pulsante che scherza
        no_clicked = st.button('No... 🤔')
        if no_clicked:
            messaggi_no = [
                "Errore: Il tasto 'No' è stato disattivato per eccesso di sex appeal della richiedente 👄",
                "Errore di sistema: Fabio non può dire di no.❌ ",
                "Riprova... ma con più amore. 😂",
                "Input non valido. Il server accetta solo: 'Sì' o 'Sì, ti prego!' 🙏",
                "Ops! Se premi 'No' perdi il diritto al massaggio speciale. Vuoi davvero rischiare? 💣",
                "Il tasto 'No' è rotto. È un segno del destino, arrenditi! 😂",
                "Errore 69: Fabio non ha l'autorizzazione per rifiutare questo invito 🚫"
            ]
            st.error(random.choice(messaggi_no))

# --- STEP 3: IL PREMIO ---
elif st.session_state.step == 3:
    st.balloons()
    st.snow() # Un po' di atmosfera
    st.markdown("<h1 class='main-title'>🎉 OTTIMA SCELTA! 🎉</h1>", unsafe_allow_html=True)
    st.write("### Hai sbloccato il pacchetto 'Vale San Valentino VIP' 🥂")
    
    # Immagine audace/divertente
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJueGZ3bmZqZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCBmcm9tX2dpZl9zZWFyY2gmY3Q9Zw/l41lH4ADRtAYnGsLe/giphy.gif")
    
    st.markdown("---")
    st.write("### 🎁 Scegli il tuo premio:")
    
    premio = st.radio("", 
        ["Maratona di San Valentino: Una notte intera di me che ti faccio rimpiangere di non volermi come morosa 🔞",
