---
fecha: 2026-08-05
tema: Armar un set de evals propio para decidir qué modelo va a producción
bucket: Arquitectura de Producto
vertical: Educación
hook_pattern: Valor Operativo Directo
fuente: https://simonwillison.net/2026/Jul/31/smevals/#atom-everything
notion_page_id: 3b3b550f-b951-8102-ab72-e0ba01109c3e
---

# Tu benchmark propio vale más que cualquier leaderboard

Categoría: Educación

Antes de elegir un modelo, escribí las cinco cosas que tu producto tiene que resolver sí o sí. Eso es tu benchmark.

Suena obvio. Casi nadie lo hace. Por eso las decisiones de IA se siguen tomando mirando tablas que no dicen nada sobre tu caso.

Simon Willison publicó esta semana smevals, una herramienta chica para correr evaluaciones propias. En el anuncio admite algo que se agradece: es su tercer intento en varios años de encontrar un enfoque de evals que le convenza.

El vocabulario que propone es simple. Un eval es un conjunto de desafíos que responden una pregunta sobre un modelo. Un grader es lo que decide si pasó.

Su ejemplo es un haiku: ¿el modelo devuelve exactamente tres líneas no vacías?

Ridículo y perfecto. Porque es verificable, se repite igual siempre, y responde algo que a él le importa.

Cómo se ve eso en tu producto:

1. Escribí las cinco tareas que no pueden fallar.
2. Definí para cada una qué es "bien", de forma verificable.
3. Corré las opciones que estás mirando.
4. Guardá el resultado con fecha.
5. Repetilo cuando salga la próxima versión.

Lo que estás construyendo no es una comparación. Es memoria.

Dentro de seis meses vas a poder responder si mejoró, en vez de intuirlo.

Al final, el leaderboard mide lo que le importa a quien lo publicó. Vos tenés otro trabajo.

Guardalo para la próxima vez que tengas que justificar un cambio de modelo.

---

## Notas internas (no publicar)

- **Bucket:** Arquitectura de Producto — framework de decisión concreto para PM/builder, con alta tasa de guardado esperada.
- **Vertical:** Educación → awareness, maximizar guardados y dwell time. Formato lista táctica (5 ítems, el máximo permitido).
- **Hook elegido:** Valor Operativo Directo. Da la instrucción antes que el contexto: el lector puede ejecutar desde el primer renglón, y el resto del post justifica por qué.
- **Re-Hook:** "Suena obvio. Casi nadie lo hace" — fricción suave que instala la sospecha de que uno está del lado equivocado, sin acusar (patrón del CASO 002).
- **El Giro:** El eval no sirve para elegir hoy, sirve para tener memoria mañana. Reencuadra una tarea técnica como una capacidad organizacional, que es lo que la vuelve decisión de producto y no de ingeniería.
- **CTA:** Invitación al guardado, coherente con Educación. Anclado en un momento futuro concreto (justificar un cambio de modelo) para que el guardado tenga uso previsto.
- **Nota:** el ejemplo del haiku y la cita de la tercera iteración salen del anuncio de Willison; el resto de la ejecución en 5 pasos es elaboración propia, no está en la fuente.
