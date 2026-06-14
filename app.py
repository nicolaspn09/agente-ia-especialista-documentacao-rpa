# app.py
import streamlit as st
from dotenv import load_dotenv
import os
import sys

# Carregar variáveis de ambiente
load_dotenv()

# Importar o novo módulo do agente
# Certifique-se de que o caminho está correto
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from chatbotDocumentacao import initialize_agent_components, process_query_with_agent


# --- INTERFACE STREAMLIT ---
st.set_page_config(
    page_title="RPA Chatbot",
    page_icon="✅",
)
st.header("Direcionador de documentações")


# Modelos disponíveis na Groq
# model_options = [
#     # "deepseek-r1-distill-llama-70b",
#     "meta-llama/llama-4-maverick-17b-128e-instruct",
#     # "moonshotai/kimi-k2-instruct",
#     # "qwen/qwen3-32b",
# ]


# Modelos disponíveis na Groq
model_options = [
    "gpt-4o-mini",
    "meta-llama/llama-4-maverick-17b-128e-instruct",
]


# Inicializar os componentes do agente apenas uma vez
if 'agent_initialized' not in st.session_state:
    st.session_state.agent_initialized = False
    st.session_state.selected_model = model_options[0] # Define um modelo padrão


with st.sidebar:
    st.title("Configurações")
    st.session_state.selected_model = st.selectbox(
        "Selecione o modelo LLM", 
        options=model_options,
        index=model_options.index(st.session_state.selected_model) if st.session_state.selected_model in model_options else 0
    )
    
    if st.button("Recarregar o Agente"):
        st.session_state.agent_initialized = False
        st.experimental_rerun()


if not st.session_state.agent_initialized:
    with st.spinner(f"Carregando o modelo {st.session_state.selected_model} e o Agente..."):
        try:
            initialize_agent_components(st.session_state.selected_model)
            st.session_state.agent_initialized = True
            st.success("Agente carregado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao carregar o agente: {e}")
            st.stop()


# Histórico de mensagens
if "messages" not in st.session_state:
    st.session_state["messages"] = []


# Exibir histórico
for message in st.session_state.messages:
    st.chat_message(message.get("role")).write(message.get("content"))


# Campo de chat
question = st.chat_input("Como posso ajudar?")

if question:
    # Nova pergunta do usuário
    st.chat_message("user").write(question)
    st.session_state.messages.append({"role": "user", "content": question})

    with st.spinner("Processando resposta..."):
        response = process_query_with_agent(question)
        
        # Mostrar resposta
        st.chat_message("ai").write(response)
        st.session_state.messages.append({"role": "ai", "content": response})