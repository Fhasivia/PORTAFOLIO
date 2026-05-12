import streamlit as st

st.set_page_config(
    page_title="Laura Martínez Alzate | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;600&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
  background: #060c0a !important;
  color: #dff2ea !important;
  font-family: 'DM Sans', sans-serif;
}

[data-testid="stHeader"], [data-testid="stToolbar"],
[data-testid="stDecoration"], footer, #MainMenu { display: none !important; }

.block-container { padding: 0 !important; max-width: 100% !important; }

.page {
  width: 100%;
  padding: 40px 5vw 60px;
  background:
    radial-gradient(ellipse 70% 40% at 5% 0%, rgba(0,255,150,0.06) 0%, transparent 55%),
    radial-gradient(ellipse 50% 35% at 95% 100%, rgba(0,200,120,0.04) 0%, transparent 50%),
    #060c0a;
}

/* ─ TOP BAR ─ */
.topbar {
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 36px; padding-bottom: 20px;
  border-bottom: 1px solid rgba(0,255,150,0.10);
}
.topbar-logo {
  font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.05rem;
  color: #dff2ea; letter-spacing: -0.02em;
}
.topbar-logo span { color: #00ff96; }
.topbar-tag {
  font-family: 'JetBrains Mono', monospace; font-size: 0.65rem;
  color: rgba(223,242,234,0.30); letter-spacing: 0.12em; text-transform: uppercase;
}
.live-dot {
  display: inline-flex; align-items: center; gap: 7px;
  background: rgba(0,255,150,0.07); border: 1px solid rgba(0,255,150,0.20);
  border-radius: 100px; padding: 5px 14px;
  font-family: 'JetBrains Mono', monospace; font-size: 0.65rem;
  color: #00ff96; letter-spacing: 0.1em;
}
.live-dot::before {
  content: ''; width: 6px; height: 6px; background: #00ff96;
  border-radius: 50%; box-shadow: 0 0 6px #00ff96;
  animation: blink 2s infinite;
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.3} }

/* ─ BENTO ─ */
.bento {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 14px;
}

/* ─ BASE CELL ─ */
.cell {
  background: rgba(255,255,255,0.025);
  border: 1px solid rgba(0,255,150,0.09);
  border-radius: 16px;
  padding: 26px;
  position: relative; overflow: hidden;
  transition: border-color .25s, transform .25s, box-shadow .25s;
}
.cell::after {
  content:''; position:absolute; inset:0; border-radius:16px;
  background: linear-gradient(135deg,rgba(0,255,150,0.04) 0%,transparent 55%);
  opacity:0; transition:opacity .25s; pointer-events:none;
}
.cell:hover { border-color:rgba(0,255,150,0.28); transform:translateY(-3px); box-shadow:0 16px 44px rgba(0,0,0,0.45),0 0 20px rgba(0,255,150,0.06); }
.cell:hover::after { opacity:1; }

