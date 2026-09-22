# Sistema de contenido de LinkedIn — Quarks Alchemist

Esta carpeta es el lugar de trabajo del contenido de LinkedIn de Quarks. Acá se escriben los
guiones, se renderizan las imágenes y los carruseles, y se guardan las salidas del radar de
noticias. El trabajo se hace **desde esta carpeta**, porque todas las skills escriben sus
salidas relativas al directorio actual.

## Dónde está la verdad

**Las reglas duras no viven en este archivo.** Viven en el brand kit compartido, porque las
skills lo leen siempre, incluso si se las invoca desde otra carpeta:

- `~/.claude/skills/quarks-brand/business_context.md` — identidad, audiencia, tono, buckets
  (§5), **las 3 categorías** (§6), cadencia y defaults (§7), objetivo (§8)
- `~/.claude/skills/quarks-brand/success_cases.md` — posts que funcionaron y por qué
- `~/.claude/skills/quarks-brand/brand_style_guide.md` — paleta, tipografías, logos

Este CLAUDE.md explica **el sistema y cómo se encadenan las skills**. Si una regla no está en
`business_context.md`, no es una regla — es una nota.

## Las 3 categorías

| | **Enseñanza** | **Opinión** | **Misceláneo** |
|---|---|---|---|
| Cuándo | lunes | jueves | 1 × mes, sin día fijo |
| Qué es | pensamiento de producto aplicable | noticia relevante + take propio | la marca en primera persona |
| Sujeto | el lector | el mundo | nosotros |
| Fuente | lista de temas (backlog) | radar + links del equipo | lo que pasa en Quarks |
| Visual | carrusel `slide_statement` | imagen `quote_photo` | foto real o `quote_photo` |

El detalle (sub-tipos de Misceláneo, prelación, reglas duras, test de clasificación) está en
`business_context.md` §6.

## El mapa de skills

```
                    ┌─ radar ────────────┐
                    │ scraping-noticias  │──┐
                    └────────────────────┘  │
                    ┌─ equipo (Discord) ─┐  ├──▶ cola en Notion ──▶ linkedin-guion ──▶ guiones/
                    │ manual: pegás link │──┤     (Categoría +                │
                    └────────────────────┘  │      Estado)                    │
                    ┌─ NotebookLM ───────┐  │                                 │
                    │ manual: pegás ideas│──┘                    ┌────────────┴────────────┐
                    └────────────────────┘                       ▼                         ▼
                                                          ig-carousels             linkedin-image
                                                        (Enseñanza →              (Opinión →
                                                       slide_statement)            quote_photo)
                                                               └──────────┬──────────┘
                                                                          ▼
                                                                     workspace/
```

| Skill | Qué hace | Cuándo |
|---|---|---|
| `scraping-noticias` | escanea fuentes, mide conversación, puntúa por género y crea páginas en Notion | Opinión (y más adelante un perfil aparte para Enseñanza) |
| `linkedin-guion` | escribe el guion de 200–250 palabras | las tres categorías |
| `ig-carousels` | carrusel 1080×1350 | Enseñanza |
| `linkedin-image` | imagen única | Opinión y Misceláneo |

**El orden es siempre el mismo:** tema → guion → validación tuya → visual. El visual nunca se
genera antes de que el guion esté aprobado.

## Defaults visuales (y cómo salirse)

- **Enseñanza → `ig-carousels` en modo light:** carrusel entero con `slide_statement` (fondo
  lavanda, spec de Figma). Los otros 18 templates oscuros existen y funcionan, pero **solo se
  usan si Danilo los pide explícitamente**.
- **Opinión → `linkedin-image` con `image_quote_photo`:** foto de fondo + gradiente + card.
  Los otros templates de imagen, solo a pedido explícito.
- **Antes de renderizar una imagen de Opinión**, se proponen en el chat varias opciones de
  título + chip (`eyebrow`) + escena de la foto (`photo_query`). Se renderiza recién con el OK.

## Entrega

Toda salida de imagen o carrusel se reporta con su **ruta absoluta** en el mensaje final, así
se puede subir a LinkedIn sin buscar el archivo. Si el cliente lo soporta, además se adjunta
el archivo en la conversación.

**El carrusel se entrega como PDF.** LinkedIn publica los carruseles como *document post*, y
lo que se sube es un `carrusel.pdf` con una página por slide (4:5 exacto, sin márgenes). Se
arma con `build_carousel_pdf.py` recién **después** de que apruebes los slides. Los PNGs
sueltos quedan en el batch para revisar, para Instagram, o para cambiar un slide y volver a
armar el PDF.

## Estructura de la carpeta

```
quarks-contenido/
├── CLAUDE.md          ← este archivo
├── guiones/           ← salida de linkedin-guion: YYYY-MM-DD-<slug>.md
├── workspace/         ← salida visual: YYYY-MM-DD/<slug>/ (imágenes y batches de carrusel)
├── salida-noticias/   ← salida del radar: candidates.json, scored.json
└── backlog/           ← temas semilla de Enseñanza, banco de misceláneos
```

## Cosas que conviene recordar

- **Todo en español rioplatense neutro. Nunca en inglés.**
- **Cero cifras inventadas.** Si no hay dato verificable, se cambia el formato visual, no se
  estima el número.
- **Antes de nombrar un cliente**, chequear NDA. El de Curcija está `pending`: ese proyecto se
  cuenta anonimizado.
- En Windows, los scripts de las skills van con `PYTHONUTF8=1`.
