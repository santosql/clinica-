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