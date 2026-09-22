---
fecha: 2026-09-22
tema: El eval como especificación ejecutable que reemplaza al PRD
bucket: Arquitectura de Producto
categoria: Enseñanza
vertical: Educación
hook_pattern: Valor Operativo Directo
fuente: https://www.news.aakashg.com/p/how-to-build-your-first-eval
notion_page_id: 3deb550f-b951-815e-bf8c-c8758f18c5b0
---

# El eval reemplazó al PRD

Categoría: Enseñanza

El PRD que vas a escribir esta semana describe lo que esperás que pase. No lo demuestra.

Daniel McKinnon escribió los evals de Gemini, de Llama y de los Ray-Ban de Meta. Cuando un equipo le pide algo, contesta siempre lo mismo: no me mandes el PRD, mandame el eval.

Suena a capricho de ingeniero. Es una idea de producto.

Un documento describe el comportamiento que esperás. Un eval lo muestra: cien casos con la respuesta correcta al lado. Donde el texto admite interpretación, la planilla no.

Y armarlo no necesita equipo de research. Son seis pasos.

Primero, el problema en una oración: "extraer el nombre de quien escribe desde un mail de soporte". Si no entra en una oración, todavía no sabés qué estás construyendo.

Después el piso: el caso más fácil que el modelo tendría que resolver sí o sí. Y el techo: el que esperás que falle. El medio se llena por búsqueda binaria, hasta unos cien casos.

Hay una regla que no se negocia: nunca ablandes una respuesta incorrecta. Si un caso admite dos respuestas defendibles, se descarta. Un eval indulgente no mide, te felicita.

Ahí está lo interesante. Escribir un eval te obliga a decidir qué está bien antes de ver el resultado. El PRD te dejaba discutirlo después.

La especificación dejó de ser un documento. Ahora es algo que se corre.

Guardate esto para el próximo spec y arrancá por los diez casos más fáciles.

#ProductManagement #IA #Evals #Discovery #ProductoLATAM

Fuente: https://www.news.aakashg.com/p/how-to-build-your-first-eval

---

## Notas internas (no publicar)

- **Bucket:** Arquitectura de Producto — es método de especificación de producto, no análisis de coyuntura de IA.
- **Categoría:** Enseñanza. El sujeto de la primera oración es el lector y su artefacto ("el PRD que vas a escribir").
- **Vertical interna:** Educación → Awareness. Objetivo: guardado.
- **Hook elegido:** Valor Operativo Directo, con filo de Dato Contraintuitivo. Le habla a algo que el lector tiene agendado esta semana y le dice que está roto.
- **Re-Hook:** McKinnon como credencial verificable (Gemini, Llama, Ray-Ban) sosteniendo una instrucción que suena absurda: no me mandes el PRD. La tensión es "¿cómo que no?".
- **El Giro:** el eval no es una herramienta de QA, es un desplazamiento de poder en la definición. Obliga a decidir el criterio antes del resultado, y eso cierra la puerta a la discusión post-hoc.
- **CTA:** invitación al guardado + primer paso chico (los diez casos más fáciles). Coherente con Enseñanza.
- **Dato no usado, disponible para el visual:** McKinnon estima que hay menos de 100 PMs construyendo modelos frontier en el mundo.
