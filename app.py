import streamlit as st
from streamlit.components.v1 import html

cards = [
    {"id": "card-2025-09-13", "title": "13-09-2025", "content": "Hablé contigo, cuanto hubiese querido que fuera en persona, pero el ruido en mi cabeza no me daba paz. Quiero morir, nunca he estado peor en mi vida, perdí a la mujer de mi vida por ser inmaduro, en todo aspecto.

De cierta forma obtuve alivio con esa charla, pero la indiferencia y el resentimiento que coseché me revuelven el estomago y aprietan mi pecho profundamente. Es mi culpa, cuanto quisiera decir que no lo es: que no es de nadie, pero es mía.

Me arrepiento no haber estado para ti, porque si hubiese podido comunicarme no te habría perdido, al menos en el sentimiento. Porque te amo más que a nadie en el mundo, más que a mis padres, más que a mis abuelos, y te amaría más que a un hijo. El peor error de mi vida fue perderte y no solo eso, sino que las peores palabras las escuchaste de la persona que aún amabas, jamás voy a perdonarme a mí mismo, pero cuanto desearía que tu me perdonaras, porque aún no estoy seguro si lo hiciste.

Puedo dejar de mentir, porque no hay nada que conservar. Tuve pensamientos fugaces de terminar todo, por priorizar mi futuro, pero tonto yo que no entendí hasta hace unos meses que mi carrera solo es un medio para conseguir la felicidad, la felicidad que pude haber tenido contigo. Lo intenté todo porque no quería que nos separáramos, tuve charlas de noches enteras con muchos de mis amigos y aunque a veces no encontraba respuestas en otras ocasiones algo escuchaba en mi interior: que debía luchar por ti y quedarme a tu lado hasta el día de mi muerte, en ese proceso sentí tu indiferencia, y me carcomía sin encontrarle un sentido.

Muchas veces en la U y en privado hablaba del miedo que tenía por perderte. Me aterraba y ahora veo que en algo yo, si tenía la razón.

Es cierto, dije que eres un desastre, no te conocí así y entiendo que las circunstancias de la vida te metieron en un hoyo que cualquiera caería, siempre lo supe, siempre te entendí. Más aún ahora con la muerte de la mamá del Joaquín, a quien acompañé tal como lo hice contigo. Intenté seguir a tu lado, pero entiendo el asco que sentías hacia mí, traicioné tu confianza y no hay ninguna excusa que valga.

Dios sabe cuanto te amo y como jamás te olvidaré, no importa lo que pase, mi primer y único amor, la mujer que me enseñó que a amar y que te amen. Como quisiera haber luchado no solo en lo práctico, sino también en lo emocional, tener las herramientas necesarias y hacerte sentir amada, por todo el cariño que puedo darte, que no fue entregado.

No te escribí ni llamé por verte con alguien más, colapsé en llanto mucho antes ese día, ni siquiera te había visto. De todas formas es un dolor inimaginable.

Lamento terminar esta carta de esta manera, pero ya no hay forma de expresar el real cariño y amor que tengo por ti. Me niego a despedirme."},
    {"id": "card-2025-09-14", "title": "14-09-2025", "content": "Nada de lo que me digas me quita de la cabeza que eres el amor de mi vida, aunque entendí muchas cosas. Ni siquiera se si alguna vez verás estas cartas, porque no planeo avisarte de ellas, decidiste alejarte de mí y lo entiendo.

Otra vez me congelé, quise despedirme pero nuevamente, no sabía cómo. Las lágrimas se secan y sedimentan en mis lentes de sol, que debo lavar diariamente, de cierta forma me gusta ocultar parte del sufrimiento cuando me veo al espejo.

Quisiera contarte toda mi vida, todo lo que cambié, mejoré y mejoraré. Se supone que el sufrimiento de una ruptura se sana con tiempo y canalización en cosas de provecho hacia uno mismo, pero estoy acostumbrado a vivir por ti aunque así no lo veas, es así como puedo sobrevivir, es el propósito de mi  vida. 

Ya no hay nada nuevo que sepa lamentar, pero el dolor no se irá. No quiero dejarte ni en lo físico ni en lo emocional, seguiré diciendo “te amo antonia” repetidamente en mi cabeza, en voz alta, como se me ocurra en el momento.

Hasta el sentimiento de compartir un asiento en la micro lo extraño, sentir tu presencia y calidez, de apoyarte en mi hombro, y lamentablemente me recuerda a como nos encerrábamos en mi casa. Hoy tengo el tiempo libre de estar solo, de no estudiar, el conocimiento de mi pequeño mundo para poder llevarte a donde sea. Es algo que llegó a mi vida no por perderte, sino el hablar contigo.

Estoy en mi casa y aún siento un poco de tu aroma perdiéndose en mi chaqueta, cada cigarro es un recuerdo nuestro que consumo, y el sentir el sabor de la colilla quemándose el recuerdo de que las cosas terminaron. En esencia el cigarro es el mismo, y no quiero otros.

Las plantas brotan y muchos dicen que el amor es hormonal, pero el crecimiento de estas y especialmente en frutales es algo que perdura, los protegen y dan sostén a nuevos tejidos. Es cierto, es hormonal, pero gracias a eso llegan a la luz, gracias a eso despiertan después de un horrible invierno, floreciendo. Cuanto me gustaría verte florecer y me duele tanto que te hayas privado de ello, cuando era mi mayor deseo.

Florecer y vuelve a mí, vuelve a mí de la manera que quieras. Quédate conmigo."}
]

st.markdown("""
<style>
:root {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
html, body, .stApp {
  -webkit-user-select: none !important;
  -moz-user-select: none !important;
  -ms-user-select: none !important;
  user-select: none !important;
}
.nav {
  position: sticky;
  top: 0;
  background: rgba(255,255,255,0.95);
  padding: 10px;
  z-index: 1000;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  align-items: center;
  border-bottom: 1px solid rgba(0,0,0,0.06);
}
.nav a { text-decoration: none; }
.nav button {
  padding: 8px 12px;
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 6px;
  background: transparent;
  cursor: pointer;
  font-weight: 600;
}
.card {
  border-radius: 8px;
  padding: 20px;
  margin: 24px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  background: #ffffff;
}
.card h3 {
  margin: 0 0 8px 0;
  font-size: 18px;
}
.card-content {
  white-space: pre-wrap;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
</style>
""", unsafe_allow_html=True)

nav_html = '<div class="nav">'
for c in cards:
    nav_html += f'<a href="#{c["id"]}"><button>{c["title"]}</button></a>'
nav_html += '</div>'

st.markdown(nav_html, unsafe_allow_html=True)

for c in cards:
    st.markdown(
        f'''
        <div class="card" id="{c["id"]}" oncopy="return false" oncut="return false" onpaste="return false" oncontextmenu="return false" draggable="false" unselectable="on">
          <h3>{c["title"]}</h3>
          <div class="card-content">{c["content"]}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )
