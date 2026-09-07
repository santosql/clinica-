#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
clinica vida+ - app de console
recursos disponiveis:
    -cadastro de pacientes
    -estatisticas
    -busca
    -listagem
requisitos:
    -python 3.10 ou superior
"""

from typing import Dict, List, dict

paciente = Dict[str, str] # nome(str), telefone(str), idade(int como str internamente)

def _input_nao_vazio(rotulo: str) -> str:
    """
    Recebe um rótulo e solicita ao usuário uma entrada não vazia.
    Retorna a entrada do usuário como uma string.
    """
    while True:
        valor = input(rotulo).strip()
        if valor:
            return valor
        print("campo obrigatório. por favor, tente novamente.")

def _input_int(rotulo:str,minimo:int=None,maximo:int=None) -> int:
    """
    Recebe um rótulo e solicita ao usuário uma entrada inteira.
    Retorna a entrada do usuário como um inteiro.
    """
    while True:
        entrada = input(rotulo).strip()
        try:
            valor=int(entrada)
            if minimo is not None and valor<minimo:
                print(f"valor mínimo é{minimo}")
                continue
            if maximo is not None and valor>maximo:
                print(f"valor máximo é{maximo}")
                continue
            return valor
        except ValueError:
            print("informe um número inteiro válido.")

def cadastrar_paciente(pacientes: List[paciente]) -> None:
    """
    Cadastra um novo paciente na lista de pacientes.
    Solicita ao usuário o nome, telefone e idade do paciente.
    Adiciona o paciente à lista de pacientes.
    """
    print("\n=== Cadastro de Paciente ===")
    nome=_input_nao_vazio("nome completo: ")
    idade=_input_int("idade(em anos): ",minimo=0,maximo=100)
    telefone=_input_nao_vazio("telefone(ex: 2198765-4321): ")
    pacientes.append({"nome":nome,"idade":str(idade),"telefone":telefone})
    print(f"paciente{nome}cadastrado com sucesso!\n")

def ver_estatisticas(pacientes: List[paciente]) -> None:
    """
    Exibe estatísticas sobre os pacientes cadastrados.
    Mostra o total de pacientes, a idade média e a idade mínima e máxima.
    """
    print("\n=== Estatísticas ===")
    if not pacientes:
        print("nenhum paciente cadastrado.\n")
        return

    idades=[int(p["idade"]) for p in pacientes if p.get("idade")]
    if not idades:
        print("nenhum paciente com idade cadastrada.\n")
        return

    total=len(pacientes)
    media=sum(idades)/len(idades)
    mais_novo=min(idades)
    mais_velho=max(idades)

    print(f"total de pacientes: {total}")
    print(f"idade média: {media:.1f} anos")
    print(f"paciente mais novo: {mais_novo} anos")
    print(f"paciente mais velho: {mais_velho} anos\n")

def buscar_por_nome(pacientes:List[paciente],termo:str)->List[paciente]:
    """
    Busca pacientes pelo nome.
    Retorna uma lista de pacientes cujo nome contém o termo de busca (case insensitive).
    """
    termo=termo.strip().lower()
    return [p for p in pacientes if termo in p.get("nome","").lower()]

def acao_busca(pacientes:List[paciente])->None:
    """
    Solicita ao usuário um termo de busca e exibe os pacientes encontrados.
    """
    print("\n=== buscar por nome ===")
    termo=_input_nao_vazio("informe o nome ou parte do nome do paciente: ")
    resultados=buscar_por_nome(pacientes,termo)
    if not resultados:
        print("nenhum paciente encontrado com esse nome.\n")
        return
    for i,p in enumerate(resultados,1):
        print(f"{i}. {p['nome']} - {p['idade']} anos - {p['telefone']}")
    print()

def listar_pacientes(pacientes:List[paciente])->None:
    """
    Lista todos os pacientes cadastrados.
    """
    print("\n=== Listagem de Pacientes ===")
    if not pacientes:
        print("nenhum paciente cadastrado.\n")
        return
    for i,p in enumerate(pacientes,1):
        print(f"{i}. {p['nome']} - {p['idade']} anos - {p['telefone']}")
    print()

def menu():
    """
    Exibe o menu principal e solicita ao usuário uma opção.
    Retorna a opção escolhida pelo usuário.
    """
    pacientes: List[paciente] = []
    opcoes={
        "1": ("cadastrar paciente",lambda:cadastrar_paciente(pacientes)),
        "2": ("ver estatisticas",lambda:ver_estatisticas(pacientes)),
        "3": ("buscar por nome",lambda:acao_busca(pacientes)),
        "4": ("listar pacientes",lambda:listar_pacientes(pacientes)),
        "5": ("sair",None)
    }

    while True:
        print("=== Menu Principal ===")
        for k,(titulo,_)in opcoes.items():
            print(f"{k}. {titulo}")
        escolha=input("escolha uma opção: ").strip()

        if escolha=="5":
            print("encerrando...até logo!")
            break
        if escolha in opcoes:
            try:
                acao=opcoes[escolha][1]()
                if acao:
                    acao()
            except Exception as exc:
                print(f"ocorreu um erro: {exc}")
        else:
            print("opção inválida. tente novamente.\n")

if __name__=="__main__":
    menu()
    