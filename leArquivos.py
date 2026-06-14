import os
import sys
from docx import Document as DocxDocument
from langchain.schema import Document

sys.path.append(r"C:\rpa\Python")
from Classes.Postgres.Postgres.ConectaPGVector import ConectaPGVector  # supondo que você salvou a classe em conecta_pgvector.py


def ler_docx(caminho_arquivo):
    pass # Logica de negocio removida por seguranca corporativa



def coletar_documentos(base_path):
    pass # Logica de negocio removida por seguranca corporativa



if __name__ == "__main__":
    # Conecta no PGVector
    connector = ConectaPGVector()

    # Caminho base
    base_path = r"G:\.shortcut-targets-by-id\1BP7ZF_9pVQKQQb6uq3IUlFsAmpYpZeo1\Manual RPA´s"

    # Coleta os documentos do diretório
    docs = coletar_documentos(base_path)
    print(f"Total de documentos coletados: {len(docs)}")

    # Envia para o banco
    if docs:
        connector.add_documents_to_collection(
            documents=docs,
            collection_name="manual_rpa",  # nome da tabela/coleção no PGVector
            pre_delete_collection=True      # cuidado: apaga a coleção antes de inserir
        )
