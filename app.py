import streamlit as st

st.set_page_config(
    page_title="Laura Martínez Alzate | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;700&display=swap');

  /* ── Reset & Base ── */
  * { box-sizing: border-box; margin: 0; padding: 0; }

  html, body, [data-testid="stAppViewContainer"] {
    background: #050a08 !important;
    color: #e8f5f0 !important;
    font-family: 'Space Grotesk', sans-serif;
  }

  [data-testid="stAppViewContainer"] {
    background:
      radial-gradient(ellipse 80% 50% at 20% -10%, rgba(0,255,160,0.07) 0%, transparent 60%),
      radial-gradient(ellipse 60% 40% at 80% 110%, rgba(0,200,130,0.05) 0%, transparent 55%),
      #050a08 !important;
  }

  [data-testid="stHeader"], [data-testid="stToolbar"],
  footer, #MainMenu { display: none !important; }

  .block-container {
    padding: 0 !important;
    max-width: 100% !important;
  }

  /* ── Noise overlay ── */
  body::before {
    content: '';
    position: fixed; inset: 0; z-index: 0; pointer-events: none;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
    opacity: 0.4;
  }

  /* ── Hero ── */
  .hero {
    position: relative;
    padding: 90px 7vw 70px;
    border-bottom: 1px solid rgba(0,255,160,0.10);
    overflow: hidden;
  }

  .hero::after {
    content: '';
    position: absolute;
    top: -60px; right: -80px;
    width: 520px; height: 520px;
    background: radial-gradient(circle, rgba(0,255,160,0.09) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
  }

  .badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(0,255,160,0.08);
    border: 1px solid rgba(0,255,160,0.25);
    border-radius: 100px;
    padding: 6px 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: #00ffa0;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 28px;
  }

  .badge::before {
    content: '';
    width: 7px; height: 7px;
    background: #00ffa0;
    border-radius: 50%;
    box-shadow: 0 0 8px #00ffa0;
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
  }

  .hero-name {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: clamp(2.8rem, 7vw, 6rem);
    line-height: 1.0;
    letter-spacing: -0.03em;
    color: #e8f5f0;
    margin-bottom: 6px;
  }

  .hero-name span {
    color: #00ffa0;
    text-shadow: 0 0 40px rgba(0,255,160,0.4);
  }

  .hero-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: clamp(0.85rem, 1.8vw, 1.05rem);
    color: rgba(232,245,240,0.45);
    margin-top: 18px;
    letter-spacing: 0.04em;
  }

  .hero-desc {
    margin-top: 24px;
    font-size: 1.05rem;
    color: rgba(232,245,240,0.65);
    max-width: 520px;
    line-height: 1.7;
  }

  .hero-stats {
    display: flex; gap: 40px; flex-wrap: wrap;
    margin-top: 48px;
  }

  .stat {
    display: flex; flex-direction: column; gap: 4px;
  }

  .stat-num {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: #00ffa0;
  }

  .stat-label {
    font-size: 0.78rem;
    color: rgba(232,245,240,0.4);
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  /* ── Section titles ── */
  .section {
    padding: 70px 7vw;
  }

  .section-header {
    display: flex; align-items: center; gap: 20px;
    margin-bottom: 48px;
  }

  .section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: #00ffa0;
    letter-spacing: 0.15em;
    text-transform: uppercase;
  }

  .section-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: clamp(1.6rem, 3.5vw, 2.5rem);
    color: #e8f5f0;
    letter-spacing: -0.02em;
  }

  .divider {
    height: 1px;
    background: linear-gradient(90deg, rgba(0,255,160,0.3) 0%, transparent 70%);
    margin: 0 7vw;
  }

  /* ── Project cards grid ── */
  .projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 20px;
  }

  .card {
    position: relative;
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(0,255,160,0.10);
    border-radius: 16px;
    padding: 28px;
    transition: all 0.3s ease;
    overflow: hidden;
    cursor: pointer;
    text-decoration: none !important;
    display: block;
  }

  .card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(0,255,160,0.05) 0%, transparent 60%);
    opacity: 0;
    transition: opacity 0.3s;
    border-radius: 16px;
  }

  .card:hover {
    border-color: rgba(0,255,160,0.35);
    transform: translateY(-4px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.5), 0 0 30px rgba(0,255,160,0.08);
  }

  .card:hover::before { opacity: 1; }

  .card-index {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    color: rgba(0,255,160,0.5);
    letter-spacing: 0.1em;
    margin-bottom: 16px;
  }

  .card-icon {
    font-size: 1.8rem;
    margin-bottom: 14px;
    display: block;
  }

  .card-title {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 1.05rem;
    color: #e8f5f0;
    margin-bottom: 8px;
    line-height: 1.3;
  }

  .card-desc {
    font-size: 0.82rem;
    color: rgba(232,245,240,0.45);
    line-height: 1.6;
    margin-bottom: 20px;
  }

  .card-tag {
    display: inline-block;
    background: rgba(0,255,160,0.08);
    border: 1px solid rgba(0,255,160,0.18);
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 0.7rem;
    font-family: 'JetBrains Mono', monospace;
    color: #00ffa0;
    letter-spacing: 0.05em;
    margin-right: 6px;
    margin-bottom: 6px;
  }

  .card-arrow {
    position: absolute;
    top: 24px; right: 24px;
    width: 32px; height: 32px;
    background: rgba(0,255,160,0.08);
    border: 1px solid rgba(0,255,160,0.20);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.85rem;
    color: #00ffa0;
    transition: all 0.3s;
  }

  .card:hover .card-arrow {
    background: rgba(0,255,160,0.18);
    border-color: rgba(0,255,160,0.5);
    transform: translate(2px, -2px);
  }

  /* ── Footer ── */
  .footer {
    padding: 48px 7vw;
    border-top: 1px solid rgba(0,255,160,0.08);
    display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;
  }

  .footer-name {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 1.1rem;
    color: #e8f5f0;
  }

  .footer-copy {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: rgba(232,245,240,0.3);
  }

  /* scrollbar */
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: #050a08; }
  ::-webkit-scrollbar-thumb { background: rgba(0,255,160,0.25); border-radius: 3px; }
