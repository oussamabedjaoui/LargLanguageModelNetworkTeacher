import streamlit as st
import ollama

# --- CONFIGURATION ---
st.set_page_config(page_title="Professeur IA", page_icon="🎓")
st.title("🎓 Le Professeur de Réseaux")
st.caption("Posez-moi une question, je suis là pour vous aider !")

MODEL_NAME = "mon-prof"

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Affiche l'historique
for message in st.session_state["messages"]:
    role = message["role"]
    if role == "user" or role == "assistant":
        with st.chat_message(role):
            # On affiche le contenu nettoyé
            st.markdown(message["content"])

# --- CŒUR DU PROGRAMME ---
if prompt := st.chat_input("Votre question ici..."):
    
    # 1. Affiche la question utilisateur
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. PROMPT STRICT
    prompt_modifie = f"""
    [INSTRUCTIONS]
    Tu es un expert réseau pédagogue.
    
    1. Si la question est technique : Explique simplement.
    2. Si la question est hors sujet (Napoléon, Cuisine...) : Réponds JUSTE "Je ne sais pas, je suis un prof de réseaux."
    
    Ne mets JAMAIS de titre comme "Réponse :" au début.
    
    QUESTION : {prompt}
    """

    # Sauvegarde (on garde le prompt modifié en mémoire interne, mais on affiche le simple)
    st.session_state["messages"].append({
        "role": "user", 
        "content": prompt_modifie,
        "display_content": prompt 
    })

    # 3. Génération de la réponse
    with st.chat_message("assistant"):
        response_container = st.empty()
        full_response = ""
        
        try:
            stream = ollama.chat(
                model=MODEL_NAME,
                messages=st.session_state["messages"],
                stream=True,
                options={'temperature': 0.6}
            )
            
            for chunk in stream:
                content = chunk['message']['content']
                full_response += content
                
                # --- ZONE DE NETTOYAGE ---
                # On crée une version "propre" du texte pour l'affichage
                # On enlève toutes les variantes possibles du préfixe gênant
                clean_text = full_response
                clean_text = clean_text.replace("RÉPONSE DU PROF :", "")
                clean_text = clean_text.replace("RÉPONSE DU PROF", "")
                clean_text = clean_text.replace("REPONSE DU PROF :", "")
                clean_text = clean_text.replace("Instruction :", "")
                clean_text = clean_text.strip() # Enlève les espaces vides au début
                
                response_container.markdown(clean_text + "▌")
            
            # Affichage final sans le curseur
            response_container.markdown(clean_text)
            
            # C'est la version PROPRE qu'on sauvegarde dans l'historique
            st.session_state["messages"].append({"role": "assistant", "content": clean_text})
        
        except Exception as e:
            st.error(f"Erreur : {e}")