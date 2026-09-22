---
fecha: 2026-09-22
tema: Qué es Jev, cómo funciona un modelo que decide en vez de conversar y si cambia el mapa de la IA en producto
bucket: El Futuro Aplicado
categoria: Opinión
vertical: Coyuntura & Opinión
hook_pattern: Dato Contraintuitivo
fuente: https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/
---

# La IA que decide sin hablar

Categoría: Opinión

Casi todo lo que un producto le pide a una IA no es una conversación. Es una decisión.

¿Este mail es urgente? ¿Este comando es peligroso? ¿A qué equipo va este ticket? Hoy se resuelve pidiéndole a un chat un "sí" o un "no" y esperando que respete el formato.

Jev, el modelo que TypeSafe AI lanzó la semana pasada, parte de otra premisa. No genera texto. Vos definís las respuestas posibles (una categoría, un puntaje, un sí o no) y el modelo devuelve la probabilidad de cada una, en una sola pasada.

Eso cambia tres cosas. No puede contestar fuera del menú. Responde, según la empresa, en 70 a 500 milisegundos. Y el código lee esa probabilidad directo. Vercel lo usó para revisar comandos y obtuvo resultados de 5 a 18 veces más rápido.

Diogo Almeida, su fundador y ex OpenAI, lo explica así. Optimizamos la IA para el lenguaje humano, y las computadoras hablan otro idioma.

No todos compran el cambio de paradigma. Sean Goedecke cree que un LLM común, forzado a responder con una sola palabra, lograría algo parecido. Armin Ronacher advierte que el problema de la alucinación se le delega un poco al usuario.

Lo que sí se mueve es el mapa. Un modelo que razona y conversa. Otro que decide rápido y barato, adentro del software.

Quizás la IA más útil de los próximos años sea una que nunca vas a ver hablar.

¿Cuántas "conversaciones" con IA de tu producto son, en realidad, una decisión?

#InteligenciaArtificial #ProductManagement #LLM #AIEngineering #StartupsLATAM

Fuente: https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/

---

## Notas internas (no publicar)

- **Cambio respecto de la versión anterior:** antes el post era una opinión sobre el sesgo escondido en un número (el experimento de Willison con las ciudades). Ahora explica qué es Jev, cómo funciona, en qué se diferencia de un LLM, qué beneficios trae y si es un cambio de paradigma, con las voces a favor y en contra.
- **Bucket:** El Futuro Aplicado. Explica la tecnología sin humo y la conecta con decisiones de producto reales.
- **Categoría:** Opinión, con tratamiento divulgativo. El sujeto es el mundo (una noticia de la semana), no el lector. No es Enseñanza porque no entrega un método: explica una novedad.
- **Hook elegido:** Dato Contraintuitivo, en versión conceptual. No abre con el nombre de la empresa, que recién aparece en el tercer párrafo.
- **Re-Hook:** tres preguntas de producto que cualquier PM reconoce, más el dolor de hoy (pedirle a un chat un "sí" y rezar por el formato).
- **El Giro:** el cambio no es de modelo, es de arquitectura. La IA se parte en dos piezas: una que conversa y otra que decide adentro del software, y la segunda se vuelve invisible.
- **CTA:** opinión rápida que invita a revisar el propio producto. Busca comentarios con casos concretos.
- **Voces citadas, con su origen:**
  - Cómo funciona (primitivas choice/score/sí-no, una sola pasada, "no escriben respuestas ni explican su razonamiento"): docs.typesafe.ai/concepts/system-one.
  - 70–500 ms: blog de lanzamiento de TypeSafe. Es cifra del vendor y el post la atribuye ("según la empresa").
  - Vercel, 5 a 18 veces más rápido: Pranit Sharma (ingeniero de Vercel) en TechCrunch.
  - Almeida, "the problem is we are optimizing for human language": TechCrunch. En el post va parafraseado en castellano, sin comillas, porque es traducción.
  - Goedecke (seangoedecke.com, "Jev means structured output is interesting again"): el escepticismo sobre el foso, porque un LLM con prefill y un solo token restringido podría replicarlo.
  - Ronacher (CTO de Earendil) en TechCrunch: "it delegates the hallucination problem a little bit to the user". También va parafraseado.
- **Citas verificadas contra el texto crudo de TechCrunch:** Almeida dijo "The problem is we are optimizing for human language … it's not useful for automation because computers speak a different language". Ronacher y Sharma, textuales como figuran arriba. La afirmación de Forkast sobre una ronda de US$40M quedó afuera porque no se puede corroborar.
- **Material de re-hook que no entró:** Almeida en Latent Space ("refusal is just, like, obviously a type error"), el primer comentario del hilo de HN ("Trading general purpose generation for fast typed inference") y el que dice que con 50–100 ejemplos un clasificador casero da 95% en emails.
