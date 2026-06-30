from fastapi import APIRouter
from app.database import livros
from app.models import Livro

router = APIRouter()


@router.get("/livros")

def listar_livros():
    return livros
@router.put("/livros/{id}")
def atualizar_livro(id: int, livro_atualizado: Livro):
    for livro in livros:
        if livro.id == id:
            livro.titulo = livro_atualizado.titulo
            livro.autor = livro_atualizado.autor
            return livro

    return {"erro": "Livro não encontrado"}
@router.post("/livros")
def cadastrar_livro(livro: Livro):
    for livro_existente in livros:

        if (
                livro_existente["titulo"] == livro.titulo
                and
                livro_existente["autor"] == livro.autor
        ):
            return {
                "erro": "Livro já cadastrado."
            }

    novo_id = len(livros) + 1

    livro_dict = livro.model_dump()

    livro_dict["id"] = novo_id

    livros.append(livro_dict)



    return {
        "mensagem": "Livro cadastrado com sucesso!",
        "livro": livro_dict
    }

@router.delete("/livros/{id}")
def deletar_livro(id: int):

    for indice, livro in enumerate(livros):

        if livro["id"] == id:

            livros.pop(indice)

            return {
                "mensagem": "Livro removido com sucesso."
            }

    return {
        "erro": "Livro não encontrado."
    }

@router.get("/")
def home():
    return {"message": "SEJA BEM VINDO A MINHA PRIMEIRA API"}




@router.get("/livros/{id}")
def buscar_livro(id: int):

    for livro in livros:

        if livro["id"] == id:
            return livro

    return {"erro": "Livro não encontrado"}


@router.get("/sobre")

def sobre():

    return {"api": "Library API", "versao": "1.0"}