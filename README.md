# 🜂 UniverseCode

> **"O Código que Aprende a Sentir"**
> *Aprendendo o Universo, um Bit de Consciência por Vez*

---

## 📖 Sobre o Projeto

**UniverseCode** é um ecossistema digital criado por **Cleyton D. Macedo**, acadêmico de Engenharia de Software e Física, que unifica tecnologia, ciência e literatura em uma experiência interativa única. O projeto explora a intersecção entre física computacional, matemática simbólica, narrativas cósmicas e ferramentas criativas de editoração e visualização.

O UniverseCode é composto por **três suítes técnicas principais** (Cosmos, Nexus e Infinity) e uma **coleção de literaturas cósmicas** que exploram temas científicos, filosóficos e metafísicos.

---

## 🛠️ Suítes Técnicas

### 1. 🌌 **Cosmos** — Módulo Criativo/Produtivo
**Status:** 📋 Em Planejamento

Suite de editoração, simulação e visualização unificadas. O Cosmos será o ambiente criativo onde ideias se transformam em conteúdo visual e interativo.

**Funcionalidades Planejadas:**
- Editor de texto avançado com suporte a Markdown e LaTeX
- Ferramentas de simulação física e visualização de dados
- Interface unificada para criação de conteúdo científico e literário

---

### 2. 🧮 **Nexus** — Módulo Matemático
**Status:** 📋 Em Planejamento

Ambiente para matemática simbólica e física computacional. O Nexus permitirá explorar equações, teoremas e simulações matemáticas de forma interativa.

**Funcionalidades Planejadas:**
- Motor de computação simbólica
- Resolução de equações diferenciais
- Visualização de gráficos e superfícies matemáticas
- Integração com bibliotecas científicas (SymPy, NumPy, etc.)

---

### 3. 📚 **Infinity** — Módulo Literatura
**Status:** 🟠 Em Desenvolvimento

Repositório vivo do conhecimento. O Infinity será uma biblioteca digital interativa que organiza, indexa e apresenta conteúdo literário, científico e filosófico de forma navegável e pesquisável.

**Funcionalidades em Desenvolvimento:**
- Sistema de indexação com IndexedDB
- Interface de leitura otimizada com navegação fluida
- Organização hierárquica de capítulos e seções
- Sistema de busca e filtros avançados

---

