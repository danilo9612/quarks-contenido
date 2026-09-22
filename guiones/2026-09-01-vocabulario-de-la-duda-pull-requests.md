---
fecha: 2026-09-01
tema: Un análisis de 467.000 pull requests muestra que el vocabulario de la duda está desapareciendo, y en un PR la duda es información
bucket: Arquitectura de Producto
vertical: Educación
hook_pattern: Dato Contraintuitivo
fuente: https://louisabraham.github.io/load-bearing/
notion_page_id: 3ceb550f-b951-8157-aa72-ec5d239386e0
---

# El vocabulario de la duda está desapareciendo del código

Categoría: Educación

Alguien analizó 467.000 pull requests de GitHub y encontró que las palabras que están desapareciendo son las de la duda.

Seems. Perhaps. Probably. Basically. El grupo de vocabulario donde viven pasó del 36% al 4,5% en veinte meses.

El análisis agrupó 52 millones de palabras en diez familias. Una de esas familias no existía en 2025 y hoy aparece en casi cuatro de cada diez PRs atribuidos a personas.

Sus palabras más características: plainly, genuinely, deliberately, outright, asserted, premise.

Confianza pura. Cero cobertura.

Y acá está lo que importa, que no es una cuestión de estilo: en un pull request, la duda es información.

Cuando alguien escribe "creo que funciona, pero no probé el caso raro", le está dibujando un mapa al que revisa. Mirá acá primero.

Un registro uniformemente asertivo borra ese mapa. Todo suena igual de firme, así que nada señala dónde mirar, y revisar deja de ser leer para volverse auditar entero.

Tres cosas concretas para tu próximo PR:

Escribí tus incertidumbres explícitamente. Una línea de "esto lo asumí" vale más que tres párrafos prolijos.

Separá en la descripción lo que verificaste de lo que aceptaste del modelo.

Si salió de un agente, marcá qué parte no leíste con atención. Nadie te va a penalizar; quien revisa te lo va a agradecer.

Escribir con seguridad se volvió gratis. Escribir dónde no estás seguro es lo que quedó siendo trabajo humano.

Guardalo y probalo en el próximo.

---

## Notas internas (no publicar)

- **Bucket:** Arquitectura de Producto — es práctica de proceso de equipo y calidad de revisión, no análisis de tendencia tecnológica.
- **Vertical:** Educación → Awareness, CTA de guardado. El cuerpo entrega tres prácticas accionables, no solo el diagnóstico (regla de posts educativos: instructivos, no analíticos).
- **Hook elegido:** Dato Contraintuitivo. Lo esperable de un análisis así sería "la IA escribe nuestro código"; el hallazgo real es más fino y más raro: cambió el registro, no la autoría declarada.
- **Re-Hook:** Las cuatro palabras concretas (seems, perhaps, probably, basically) más la caída de 36% a 4,5%. Específico y verificable, justifica el click.
- **El Giro:** Lo que se perdió no es prolijidad, es señalización. La duda escrita cumplía una función técnica —orientaba al revisor— y al desaparecer el costo se traslada entero a quien revisa. El problema es de comunicación humana dentro de un proceso técnico.
- **CTA:** Invitación al guardado + aplicación inmediata, coherente con Educación.
- **Datos exactos de la fuente (verificados leyendo `analysis.js` del sitio, generado 2026-09-01):** 467.387 PRs, 602 días, 52.506.137 palabras, 86 semanas (2025-01-06 → 2026-08-24). 10 clusters por k-means con divergencia KL. El cluster "que llegó" pasó de 0,86% a 37,4% de share (39,5% promediando las últimas 4 semanas, que es la cifra que el propio sitio titula como "último mes"). El cluster en declive pasó de 35,6% a 4,5%.
- **Precisión a cuidar si se reescribe:** el cluster en declive contiene también nombres de usuario de GitHub de una comunidad específica, así que no es "el cluster de la duda" en sentido puro. El guion dice "el grupo de vocabulario donde viven", que es exactamente lo que la fuente sostiene. No convertirlo en "el vocabulario de la duda cayó 36 puntos" — eso sería sobreafirmar.
- **Corrección aplicada:** el resumen original que dejó el radar de scraping para esta noticia era incorrecto (decía que el análisis medía qué palabras del prompt mueven el output). No es eso: es un scraper de PRs de GitHub que mide qué vocabulario aparece y desaparece en el tiempo.
