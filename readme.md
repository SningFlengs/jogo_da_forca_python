## Resumo do Funcionamento

Jogo da forca desenvolvido em python, o jogador tenta adivinhar uma palavra sorteada do banco de dados, letra por letra, ou a palavra completa. O jogador possui 7 chances para errar antes de perder o jogo. O jogo possui um sistema de ranking que guarda o nickname dos jogadores e seus pontos, além da possibilidade de adicionar novas palavras ao banco de dados do jogo.

## Características Gerais

1. **Menu Principal**: O jogo começa com um menu principal que permite ao jogador escolher entre:
   - Jogar
   - Ver Ranking
   - Ver Créditos
   - Cadastrar Nova Palavra
   - Sair

2. **Sistema de Palavras**:
   - Palavras pré-definidas são armazenadas em uma lista no início do código.
   - Existe a opção de adicionar novas palavras ao banco de dados de palavras (`palavras.txt`).

3. **Sistema de Ranking**:
   - O ranking dos jogadores é armazenado em um arquivo (`ranking.txt`).
   - Os jogadores têm suas pontuações salvas e atualizadas após cada partida se houver vitória..

4. **Funcionamento do jogo**:
   - O jogador deve adivinhar a palavra sorteada chutando letras.
   - O jogador pode tentar adivinhar a palavra inteira a qualquer momento.
   - Cada letra correta é revelada na palavra, enquanto letras incorretas diminuem o número de chances restantes.
   - O jogo termina quando o jogador adivinha a palavra ou esgota suas chances.

5. **Tratativa de erro**:
   - O jogo possui uma tratativa de erro. Caso os arquivos, `palavras.txt` ou `ranking.txt` forem excluídos a qualquer momento, o jogo continuará funcionando.

## Jogabilidade

1. **Início do Jogo**:
   - O jogador escolhe a opção "Jogar" no menu principal.
   - É solicitado o nickname do jogador.
   - Uma palavra é sorteada aleatoriamente da lista de palavras.

2. **Adivinhação**:
   - O jogador tem 7 chances para errar.
   - Para cada chute, é verificado se está correto ou não..
   - O jogador pode tentar adivinhar a palavra inteira.

3. **Termino do Jogo**:
   - Se o jogador acerta a palavra, sua pontuação é incrementada e salva no ranking.
   - Se o jogador perde todas as chances, a palavra sorteada é revelada.

## Bibliotecas Utilizadas

1. **`random`**:
   - Usada para sortear palavras aleatórias da lista de palavras.

2. **`pathlib`**:
   - Usada para manipulação de caminhos de arquivos e verificação de existência dos arquivos de palavras e ranking.

3. **`time`**:
   - Usada para criar pequenos atrasos, melhorando a aparência do jogo com animações simples de loading.

## Funções e Suas utilidades

1. **`styleprint(txt)`**:
   - Imprime texto formatado com bordas, usado para melhorar a visualização de títulos e mensagens importantes.

2. **`gerar_forca(palavra, chutes, chances)`**:
   - Gera a visualização da palavra da forca com letras acertadas e espaços em branco para letras não adivinhadas.

3. **`loading()`**:
   - Cria uma animação de carregamento com três pontos.

4. **`cadastrar_palavra()`**:
   - Permite ao jogador cadastrar novas palavras no banco de dados de palavras.

5. **`procurar_nickname(nickname_usuario, pontos_usuario)`**:
   - Verifica se o nickname do jogador já existe no ranking e atualiza sua pontuação ou adiciona um novo registro.

6. **`menu()`**:
   - Exibe o menu principal do jogo.

7. **`antierror_palavra()`**:
   - Verifica a existência do arquivo de palavras e cria-o se não existir, preenchendo-o com as palavras pré-definidas.

8. **`antierror_rank()`**:
   - Verifica a existência do arquivo de ranking e cria-o se não existir.
