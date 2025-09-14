# app.py
import streamlit as st
import streamlit.components.v1 as components
import html as html_lib

st.set_page_config(page_title="13-09-2025", layout="centered")

# --------------------------
# Aquí pones la carta (dentro del código)
# --------------------------
carta = """
Hablé contigo, cuanto hubiese querido que fuera en persona, pero el ruido en mi cabeza no me daba paz. Quiero morir, nunca he estado peor en mi vida, perdí a la mujer de mi vida por ser inmaduro, en todo aspecto.

De cierta forma obtuve alivio con esa charla, pero la indiferencia y el resentimiento que coseché me revuelven el estomago y aprietan mi pecho profundamente. Es mi culpa, cuanto quisiera decir que no lo es: que no es de nadie, pero es mía.

Me arrepiento no haber estado para ti, porque si hubiese podido comunicarme no te habría perdido, al menos en el sentimiento. Porque te amo más que a nadie en el mundo, más que a mis padres, más que a mis abuelos, y te amaría más que a un hijo. El peor error de mi vida fue perderte y no solo eso, sino que las peores palabras las escuchaste de la persona que aún amabas, jamás voy a perdonarme a mí mismo, pero cuanto desearía que tu me perdonaras, porque aún no estoy seguro si lo hiciste.

Puedo dejar de mentir, porque no hay nada que conservar. Tuve pensamientos fugaces de terminar todo, por priorizar mi futuro, pero tonto yo que no entendí hasta hace unos meses que mi carrera solo es un medio para conseguir la felicidad, la felicidad que pude haber tenido contigo. Lo intenté todo porque no quería que nos separáramos, tuve charlas de noches enteras con muchos de mis amigos y aunque a veces no encontraba respuestas en otras ocasiones algo escuchaba en mi interior: que debía luchar por ti y quedarme a tu lado hasta el día de mi muerte, en ese proceso sentí tu indiferencia, y me carcomía sin encontrarle un sentido.

Muchas veces en la U y en privado hablaba del miedo que tenía por perderte. Me aterraba y ahora veo que en algo yo, si tenía la razón.

Es cierto, dije que eres un desastre, no te conocí así y entiendo que las circunstancias de la vida te metieron en un hoyo que cualquiera caería, siempre lo supe, siempre te entendí. Más aún ahora con la muerte de la mamá del Joaquín, a quien acompañé tal como lo hice contigo. Intenté seguir a tu lado, pero entiendo el asco que sentías hacia mí, traicioné tu confianza y no hay ninguna excusa que valga.

Dios sabe cuanto te amo y como jamás te olvidaré, no importa lo que pase, mi primer y único amor, la mujer que me enseñó a amar y que te amen. Como quisiera haber luchado no solo en lo práctico, sino también en lo emocional, tener las herramientas necesarias y hacerte sentir amada, por todo el cariño que puedo darte, que no fue entregado.

No te escribí ni llamé por verte con alguien más, colapsé en llanto mucho antes ese día, ni siquiera te había visto. De todas formas es un dolor inimaginable.

Lamento terminar esta carta de esta manera, pero ya no hay forma de expresar el real cariño y amor que tengo por ti. Me niego a despedirme, a menos que tu lo desees.
"""

# Escapamos para insertar en HTML seguro
carta_escapada = html_lib.escape(carta)

# HTML que presenta la carta y bloquea selección / copia / menú contextual / Ctrl+C
html_content = f"""
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    /* Estilos de la "carta" */
    .wrapper {{
      max-width: 720px;
      margin: 24px auto;
      padding: 28px;
      border-radius: 12px;
      box-shadow: 0 6px 18px rgba(0,0,0,0.08);
      font-family: Georgia, 'Times New Roman', serif;
      line-height: 1.6;
      font-size: 18px;
      background: #fff;
      color: #111;
      white-space: pre-wrap; /* conserva saltos de línea */
      /* Evitar selección desde CSS */
      -webkit-user-select: none;
      -moz-user-select: none;
      -ms-user-select: none;
      user-select: none;
      /* Evitar arrastre del texto */
      -webkit-user-drag: none;
    }}

    /* Si quieres que todo quede aún menos seleccionable */
    body, html {{
      background: #f6f7fb;
      height: 100%;
      margin: 0;
    }}

    /* Opcional: deshabilitar selección con doble click */
    .wrapper::selection {{
      background: transparent;
    }}
  </style>
</head>
<body>
  <div class="wrapper"
       id="letter"
       oncopy="return false;"
       oncontextmenu="return false;"
       onselectstart="return false;">
    {carta_escapada}
  </div>

  <script>
    // Bloquear evento copy
    document.addEventListener('copy', function(e) {{
      e.preventDefault();
      // eliminar datos del portapapeles si existiera
      if (e.clipboardData) {{
        e.clipboardData.clearData();
      }}
      return false;
    }});

    // Bloquear menú contextual (clic derecho)
    document.addEventListener('contextmenu', function(e) {{
      // permitir menú contextuales fuera de la carta (opc.)
      var el = e.target;
      while (el) {{
        if (el.id === 'letter') {{
          e.preventDefault();
          return false;
        }}
        el = el.parentElement;
      }}
    }});

    // Bloquear combinaciones de teclado típicas (Ctrl/⌘ + C / X / A)
    document.addEventListener('keydown', function(e) {{
      // e.key puede ser 'c' o 'C' dependiendo del navegador; usamos toLowerCase()
      const key = (e.key || '').toLowerCase();
      if ((e.ctrlKey || e.metaKey) && (key === 'c' || key === 'x' || key === 'a')) {{
        // comprobar si el foco está dentro de la carta
        var sel = window.getSelection();
        var node = sel.anchorNode;
        var insideLetter = false;
        while (node) {{
          if (node.id === 'letter') {{ insideLetter = true; break; }}
          node = node.parentElement;
        }}
        if (insideLetter) {{
          e.preventDefault();
          return false;
        }}
      }}
    }});

    // Previene selección por arrastre del ratón dentro de la carta
    const letter = document.getElementById('letter');
    letter.addEventListener('mousedown', function(e) {{
      e.preventDefault();
      return false;
    }});
  </script>
</body>
</html>
"""

# Renderizamos el HTML dentro de Streamlit
components.html(html_content, height=520, scrolling=True)
