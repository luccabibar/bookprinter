# BOOKPRINTER V1.0

Ferramenta simples para reordenação de PDFs para impressão em formato de livro

---

### O que é

Este programa é uma ferramenta que reorganiza um pdf, para que se possa imprimí-lo não como folhas sequenciais, mas sim como um livro.

### Formato

O formato que este programa atende é o seguinte: arquivos PDF A4 convencionais, que devem ser impressos no modo `Duas Páginas por Folha`, a fim de que cada folha contenha `4 páginas` (`2` em cada face). Uma vez que todas as folhas estão impressas, é possível dobrá-las ao meio, e ao empilhar todas as folhas já dobradas, elas assumem a formatação de um livro.

### Não entendi nada

Achou complicado? Fazer o que, eu to tentando explicar um objeto físico complexo por meio de texto. E o texto ta confuso também. 

Pra entender do que se trata, é possível construir um pequeno modelo de papel. Pode ser um saco, mas construir este modelo vai te fazer entender como esse programa opera.

1. Pegue uma folha de papel A4, parta no meio, de maneira que agora você tem duas folhas de papel A5.
2. Pegue cada uma dessas folhas e dobre no meio.
3. Empilhe as folhas, de modo que as dobras se alinhem
4. Note a estrutura que o objeto assumiu, e a similaridade com um livro ou caderno de brochura.
5. Numere cada uma das páginas, começando da "capa" e terminando em seu verso
6. Agora, observe o padrão de os números das páginas tomam.

Se você seguiu essas etapas corretamente, você deve ter ficado com o seguinte:

Uma folha marcada com `8` e `1` em um lado, e `2` e `7` em outro
Uma outra folha, marcada com `6` e `3` em um lado, e `4` e `5` em outro

Note que é um padrão regular, mas calculá-lo não é exatamente intuitivo. Este programa faz isso, reordena um PDF para que possa ser impresso para atender este formato.

### Uso

Para user o programa, basta executá-lo com seu PDF como parâmetro. Note que é necessário instalar o pacote `pypdf`

instalar pacote:
`~$ pip install pypdf`

executar programa:
`~$ py bookprinter.py target.pdf`

### Exemplo
Dado um arquivo de `8` páginas:

O programa determina que ele usará Duas Folhas na impressão, e então gera um novo arquivo, baseado no pdf original, mas reordenado

O arquivo gerado terá a seguinte ordem:
`P8, P1, P6, P3, P2, P7, P4, P5`
Cada página que será impressa corresponde a dois números.

A `Primeira Folha` conterá  `P8` e `P1`, e no seu verso, `P2` e `P7`
A `Segunda Folha` conterá `P6` e `P3`, e em seu verso, `P4` e `P5`

Isso significa que, ao empilhar as folhas em ordem, e dobrá-las ao meio, elas assumirrão o formato de um livro, onde cada folha cobre a próxima. Ideal para grampear no meio.

### Impressão

A impressão segue o seguinte esquema: primeiro são impressos todas as folhas da frente, e depois são impressas todas do verso. Assim, só é necessário recarregar a impressora uma vez. Note que deve haver uma pausa enrte a etapa da parte da frente e a do verso.