/* ─ HERO (8 cols) ─ */
.cell-hero { grid-column: span 8; padding:42px; background:rgba(0,255,150,0.03); border-color:rgba(0,255,150,0.13); }
.hero-eyebrow { font-family:'JetBrains Mono',monospace; font-size:0.68rem; color:#00ff96; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:18px; }
.hero-name { font-family:'Syne',sans-serif; font-weight:800; font-size:clamp(2.2rem,4vw,3.8rem); line-height:1.0; letter-spacing:-0.03em; color:#dff2ea; }
.hero-name em { color:#00ff96; font-style:normal; text-shadow:0 0 28px rgba(0,255,150,0.35); }
.hero-role { font-family:'JetBrains Mono',monospace; font-size:0.78rem; color:rgba(223,242,234,0.38); margin-top:14px; letter-spacing:0.04em; }
.hero-desc { font-size:0.92rem; color:rgba(223,242,234,0.55); line-height:1.75; max-width:460px; margin-top:18px; }

/* ─ STATS (4 cols) ─ */
.cell-stats { grid-column: span 4; display:flex; flex-direction:column; gap:10px; background:transparent; border:none; padding:0; }
.cell-stats:hover { transform:none; box-shadow:none; }
.cell-stats::after { display:none; }
.stat-box { flex:1; background:rgba(255,255,255,0.025); border:1px solid rgba(0,255,150,0.09); border-radius:14px; padding:18px 22px; display:flex; align-items:center; justify-content:space-between; transition:border-color .25s; }
.stat-box:hover { border-color:rgba(0,255,150,0.28); }
.stat-val { font-family:'Syne',sans-serif; font-weight:800; font-size:2rem; color:#00ff96; }
.stat-lbl { font-size:0.72rem; color:rgba(223,242,234,0.35); letter-spacing:0.08em; text-transform:uppercase; text-align:right; line-height:1.5; }

/* ─ SKILLS (4 cols) ─ */
.cell-skills { grid-column: span 4; }
.cell-label { font-family:'JetBrains Mono',monospace; font-size:0.62rem; color:rgba(0,255,150,0.50); letter-spacing:0.15em; text-transform:uppercase; margin-bottom:10px; }
.cell-title { font-family:'Syne',sans-serif; font-weight:700; font-size:1rem; color:#dff2ea; margin-bottom:14px; }
.skill-tags { display:flex; flex-wrap:wrap; gap:7px; }
.skill-tag { background:rgba(0,255,150,0.07); border:1px solid rgba(0,255,150,0.16); border-radius:7px; padding:4px 11px; font-family:'JetBrains Mono',monospace; font-size:0.68rem; color:#00ff96; }

/* ─ ABOUT (4 cols) ─ */
.cell-about { grid-column: span 4; }
.about-text { font-size:0.82rem; color:rgba(223,242,234,0.48); line-height:1.75; margin-top:8px; }
.about-loc { margin-top:14px; display:flex; align-items:center; gap:8px; font-family:'JetBrains Mono',monospace; font-size:0.68rem; color:rgba(0,255,150,0.55); }
.about-loc::before { content:'◎'; font-size:0.75rem; }

/* ─ SECTION HEADER (12 cols) ─ */
.cell-sec-hdr { grid-column:span 12; background:transparent; border:none; padding:8px 0 0; display:flex; align-items:baseline; gap:14px; }
.cell-sec-hdr:hover { transform:none; box-shadow:none; border-color:transparent; }
.cell-sec-hdr::after { display:none; }
.sec-num { font-family:'JetBrains Mono',monospace; font-size:0.62rem; color:rgba(0,255,150,0.38); }
.sec-title { font-family:'Syne',sans-serif; font-weight:800; font-size:clamp(1.2rem,2.2vw,1.7rem); color:#dff2ea; letter-spacing:-0.02em; }
.sec-line { flex:1; height:1px; background:linear-gradient(90deg,rgba(0,255,150,0.22) 0%,transparent 75%); }

/* ─ PROJECT CARD (3 cols each = 4 per row) ─ */
.cell-proj { grid-column:span 3; text-decoration:none !important; display:block; cursor:pointer; }
.proj-top { display:flex; align-items:flex-start; justify-content:space-between; margin-bottom:12px; }
.proj-icon { width:40px; height:40px; border-radius:10px; background:rgba(0,255,150,0.08); border:1px solid rgba(0,255,150,0.16); display:flex; align-items:center; justify-content:center; font-size:1.15rem; }
.proj-idx { font-family:'JetBrains Mono',monospace; font-size:0.60rem; color:rgba(0,255,150,0.30); letter-spacing:0.10em; }
.proj-title { font-family:'Syne',sans-serif; font-weight:700; font-size:0.92rem; color:#dff2ea; margin-bottom:6px; line-height:1.3; }
.proj-desc { font-size:0.76rem; color:rgba(223,242,234,0.40); line-height:1.6; margin-bottom:14px; }
.proj-footer { display:flex; align-items:center; justify-content:space-between; gap:8px; }
.proj-tags { display:flex; gap:5px; flex-wrap:wrap; }
.proj-tag { background:rgba(0,255,150,0.06); border:1px solid rgba(0,255,150,0.13); border-radius:5px; padding:2px 7px; font-family:'JetBrains Mono',monospace; font-size:0.60rem; color:rgba(0,255,150,0.65); }
.proj-arrow { width:26px; height:26px; border-radius:6px; background:rgba(0,255,150,0.07); border:1px solid rgba(0,255,150,0.16); display:flex; align-items:center; justify-content:center; font-size:0.72rem; color:#00ff96; transition:all .25s; flex-shrink:0; }
.cell-proj:hover .proj-arrow { background:rgba(0,255,150,0.18); border-color:rgba(0,255,150,0.50); transform:translate(2px,-2px); }

/* ─ FOOTER ─ */
.footer { margin-top:44px; padding-top:22px; border-top:1px solid rgba(0,255,150,0.08); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; }
.footer-name { font-family:'Syne',sans-serif; font-weight:700; font-size:0.9rem; color:#dff2ea; }
.footer-copy { font-family:'JetBrains Mono',monospace; font-size:0.62rem; color:rgba(223,242,234,0.22); }

::-webkit-scrollbar { width:5px; }
::-webkit-scrollbar-track { background:#060c0a; }
::-webkit-scrollbar-thumb { background:rgba(0,255,150,0.20); border-radius:3px; }
</style>
""", unsafe_allow_html=True)

projects = [
    {"title": "App de Audio",     "desc": "Procesamiento y análisis de audio con interfaces interactivas.",         "icon": "🎵", "url": "https://app-audio.streamlit.app/",                                     "tags": ["Audio", "DSP"]},
    {"title": "Detección",        "desc": "Detección inteligente con visión por computadora y modelos ML.",         "icon": "🔍", "url": "https://detecci-n-68fgkrrhas8ydz2moh8zbu.streamlit.app/",            "tags": ["CV", "ML"]},
    {"title": "Web Intro",        "desc": "Página de introducción y presentación personal interactiva.",            "icon": "🌐", "url": "https://miwebintro.streamlit.app/",                                  "tags": ["Web", "UI"]},
    {"title": "Sentimientos",     "desc": "NLP para clasificación emocional de textos en tiempo real.",             "icon": "🧠", "url": "https://sentimentoslaura.streamlit.app/",                           "tags": ["NLP", "AI"]},
    {"title": "TDF Español",      "desc": "Procesamiento de texto y análisis lingüístico en español.",              "icon": "📝", "url": "https://tdfesp-dmqheyywqfh4bqbcyvgtnx.streamlit.app/",             "tags": ["NLP", "Texto"]},
    {"title": "Proyecto HN",      "desc": "Análisis y visualización de datos avanzada.",                            "icon": "📊", "url": "https://hnlatmk6qyahgosdlysqu2.streamlit.app/",                    "tags": ["Data", "Viz"]},
    {"title": "Word Cloud",       "desc": "Generador visual de nubes de palabras personalizadas.",                  "icon": "☁️", "url": "https://wordcloudlaura.streamlit.app/",                            "tags": ["Viz", "NLP"]},
    {"title": "OCR",              "desc": "Reconocimiento óptico de caracteres y extracción de texto.",             "icon": "👁️", "url": "https://ocrlauramartinez.streamlit.app/",                         "tags": ["OCR", "CV"]},
    {"title": "OCR + Audio",      "desc": "OCR combinado con síntesis de voz para documentos.",                     "icon": "🔊", "url": "https://ocr-audio-lauramartinez.streamlit.app/",                   "tags": ["OCR", "Audio"]},
    {"title": "MQTT Receptor",    "desc": "Recepción y monitoreo de mensajes con protocolo MQTT.",                  "icon": "📡", "url": "https://recepmqtt-lauramartinez.streamlit.app/",                   "tags": ["IoT", "MQTT"]},
    {"title": "MQTT Emisor",      "desc": "Envío y publicación de mensajes en broker MQTT.",                        "icon": "📤", "url": "https://sendcmqtt-lauramaertinez.streamlit.app/",                  "tags": ["IoT", "MQTT"]},
    {"title": "Chat PDF",         "desc": "Chatea con documentos PDF usando inteligencia artificial.",              "icon": "💬", "url": "https://chatpdf-wuh2rzvhoofnbptnvewxrz.streamlit.app/",            "tags": ["AI", "LLM"]},
    {"title": "Control por Voz",  "desc": "Control de aplicaciones mediante comandos de voz en tiempo real.",       "icon": "🎤", "url": "https://ctrlvoice-lauramartinez.streamlit.app/",                   "tags": ["Voz", "CV"]},
    {"title": "Draw App",         "desc": "Aplicación de dibujo y creación visual interactiva.",                    "icon": "✏️", "url": "https://drawlauramartinez.streamlit.app/",                        "tags": ["CV", "UI"]},
    {"title": "Hand Draw",        "desc": "Dibujo mediante detección de gestos y movimiento de manos.",             "icon": "🖐️", "url": "https://drawhandlauramartinez.streamlit.app/",                    "tags": ["Gestos", "CV"]},
    {"title": "Vision App",       "desc": "Visión artificial para análisis y reconocimiento visual.",               "icon": "🤖", "url": "https://visionapp-lauramartinez.streamlit.app/",                   "tags": ["AI", "CV"]},
]

# Build project cards HTML
proj_html = ""
for i, p in enumerate(projects):
    idx = str(i + 1).zfill(2)
    tags_html = "".join(f'<span class="proj-tag">{t}</span>' for t in p["tags"])
    proj_html += f"""
    <a href="{p['url']}" target="_blank" class="cell cell-proj">
      <div class="proj-top">
        <div class="proj-icon">{p['icon']}</div>
        <div class="proj-idx">PRJ_{idx}</div>
      </div>
      <div class="proj-title">{p['title']}</div>
      <div class="proj-desc">{p['desc']}</div>
      <div class="proj-footer">
        <div class="proj-tags">{tags_html}</div>
        <div class="proj-arrow">↗</div>
      </div>
    </a>"""

page_html = f"""
<div class="page">

  <div class="topbar">
    <div class="topbar-logo">Laura<span>.</span>MartínezAlzate</div>
    <div class="topbar-tag">Data Science · ML · CV</div>
    <div class="live-dot">Disponible</div>
  </div>

  <div class="bento">

    <!-- HERO -->
    <div class="cell cell-hero">
      <div class="hero-eyebrow">// portfolio · 2025</div>
      <div class="hero-name">Laura <em>Martínez</em><br>Alzate</div>
      <div class="hero-role">Data Scientist &amp; Machine Learning Engineer</div>
      <div class="hero-desc">
        Construyo soluciones inteligentes con Python, ML y visión por computadora.
        Cada proyecto conecta datos con impacto real.
      </div>
    </div>

    <!-- STATS -->
    <div class="cell cell-stats">
      <div class="stat-box">
        <div class="stat-val">16</div>
        <div class="stat-lbl">Proyectos<br>desplegados</div>
      </div>
      <div class="stat-box">
        <div class="stat-val">AI</div>
        <div class="stat-lbl">Especialidad<br>principal</div>
      </div>
      <div class="stat-box">
        <div class="stat-val">∞</div>
        <div class="stat-lbl">Ideas en<br>proceso</div>
      </div>
    </div>

    <!-- SKILLS -->
    <div class="cell cell-skills">
      <div class="cell-label">// Stack tecnológico</div>
      <div class="cell-title">Habilidades</div>
      <div class="skill-tags">
        <span class="skill-tag">Python</span>
        <span class="skill-tag">Streamlit</span>
        <span class="skill-tag">OpenCV</span>
        <span class="skill-tag">NLP</span>
        <span class="skill-tag">TensorFlow</span>
        <span class="skill-tag">MQTT</span>
        <span class="skill-tag">OCR</span>
        <span class="skill-tag">LLMs</span>
        <span class="skill-tag">Data Viz</span>
        <span class="skill-tag">ML</span>
        <span class="skill-tag">Audio DSP</span>
        <span class="skill-tag">GitHub</span>
      </div>
    </div>

    <!-- ABOUT -->
    <div class="cell cell-about">
      <div class="cell-label">// Sobre mí</div>
      <div class="cell-title">Perfil</div>
      <div class="about-text">
        Apasionada por transformar datos en experiencias útiles. Trabajo con
        visión por computadora, procesamiento de lenguaje natural, IoT y aplicaciones
        de IA desplegadas en la nube.
      </div>
      <div class="about-loc">Medellín, Colombia</div>
    </div>

    <!-- SECTION HEADER -->
    <div class="cell cell-sec-hdr">
      <span class="sec-num">01</span>
      <span class="sec-title">Proyectos</span>
      <span class="sec-line"></span>
    </div>

    {proj_html}

  </div>

  <div class="footer">
    <div class="footer-name">Laura Martínez Alzate</div>
    <div class="footer-copy">Built with Streamlit · 2025 · Medellín, Colombia</div>
  </div>

</div>
"""

st.markdown(page_html, unsafe_allow_html=True)
