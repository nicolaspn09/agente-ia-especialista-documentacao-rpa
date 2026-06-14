import os
import re
import sys
import json
from typing import Optional, Any, List

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor, tool
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema import Document
from dotenv import load_dotenv

# Adiciona o caminho para a classe ConectaPGVector
sys.path.append(r"C:\rpa\Python") 
from Classes.Postgres.Postgres.ConectaPGVector import ConectaPGVector

# Carregar variáveis de ambiente
load_dotenv(r"C:\Users\Nícolas Nasário\OneDrive\Cursos online\Treinamento Python - Hashtag\Códigos\Chatbot Documentacao RPA\.env")
groq_api_key = os.getenv("GROQ_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")



def consulta_documentacoes_banco():
    pass # Logica de negocio removida por seguranca corporativa



def listagem_documentos() -> List[str]:
    pass # Logica de negocio removida por seguranca corporativa
