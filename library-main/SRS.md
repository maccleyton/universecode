Excelente, Cleyton! ✅ Com essas decisões fechadas, aqui está a **versão final do SRS em Markdown**, pronta para você usar no Cosmos Editor ou versionar no GitHub:

***

# **Nexus Calc Suite – Documento de Requisitos (SRS)**

## **1. Introdução**

O *Nexus Calc Suite* é uma aplicação modular que integra quatro calculadoras: **Financeira**, **Supercientífica**, **Lógica** e **Gráfica**. Este documento define os requisitos funcionais, não funcionais, critérios de aceitação e roadmap para implementação.

***

## **2. Escopo**

*   **Financeira**: comportamento igual a calculadoras financeiras clássicas (emuladores existentes).
*   **Supercientífica**: operações básicas, avançadas, frações, números complexos, conjuntos, coordenadas e funções.
*   **Lógica**: conversão entre bases numéricas.
*   **Gráfica**: visualização de funções (MVP futuro).

***

## **3. Requisitos Funcionais**

### **3.1 Financeira**

*   Teclas: `PV`, `FV`, `n`, `i%`, `PMT`, `C`, `⌫`, `+`, `-`, `×`, `÷`, `=`.
*   Toggle: PMT **início/fim**.
*   Comportamento clássico (sem solver numérico).
*   Mensagens claras para entradas inválidas.

**Critérios de aceitação:**

*   `PV=1000`, `i=1%`, `n=12`, `PMT=0` → `FV≈1126,83`.

***

### **3.2 Supercientífica**

#### **Teclado**

*   Agrupadores: `(` `)` `[` `]` `{` `}`.
*   Operadores: `+ - × ÷ ^`.
*   Funções: `sin`, `cos`, `tan`, `log`, `ln`, `exp`, `sqrt`, `cbrt`, `root(n,x)`.
*   Constantes: `π`, `e`.
*   Toggle: **DEG/RAD** (global).

#### **Operações**

*   **Básicas**: soma, subtração, multiplicação, divisão.
*   **Avançadas**: potência, radiciação, logaritmos.
*   **Complexas**:
    *   Álgebra de expoentes (multiplicação/divisão, radiciação aninhada).
    *   Frações: `p/q`, simplificação, conversão sob demanda.
    *   Números complexos: `a+bi`, operações básicas, potência, radiciação principal.
*   **Conjuntos**: `{…}`, `∪`, `∩`, `\`, `⊆`, `∈`, `A^c` (universo definido manualmente).
*   **Coordenadas**: `(a,b)*(c,d)` → produto **componente a componente**.
*   **Funções**:
    *   1º grau: `f(x)=ax+b` → avaliação, zero.
    *   2º grau: `f(x)=ax²+bx+c` → vértice, raízes, Δ.

**Critérios de aceitação:**

*   `sqrt(4)` → `2`.
*   `root(3,18)` → `≈2,6207`.
*   `(1/3)+(1/6)` → `1/2`.
*   `(2+3i)*(1-i)` → `5 - i`.
*   `{1,2} ∪ {2,3}` → `{1,2,3}`.
*   `f(x)=x²-3x+2` → raízes `1` e `2`.

***

### **3.3 Lógica**

*   Entrada: inteiro (truncar decimal).
*   Saídas: DEC, HEX, OCT, BIN.
*   Futuro: bit-depth, complemento de dois.

***

### **3.4 Gráfica (MVP)**

*   Entrada: `f(x)`, intervalo `[xmin,xmax]`, passo.
*   Render: canvas, eixos, grade, zoom/pan.
*   Mensagens para domínio inválido.

***

## **4. UX & Interface**

*   Navegação por **tabs**.
*   Teclado completo para Científica.
*   Mensagens claras e PT-BR (com termos técnicos em inglês entre parênteses).
*   Tema: azul + destaques dourados.
*   Fita de auditoria com exportação TXT/CSV.

***

## **5. Requisitos Não Funcionais**

*   **Performance**: resposta <50ms para expressões típicas.
*   **Segurança**: sem `eval`, sanitização de entrada.
*   **Acessibilidade**: ARIA, contraste AA, navegação por teclado.

***

## **6. Roadmap**

1.  Supercientífica – teclado, parser, funções básicas.
2.  Frações e simplificação.
3.  Complexos (forma algébrica).
4.  Conjuntos finitos.
5.  Coordenadas e funções.
6.  Financeira – teclas clássicas.
7.  Gráfica – MVP.

***

## **7. Decisões Confirmadas**

*   Produto entre pontos: **componente a componente**.
*   Escopo da Supercientífica: **ampliado além dos exemplos citados**.
*   Conversão de frações: **sob demanda**.
*   Universo dos conjuntos: **definido manualmente**.
*   Financeira: **emulador igual aos existentes atualmente**.
*   DEG/RAD: **toggle global**.
*   Idioma: **PT-BR com termos técnicos em inglês entre parênteses**.

***

## **8. Glossário**

*   **root(n,x)**: raiz n-ésima (*nth root*).
*   **PMT**: pagamento periódico (*payment*).
*   **Δ**: discriminante (*discriminant*).

***
