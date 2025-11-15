# Integração por Frações Parciais

Projeto de Cálculo II para decomposição e integração por frações parciais.

## Visão geral
Este repositório implementa soluções para quatro casos típicos de integrais racionais usando decomposição em frações parciais e integração analítica. Há uma interface de menu (`menu.py`) que permite executar cada caso individualmente.

Casos implementados:
- Caso 1: ∫ (A*x + B) / ((x - x1)*(x - x2)) dx — (raízes reais)
- Caso 2: ∫ (A*x + B) / (a*x² + b*x + c) dx
- Caso 3: ∫ (A*x + B) / ((x² + x1)*(x² + x2)) dx
- Caso 4: ∫ (A*x² + B*x + C) / ((x - a)*(x² + b)) dx

Estrutura principal:
- menu.py — menu interativo para executar os casos
- caso1/, caso2/, caso3/, caso4/ — scripts de cada caso (`integrar-1.py`, `integrar-2.py`, ...)
- caso1/integrar.py — implementação orientada a objetos (ex.: `IntegradorCaso3`)
- testes/ — arquivos de entrada/saída para validação manual
- img/ — imagens/diagramas (opcional)
- LICENSE — licença MIT

## Requisitos
- Python 3.8+ (testado em Windows)
- Biblioteca padrão (math, fractions)

## Execução (Windows)
1. Abra o terminal (cmd / PowerShell) e navegue até a pasta do projeto:
   cd "C:\Users\Rafael\Desktop\Trabalho-Pratico-Calculo-II"
2. Inicie o menu interativo:
   python menu.py
3. Ou execute um caso diretamente:
   python caso1\integrar-1.py
   python caso2\integrar-2.py
   python caso3\integrar-3.py
   python caso4\integrar-4.py

Observação: alguns módulos experimentais (ex.: `caso1/integrar.py`) podem expor classes e funções para uso em scripts ou testes automatizados.

## Uso rápido
- Para calcular uma integral pelo menu: execute `python menu.py` e escolha o caso.
- Para usar a versão programática do Caso 3 (classe `IntegradorCaso3`), importe o módulo `caso1.integrar` em um script Python e instancie com os coeficientes desejados.

Exemplo mínimo:
```py
from caso1.integrar import IntegradorCaso3

integ = IntegradorCaso3(2, 3, 1, 4)
print(integ.decompor_e_integrar(verbose=False))
```

## Testes
A pasta `testes/` contém entradas de teste para cada caso. Não há um runner de testes automatizado incluído — os testes atualmente são manuais / exemplos. É encorajado adicionar testes unitários (pytest/unittest) no futuro.

## Vídeo do projeto
https://youtu.be/lk4gmuvknKo

## Contribuição
- Faça um fork e abra um pull request com descrições claras das mudanças.
- Siga o padrão de docstrings e adicione testes para novas funcionalidades.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para detalhes.

## Autores
Equipe: Any Gabriela, Guilherme Pinheiro, Izabel Chaves, Matheus Rossi e Rafael Colares