</style>
""", unsafe_allow_html=True)


# ── Projects data ──
projects = [
    {"title": "App de Audio", "desc": "Procesamiento y análisis de audio con interfaces interactivas.", "icon": "🎵", "url": "https://app-audio.streamlit.app/", "tags": ["Audio", "DSP"]},
    {"title": "Detección Inteligente", "desc": "Sistema de detección usando visión por computadora y modelos ML.", "icon": "🔍", "url": "https://detecci-n-68fgkrrhas8ydz2moh8zbu.streamlit.app/", "tags": ["CV", "ML"]},
    {"title": "Web Intro", "desc": "Página de introducción y presentación personal interactiva.", "icon": "🌐", "url": "https://miwebintro.streamlit.app/", "tags": ["Web", "UI"]},
    {"title": "Análisis de Sentimientos", "desc": "NLP para clasificación emocional de textos en tiempo real.", "icon": "🧠", "url": "https://sentimentoslaura.streamlit.app/", "tags": ["NLP", "AI"]},
    {"title": "TDF Español", "desc": "Herramienta de procesamiento de texto y análisis lingüístico.", "icon": "📝", "url": "https://tdfesp-dmqheyywqfh4bqbcyvgtnx.streamlit.app/", "tags": ["NLP", "Texto"]},
    {"title": "Proyecto HN", "desc": "Aplicación de análisis y visualización de datos avanzada.", "icon": "📊", "url": "https://hnlatmk6qyahgosdlysqu2.streamlit.app/", "tags": ["Data", "Viz"]},
    {"title": "Word Cloud", "desc": "Generador visual de nubes de palabras con datos personalizados.", "icon": "☁️", "url": "https://wordcloudlaura.streamlit.app/", "tags": ["Viz", "NLP"]},
    {"title": "OCR Inteligente", "desc": "Reconocimiento óptico de caracteres con extracción de texto.", "icon": "👁️", "url": "https://ocrlauramartinez.streamlit.app/", "tags": ["OCR", "CV"]},
    {"title": "OCR + Audio", "desc": "Combinación de OCR y síntesis de voz para documentos.", "icon": "🔊", "url": "https://ocr-audio-lauramartinez.streamlit.app/", "tags": ["OCR", "Audio"]},
    {"title": "MQTT Receptor", "desc": "Recepción y monitoreo de mensajes mediante protocolo MQTT.", "icon": "📡", "url": "https://recepmqtt-lauramartinez.streamlit.app/", "tags": ["IoT", "MQTT"]},
    {"title": "MQTT Emisor", "desc": "Envío y publicación de mensajes en broker MQTT.", "icon": "📤", "url": "https://sendcmqtt-lauramaertinez.streamlit.app/", "tags": ["IoT", "MQTT"]},
    {"title": "Chat PDF", "desc": "Chatea con tus documentos PDF usando inteligencia artificial.", "icon": "💬", "url": "https://chatpdf-wuh2rzvhoofnbptnvewxrz.streamlit.app/", "tags": ["AI", "LLM"]},
    {"title": "Control por Voz", "desc": "Interfaz de control de aplicaciones mediante comandos de voz.", "icon": "🎤", "url": "https://ctrlvoice-lauramartinez.streamlit.app/", "tags": ["Voz", "CV"]},
    {"title": "Draw App", "desc": "Aplicación de dibujo y creación visual interactiva.", "icon": "✏️", "url": "https://drawlauramartinez.streamlit.app/", "tags": ["CV", "UI"]},
    {"title": "Hand Draw", "desc": "Dibujo mediante detección de gestos y movimiento de manos.", "icon": "🖐️", "url": "https://drawhandlauramartinez.streamlit.app/", "tags": ["Gestos", "CV"]},
    {"title": "Vision App", "desc": "Sistema de visión artificial para análisis y reconocimiento visual.", "icon": "🤖", "url": "https://visionapp-lauramartinez.streamlit.app/", "tags": ["AI", "CV"]},
]

# ── Hero ──
st.markdown("""
<div class="hero">
  <div class="badge">✦ &nbsp; Portfolio &nbsp; · &nbsp; 2025</div>
  <div class="hero-name">Laura<br><span>Martínez</span><br>Alzate</div>
  <div class="hero-sub">// Data Scientist & ML Engineer</div>
  <div class="hero-desc">
    Construyo soluciones inteligentes con Python, Machine Learning y visión por computadora.
    Cada proyecto es un puente entre los datos y el mundo real.
  </div>
  <div class="hero-stats">
    <div class="stat"><div class="stat-num">16</div><div class="stat-label">Proyectos</div></div>
    <div class="stat"><div class="stat-num">∞</div><div class="stat-label">Ideas</div></div>
    <div class="stat"><div class="stat-num">AI</div><div class="stat-label">Especialidad</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Projects section ──
st.markdown("""
<div class="section">
  <div class="section-header">
    <div>
      <div class="section-label">// Proyectos desplegados</div>
      <div class="section-title">Mis Aplicaciones</div>
    </div>
  </div>
  <div class="projects-grid">
""", unsafe_allow_html=True)

for i, p in enumerate(projects):
    tags_html = "".join(f'<span class="card-tag">{t}</span>' for t in p["tags"])
    idx = str(i + 1).zfill(2)
    st.markdown(f"""
    <a href="{p['url']}" target="_blank" class="card">
      <div class="card-arrow">↗</div>
      <div class="card-index">PRJ_{idx}</div>
      <span class="card-icon">{p['icon']}</span>
      <div class="card-title">{p['title']}</div>
      <div class="card-desc">{p['desc']}</div>
      <div>{tags_html}</div>
    </a>
    """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# ── Divider ──
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Footer ──
st.markdown("""
<div class="footer">
  <div class="footer-name">Laura Martínez Alzate</div>
  <div class="footer-copy">Built with Streamlit · 2025</div>
</div>
""", unsafe_allow_html=True)
