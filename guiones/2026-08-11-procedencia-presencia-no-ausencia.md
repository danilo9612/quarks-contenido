---
fecha: 2026-08-11
tema: Las marcas de agua confirman presencia y nunca ausencia; toda política de "demostrá que no usaste IA" es incontestable por diseño
bucket: El Futuro Aplicado
vertical: Coyuntura & Opinión
hook_pattern: Dato Contraintuitivo
fuente: https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content + https://www.theregister.com/ai-and-ml/2026/08/11/anthropic-pledges-to-embed-watermarks-to-help-discern-ai-slop-in-sop-to-eu/5285792
notion_page_id: 3b9b550f-b951-81b6-a293-e8823b7f79af
---

# Presencia sí, ausencia nunca

Categoría: Coyuntura & Opinión

Se puede probar que un texto salió de una IA. Lo contrario no se va a poder probar nunca.

Desde el 2 de agosto, los modelos nuevos de Anthropic embeben una marca imperceptible en el texto que sobrevive al copiar y pegar, y metadata de procedencia firmada en los archivos. Aplica a todos sus productos y responde a las exigencias de transparencia del AI Act europeo.

Lo interesante está en las limitaciones que la propia documentación admite.

Una marca detectada indica que el contenido "puede haber sido procesado" por el modelo. La ausencia de marca no indica nada. Un texto corto, muy editado o parafraseado pierde detectabilidad, y la metadata muere en una captura de pantalla.

El sistema confirma presencia. Ausencia, jamás.

Y ahí se caen la mitad de las políticas que se están escribiendo esta semana en universidades, en equipos de contratación y en revisiones de código. Cualquier regla con la forma "demostrame que esto no lo hizo una IA" es incontestable por diseño.

La que sí funciona tiene otra forma: declarame qué usaste y cómo lo verificaste.

La trazabilidad no llegó a resolver un problema de detección. Llegó a cambiar el costo de decir la verdad: sirve para el que declara, no contra el que esconde.

La pregunta útil dejó de ser quién lo escribió. Ahora es quién se hace cargo.

¿En tu equipo hay una regla escrita sobre esto, o cada uno improvisa?

Fuente: support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content

---

## Notas internas (no publicar)

- **Bucket:** El Futuro Aplicado — análisis sin hype de una capa técnica nueva y su consecuencia práctica inmediata para quien construye o gestiona equipos.
- **Vertical:** Coyuntura & Opinión → topical. Noticia de esta semana con lectura propia; CTA de reacción rápida.
- **Hook elegido:** Dato Contraintuitivo con forma de asimetría lógica. Todos leyeron la noticia como "ahora se puede detectar la IA"; el hook nombra lo que el anuncio no puede hacer, que es justo lo que la mayoría quiere usar.
- **Re-Hook:** el detalle técnico concreto (sobrevive al copiar y pegar, metadata firmada, AI Act) da la prueba de que el hook no es una opinión suelta.
- **El Giro:** el problema no es de detección sino de confianza institucional. La procedencia no atrapa al que oculta; abarata la honestidad del que declara. Eso mueve la discusión de la herramienta a la política interna del equipo.
- **CTA:** opinión/reacción rápida sobre la práctica del propio equipo. Binaria y respondible desde el celular → comment velocity.
- **Sin bloque de marca:** la vertical es Coyuntura, no Autoridad.

### Nota de fuentes

- Mecanismos verificados en la documentación oficial: marca imperceptible a nivel de modelo en texto (viaja con el copiar y pegar, persiste parcialmente tras ediciones) y metadata C2PA firmada en .svg, .png y .jpg.
- Limitaciones citadas textualmente de esa misma página: la marca detectada indica que el contenido "puede haber sido procesado"; la ausencia no prueba nada; texto corto o muy editado pierde detectabilidad; la metadata se pierde en conversiones de formato y capturas.
- Alcance verificado: modelos lanzados desde el 2 de agosto de 2026, con transición en curso para los anteriores.
- **Descartado:** las críticas sobre remoción de marcas (herramientas open source que borran C2PA) que menciona The Register. Son ciertas pero desvían el post hacia una discusión de seguridad; el ángulo elegido es la asimetría lógica, que se sostiene incluso si las marcas fueran infalsificables.
- **Descartado:** el artículo del AI Act. Ninguna de las dos fuentes lo especifica y no se nombra un número de artículo sin verificarlo.