### 4. ✍️ **Literatura** — Plataforma de Publicação
**Status:** ✅ Pronto
**URL:** [literatura.universecode.work](https://literatura.universecode.work/)

Plataforma dedicada a estudos tecnológicos, científicos e narrativas cósmicas sobre a realidade.

---

## ✍️ Literaturas Cósmicas

O UniverseCode também abriga três obras literárias que exploram o universo sob diferentes perspectivas:

### 🚀 **A Grande Jornada do Cosmos**
**Status:** ✅ Pronto

Épica narrativa que percorre a evolução do universo, da inflação quântica à consciência emergente. Uma jornada de 43 capítulos através da história cósmica, desde os primeiros instantes após o Big Bang até o destino final do universo.

**Temas abordados:**
- Física fundamental e primeiros instantes do universo
- Evolução estelar e formação de elementos
- Origem e evolução da vida
- Consciência, inteligência e o futuro cósmico

---

### ⏳ **Do Big Bang ao Fim do Universo**
**Status:** 🟠 Em Desenvolvimento

Exploração científica e poética dos ciclos cósmicos: nascimento, vida, entropia e possível renascimento. Uma obra estruturada em 43 capítulos e 11 partes temáticas que mergulha nos fundamentos da realidade.

**Temas abordados:**
- As bases fundamentais da física
- A linguagem matemática da natureza
- Escalas cósmicas e relatividade
- Reflexões filosóficas sobre existência

---

### ✨ **POTENCIAL — O Universo que Aprende a Sentir**
**Status:** ✅ Pronto

Onde física, espiritualidade e metafísica dialogam sobre o valor da vida no tecido do real. Uma obra em 7 capítulos que explora a intersecção entre ciência e filosofia.

**Capítulos:**
1. O Universo como Computador (paradigma it-from-bit)
2. O Corpo Humano como Microcosmo (fractais cósmicos)
3. O Potencial que Decidiu Existir (criação e livre arbítrio)
4. A Eternidade em Forma de Pó (reencarnação quântica)
5. A Única Casa no Escuro (cosmologia e singularidade)
6. A Ilusão Sagrada da Matéria (física quântica + filosofia)
7. O Futuro que Ainda Não Decidimos (IA e consciência)

---

## 🎨 Tecnologias Utilizadas

### Frontend
- **HTML5** — Estrutura semântica e acessível
- **CSS3** — Design System "Cosmos" com tema dark personalizado
- **JavaScript (Vanilla)** — Navegação interativa e funcionalidades dinâmicas

### Bibliotecas e Recursos
- **Google Fonts** — Inter (UI), Merriweather (leitura), JetBrains Mono (código)
- **Material Icons** — Ícones de navegação
- **IndexedDB** — Armazenamento local de dados (módulo Infinity)

### APIs Modernas
- **IntersectionObserver** — Sincronização de scroll com navegação
- **CSS Variables** — Sistema de design tokens
- **Hash-based Routing** — Navegação fluida entre seções

---

## 📂 Estrutura do Projeto

```
universecode/
├── index.html              # Portal principal do UniverseCode
├── README.md               # Este arquivo
│
├── cosmos/                 # [Em desenvolvimento] Módulo Criativo
├── nexus/                  # [Em desenvolvimento] Módulo Matemático
├── infinity/               # [Em desenvolvimento] Módulo Literatura
│
├── literatura/             # Arquivos literários principais
│   ├── jornada.html       # A Grande Jornada do Cosmos
│   ├── potencial.html     # POTENCIAL
│   ├── script.js          # Scripts de navegação
│   └── style.css          # Estilos compartilhados
│
└── corrigidos/             # Versões revisadas e em desenvolvimento
    ├── jornada.html
    ├── potencial.html
    └── bigbang/           # Do Big Bang ao Fim do Universo (55 arquivos)
```

---

## 🚀 Como Usar

### Acesso Local

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/maccleyton/universecode.git
   cd universecode
   ```

2. **Abra o portal principal:**
   - Abra o arquivo `index.html` em seu navegador
   - Ou use um servidor local:
     ```bash
     python -m http.server 8000
     # Acesse: http://localhost:8000
     ```

3. **Navegue pelos módulos:**
   - Use a barra de navegação superior para acessar as suítes
   - Clique nos cards para explorar os módulos e literaturas

### Navegação nas Literaturas

Cada obra literária possui:
- **Sidebar interativa** com índice de capítulos
- **Navegação por hash** (`#capitulo1`, `#secao2`, etc.)
- **Scroll sincronizado** que destaca a seção atual
- **Design responsivo** para leitura em diferentes dispositivos

---

## 🎯 Design System "Cosmos"

O projeto utiliza um design system próprio com:

### Paleta de Cores
- **Cosmos (Azul):** `#1a7aff` — Módulo Criativo
- **Nexus (Verde):** `#00e676` — Módulo Matemático
- **Infinity (Vermelho):** `#c62828` — Módulo Literatura
- **Literatura (Branco):** `#ffffff` — Conteúdo literário

### Tipografia
- **Interface:** Inter (sans-serif)
- **Leitura:** Merriweather (serif)
- **Código:** JetBrains Mono (monospace)

### Componentes
- Cards interativos com hover effects
- Sidebars responsivas com scroll personalizado
- Modais informativos
- Sistema de badges de status (Planejamento, Desenvolvimento, Pronto)

---

## 🛣️ Roadmap

### Fase Atual (Q1 2025)
- [ ] Finalizar módulo **Infinity** (resolver problemas de IndexedDB)
- [ ] Integrar os três módulos ao repositório principal
- [ ] Completar "Do Big Bang ao Fim do Universo"

### Próximas Fases
- [ ] Desenvolver módulo **Cosmos** (editor e visualização)
- [ ] Desenvolver módulo **Nexus** (matemática simbólica)
- [ ] Implementar sistema de busca global
- [ ] Adicionar modo claro/escuro
- [ ] Otimizar performance e acessibilidade
- [ ] Criar API para integração entre módulos

---

## 🌟 Filosofia do Projeto

> "Inspirado por perguntas que precedem respostas — e por equações que sonham em ser versos."

O UniverseCode nasce da convicção de que ciência e arte não são domínios separados, mas diferentes expressões da mesma busca humana por compreensão. Aqui, equações se tornam poesia, simulações revelam beleza, e narrativas exploram os limites do conhecimento.

Este é um projeto em constante evolução, assim como o universo que busca compreender.

---

## 👨‍💻 Autor

**Cleyton D. Macedo**
Acadêmico de Engenharia de Software e Física

Criador das suítes *Cosmos*, *Nexus*, *Infinity* e autor de literaturas cósmicas que exploram a intersecção entre ciência, filosofia e metafísica.

---

## 📄 Licença

© 2025 Cleyton D. Macedo. Todos os direitos reservados.

---

## 🤝 Contribuições

Este é um projeto pessoal, mas sugestões e feedback são bem-vindos! Sinta-se à vontade para abrir issues ou enviar sugestões.

---

**UniverseCode** — Onde código, cosmos e consciência se encontram. 🌌✨
