---
fecha: 2026-08-25
tema: más de la mitad del tráfico web ya no tiene ojos — qué cambia al construir un sitio con dos lectores
bucket: El Futuro Aplicado
vertical: Educación
hook_pattern: Valor Operativo Directo
fuente: https://stackoverflow.blog/2026/08/21/get-rid-of-your-captcha-the-future-of-the-web-is-bots/
evidencia: Cloudflare Radar — 57,5% del tráfico HTML automatizado vs 42,5% humano (2026)
notion_page_id: 3c7b550f-b951-8120-9eea-fb05b6bdb2b1
---

# El sitio tiene dos lectores

Categoría: Educación

Más de la mitad de las visitas a un sitio ya no tienen ojos.

Cloudflare Radar mide el tráfico HTML de la web y hoy el 57,5% de los pedidos son automatizados. Los humanos quedaron en 42,5%. La mayoría de esos crawlers todavía viene a entrenar modelos, pero una porción chica y creciente viene a buscar una respuesta para alguien.

Eso deja algo práctico sobre la mesa: el sitio tiene dos lectores y solo estamos diseñando para uno.

Lo que estamos revisando en los proyectos:

1. El dato que vive solamente dentro de una imagen o un gráfico es un dato invisible.
2. Si el precio, la dirección o el horario aparecen recién después de un click en JavaScript, para el agente no existen.
3. Los títulos que ganan concursos de creatividad pierden contra los que dicen qué hay abajo.
4. El CAPTCHA que frena a un bot malo también frena al agente que venía a comprar en nombre de un cliente.
5. Un contenido bien estructurado sirve a los dos lectores. Dos versiones separadas se desincronizan en un mes.

Ninguna de estas es una técnica nueva. Son las mismas reglas de siempre sobre escribir claro, con un lector que no perdona la ambigüedad y que no pregunta dos veces.

Guardalo y pasá tu home por los cinco puntos antes del próximo sprint. ¿Cuántos aprueba?

---

## Notas internas (no publicar)

- **Bucket:** El Futuro Aplicado — tendencia aplicable hoy, sin especulación.
- **Vertical:** Educación → formato lista táctica (5 ítems, el máximo permitido), CTA de guardado.
- **Hook elegido:** Valor Operativo Directo con giro contraintuitivo ("visitas que no tienen ojos"). Personifica el dato antes de darlo.
- **Re-Hook:** la cifra de Cloudflare confirma la afirmación rara del hook en la línea siguiente. Sin eso, el hook suena a metáfora vacía.
- **El Giro:** la accesibilidad para máquinas termina siendo la vieja disciplina de escribir claro — el problema es de comunicación, no de infraestructura.
- **CTA:** guardado + micro-desafío medible ("¿cuántos aprueba?"), que además habilita comentario.
- **Evidencia dura:** Cloudflare Radar (57,5% / 42,5%). Deliberadamente NO se mezcla con el dato de Imperva (53% de todo el tráfico): miden universos distintos y promediarlos sería un error. El post del blog de Stack Overflow queda como disparador en el frontmatter.
- **Decisión:** no se nombra al ejecutivo citado en la nota original. La afirmación se sostiene en el dato institucional, no en la autoridad de una persona cuyo rol habría que verificar.
- **Impronta:** plural institucional, registro medio, sin "no es X, es Y".
