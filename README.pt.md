## INTRODUÇÃO ##
Este documento possui uma breve descrição do design, suposições, detalhes de implementação e arquitetura, bem como as instruções detalhadas para a execução do programa.

A linguagem de programação escolhida foi Python e a versão de teste foi a *2.7.10*.

## SUPOSIÇÕES ##
As suposições que serão explicadas a seguir guiaram a implementação do algoritmo.

 - A entrada deve ser passada via *standard input* e estar formatada corretamente (como especificado no exemplo da especificação).
	 - O formato aceito é baseado na *regex* `[a-zA-Z]{2}\d+((,){1}( )*[a-zA-Z]{2}\d+)*` . Cada vértice é representado por **uma** letra do alfabeto e a distância é um número inteiro. Exemplo: AB7 significa uma aresta com origem no vértice A e destino no vértice B com peso igual a 7.
 -  A saída do algoritmo é baseada nos testes passados na especificação. Portanto, se a entrada for exatamente igual à da especificação, o resultado será o mesmo.
	 - O arquivo  `src/main/main.py` contém os resultados dos testes. Se quiser executar testes para outros conjuntos de arestas, é necessário alterá-lo.
	 - Cada tipo de problema do teste está diretamente ligado à uma função correspondente que o resolve.
	 - Como há uma correspondência entre os tipos de testes e as funções implementadas, poderia ter sido feita um interface via linha de comando onde o usuário escolhe qual tipo de problema (baseado nos testes) gostaria de resolver. Porém, por questão de simplicidade da solução, essa funcionalidade não foi implementada.
	 - Foram implementados alguns tratamentos básicos de erro.
	 - O sistema considera que as entradas foram dadas em um formato válido.
 - Considera-se que o valor de uma aresta é sempre um inteiro positivo maior que zero.


## ARQUITETURA ##
O sistema possui os seguintes módulos e sub-módulos agrupados:

 - *src*: Responsável pelo código da aplicação.
	 - *main*: Contém o código relacionado ao grafo e a interação com o usuário.
	 - *util*: Contém classes utilitárias utilizadas no sistema.
 - *tests*: Contém o código responsável pelos testes da aplicação.

## DESIGN ##
Seguindo a estrutura da seção de Arquitetura, o sistema tem as seguintes classes:

 - *src*
	 - *main*
		 - *Edge*: classe que representa uma aresta do grafo.
		 - *Graph*: classe que representa o grafo. Possui uma lista de vértices e cada vértice possui uma lista de vértices adjacentes.
	 - *util*
		 - *InputUtil*: classe responsável por ler a linha da entrada padrão e retornar um string com os dados lidos.
		 - *ParserUtil*: classe responsável por fazer o *parsing* de uma string e retorna uma lista de arestas (*edges*).
		 - *PrintUtil*: classe responsável por imprimir os dados formatados na saída padrão.
 - *tests*
	 - *EdgeTest*: classe responsável por fazer os testes relacionados à classe *Edge*.
	 - *GraphTest*: classe responsável por fazer os testes relacionados à classe *Graph*.
	 - *ParserUtilTest*: classe responsável por fazer os testes relacionados à classe *ParserUtil*.
	 - *PrintUtilTest*: classe responsável por fazer os testes relacionados à classe *PrintUtil*.

## DETALHES DE IMPLEMENTAÇÃO ##
Os principais detalhes de implementação são explicados a seguir:

 - A lista de vértices utilizada no grafo é implementada utilizando a estrutura de tipo de alta-performance do Python, *defaultdict(list)*. Tal estrutura facilita a implementação e permite acesso direto aos vértices e suas arestas.
 - As implementações para encontrar a distância direta entre vértices e encontrar todos os caminhos entre os vértices foi implementada recursivamente.
 - A implementação para achar a distância mais curta entre dois vértices foi baseada no algoritmo de Dijkstra. Nota: esse algoritmo somente funciona para arestas positivas.

## COMO EXECUTAR O CÓDIGO ##
Para executar o código principal basta, a partir do diretório inicial (*root*), executar o seguinte comando:

    python -m src.main.main

Para executar os testes basta, a partir do diretório inicial (*root*), executar o seguinte comando:

    python -m unittest discover -s tests -p "*_test.py"

## TESTES ##
Os testes unitários desenvolvidos foram idealizados para garantir a corretude da solução, além de auxiliar o desenvolvimento (e.g: ao fazer uma refatoração, garantir que o código ainda está correto).

Além dos testes realizados no grafo da especificação, foi criado um novo grafo (com casos especiais que não ocorriam no grafo inicial) para testar o algoritmo e garantir a corretude da solução.