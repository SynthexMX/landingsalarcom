from pathlib import Path
import re

ROOT = Path('LANDING PAGE STITCH')
LANDINGS = ['guardias', 'control-accesos', 'cctv', 'gps']

CONSENT_JS = r'''(() => {
  'use strict';
  const KEY = 'alarcom_cookie_consent';
  const PIXEL_ID = '{{META_PIXEL_ID}}';
  const getChoice = () => localStorage.getItem(KEY);

  function loadMetaPixel() {
    if (window.fbq || PIXEL_ID.includes('{{')) return;
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://connect.facebook.net/en_US/fbevents.js';
    script.onload = () => {
      window.fbq = window.fbq || function(){ (window.fbq.queue = window.fbq.queue || []).push(arguments); };
      window.fbq('init', PIXEL_ID);
      window.fbq('track', 'PageView');
      window.fbq('track', 'ViewContent');
    };
    document.head.appendChild(script);
  }

  function setChoice(value) {
    localStorage.setItem(KEY, value);
    localStorage.setItem('alarcom_cookies_accepted', value === 'accepted' ? 'true' : 'false');
    document.getElementById('cookie-banner')?.classList.add('translate-y-full');
    if (value === 'accepted') loadMetaPixel();
  }

  document.documentElement.classList.add('js');
  document.addEventListener('DOMContentLoaded', () => {
    const banner = document.getElementById('cookie-banner');
    const accept = document.getElementById('accept-cookies');
    const reject = document.getElementById('reject-cookies');
    const choice = getChoice();

    if (!choice && banner) setTimeout(() => banner.classList.remove('translate-y-full'), 250);
    accept?.addEventListener('click', () => setChoice('accepted'));
    reject?.addEventListener('click', () => setChoice('rejected'));
    if (choice === 'accepted') loadMetaPixel();

    const preferences = document.createElement('button');
    preferences.type = 'button';
    preferences.className = 'cookie-preferences';
    preferences.textContent = 'Preferencias de cookies';
    preferences.addEventListener('click', () => {
      localStorage.removeItem(KEY);
      localStorage.removeItem('alarcom_cookies_accepted');
      banner?.classList.remove('translate-y-full');
    });
    document.body.appendChild(preferences);

    document.querySelectorAll('form').forEach((form) => {
      if (!form.querySelector('input[name="website"]')) {
        const trap = document.createElement('input');
        trap.type = 'text'; trap.name = 'website'; trap.tabIndex = -1;
        trap.autocomplete = 'off'; trap.setAttribute('aria-hidden', 'true');
        trap.className = 'form-honeypot'; form.appendChild(trap);
      }
      form.querySelectorAll('input').forEach((input) => {
        const key = `${input.name} ${input.id}`.toLowerCase();
        if (key.includes('nombre')) { input.autocomplete = 'name'; input.maxLength = 100; }
        if (key.includes('empresa')) { input.autocomplete = 'organization'; input.maxLength = 120; }
        if (input.type === 'email' || key.includes('correo')) { input.autocomplete = 'email'; input.maxLength = 254; }
        if (input.type === 'tel' || key.includes('telefono')) { input.autocomplete = 'tel'; input.inputMode = 'tel'; input.maxLength = 20; input.pattern = '[0-9+() .-]{7,20}'; }
      });
      form.addEventListener('submit', (event) => {
        if (form.querySelector('[name="website"]')?.value) { event.preventDefault(); return; }
        if (!form.checkValidity()) { event.preventDefault(); form.reportValidity(); return; }
        const button = form.querySelector('[type="submit"]');
        if (button?.disabled) { event.preventDefault(); return; }
        if (button) { button.disabled = true; button.setAttribute('aria-busy', 'true'); }
        sessionStorage.setItem('alarcom_valid_submission', '1');
      });
    });
  });
})();
'''

HARDENING_CSS = r'''
/* Progressive enhancement and accessibility */
html:not(.js) .reveal { opacity: 1 !important; transform: none !important; }
.form-honeypot { position: absolute !important; left: -10000px !important; width: 1px !important; height: 1px !important; overflow: hidden !important; }
.cookie-preferences { position: fixed; left: 12px; bottom: 12px; z-index: 39; min-height: 44px; padding: 8px 12px; border: 1px solid oklch(72% .04 220); border-radius: 8px; color: oklch(91% .015 220); background: oklch(20% .025 220); font: 600 12px/1.2 system-ui, sans-serif; cursor: pointer; }
:focus-visible { outline: 3px solid oklch(76% .15 73); outline-offset: 3px; }
button:disabled { cursor: wait; opacity: .65; }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important; scroll-behavior: auto !important; transition-duration: .01ms !important; }
  .reveal { opacity: 1 !important; transform: none !important; }
}
'''

COPY_FIXES = {
  'cctv': {
    'Acceso Biométrico': 'Cámaras IP',
    'App Móvil': 'Monitoreo remoto',
    'Barreras Vehiculares': 'DVR / NVR',
    'Control de Puertas': 'Actualización de sistema',
    'Estacionamiento': 'Videovigilancia perimetral',
    'Porque un acceso que no funciona es un acceso abierto.': 'Porque un sistema de vigilancia fuera de servicio deja puntos ciegos.',
    'distinguir unas placas o un rostro': 'distinguir una placa o un rostro',
  },
  'gps': {
    'Acceso Biométrico': 'Rastreo GPS',
    'Barreras Vehiculares': 'Telemetría y alertas',
    'Control de Puertas': 'Geocercas y rutas',
    'Estacionamiento': 'Plataforma web y app',
    'analizamos tus flotilla': 'analizamos tu flotilla',
    'Empresa Transporte Públicol': 'Empresa de transporte público',
    'Porque un acceso que no funciona es un acceso abierto.': 'Porque una unidad sin monitoreo deja tu operación sin visibilidad.',
    'Evaluamos tu espacio, tus flujos de personas y tus necesidades': 'Evaluamos tus unidades, rutas y necesidades operativas',
    'Un especialista evaluará tu espacio': 'Un especialista evaluará tu flotilla y operación',
  }
}

for slug in LANDINGS:
    page = ROOT / slug / 'index.html'
    text = page.read_text(encoding='utf-8')
    # Remove eager Meta bootstrap, retaining the untouched placeholder in consent.js.
    text = re.sub(r'<!--\s*Meta Pixel Code\s*-->.*?<!--\s*End Meta Pixel Code\s*-->', '', text, flags=re.I | re.S)
    text = re.sub(r'<script[^>]*src=["\']https://connect\.facebook\.net/[^>]+></script>', '', text, flags=re.I)
    for old, new in COPY_FIXES.get(slug, {}).items(): text = text.replace(old, new)
    # Guard scroll calculations on short pages.
    text = text.replace("var scrollPercent = Math.round((window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100);", "var scrollRange = document.documentElement.scrollHeight - window.innerHeight; var scrollPercent = scrollRange > 0 ? Math.round((window.scrollY / scrollRange) * 100) : 100;")
    if '../assets/consent.js' not in text:
        text = text.replace('</head>', '<link rel="stylesheet" href="../assets/hardening.css">\n<script defer src="../assets/consent.js"></script>\n</head>')
    page.write_text(text, encoding='utf-8')

    thanks = ROOT / slug / 'gracias.html'
    if thanks.exists():
        t = thanks.read_text(encoding='utf-8')
        t = re.sub(r'<!--\s*Meta Pixel Code\s*-->.*?<!--\s*End Meta Pixel Code\s*-->', '', t, flags=re.I | re.S)
        t = t.replace('</head>', '<meta name="robots" content="noindex,nofollow">\n<link rel="stylesheet" href="../assets/hardening.css">\n<script defer src="../assets/consent.js"></script>\n<script>document.addEventListener("DOMContentLoaded",()=>{if(sessionStorage.getItem("alarcom_valid_submission")!=="1"){const h=document.querySelector("h1,h2");if(h)h.textContent="Consulta el estado de tu solicitud";const p=h?.nextElementSibling;if(p)p.textContent="Esta página no confirma un envío. Regresa al formulario para solicitar una cotización.";}else{sessionStorage.removeItem("alarcom_valid_submission");}});</script>\n</head>')
        thanks.write_text(t, encoding='utf-8')

assets = ROOT / 'assets'; assets.mkdir(exist_ok=True)
(assets / 'consent.js').write_text(CONSENT_JS, encoding='utf-8')
(assets / 'hardening.css').write_text(HARDENING_CSS, encoding='utf-8')

# Add legally important clarifications without inventing company details.
privacy_note = '''\n<section><h2>Responsable y contacto para derechos ARCO</h2><p>Responsable: ALARCOM Seguridad Privada. Domicilio y razón social completa: pendientes de validación corporativa antes de publicación. Para solicitudes de acceso, rectificación, cancelación u oposición, escribe a <a href="mailto:contacto@grupoalarcom.com.mx">contacto@grupoalarcom.com.mx</a>.</p><h2>Datos operativos y geolocalización</h2><p>Según el servicio solicitado, podemos recibir cantidad de accesos, cámaras, guardias o unidades. En servicios GPS pueden tratarse ubicación, rutas, geocercas y telemetría únicamente para cotización, operación y soporte autorizados.</p><h2>Cookies y terceros</h2><p>Las cookies analíticas o publicitarias solo se activan después de tu consentimiento. Puedes cambiar tu decisión desde “Preferencias de cookies”.</p></section>\n'''
for slug in LANDINGS:
    p = ROOT / slug / 'privacidad.html'
    if p.exists():
        text = p.read_text(encoding='utf-8')
        if 'Responsable y contacto para derechos ARCO' not in text:
            text = text.replace('</main>', privacy_note + '</main>') if '</main>' in text else text.replace('</body>', privacy_note + '</body>')
        text = text.replace('</head>', '<link rel="stylesheet" href="../assets/hardening.css">\n<script defer src="../assets/consent.js"></script>\n</head>')
        p.write_text(text, encoding='utf-8')

# Nginx deployment hardening.
Path('nginx.conf').write_text(r'''server {
  listen 80;
  server_name _;
  root /usr/share/nginx/html;
  index index.html;
  server_tokens off;
  charset utf-8;

  add_header X-Content-Type-Options "nosniff" always;
  add_header Referrer-Policy "strict-origin-when-cross-origin" always;
  add_header X-Frame-Options "DENY" always;
  add_header Permissions-Policy "camera=(), microphone=(), geolocation=(), payment=(), usb=()" always;
  add_header Content-Security-Policy "default-src 'self'; base-uri 'self'; frame-ancestors 'none'; form-action 'self' https:; img-src 'self' data: https:; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdn.tailwindcss.com; font-src 'self' https://fonts.gstatic.com data:; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com https://connect.facebook.net; connect-src 'self' https://www.facebook.com https://connect.facebook.net; upgrade-insecure-requests" always;

  location / {
    limit_except GET HEAD POST { deny all; }
    try_files $uri $uri/ $uri.html =404;
  }
  location ~* /(?:\.git|\.github|scripts)/ { deny all; return 404; }
  location ~* \.(?:bak|conf|env|ini|log|md|sh|sql|ya?ml)$ { deny all; return 404; }
  location ~* \.(?:css|js|png|jpe?g|webp|svg|woff2?)$ { expires 30d; add_header Cache-Control "public, immutable"; try_files $uri =404; }
  error_page 404 /404.html;
}
''', encoding='utf-8')
Path('Dockerfile').write_text('FROM nginx:1.27-alpine\nCOPY nginx.conf /etc/nginx/conf.d/default.conf\nCOPY "LANDING PAGE STITCH" /usr/share/nginx/html\nEXPOSE 80\nHEALTHCHECK --interval=30s --timeout=3s CMD wget -q --spider http://127.0.0.1/ || exit 1\nCMD ["nginx", "-g", "daemon off;"]\n', encoding='utf-8')
Path('.dockerignore').write_text('.git\n.github\nscripts\n**/*.md\n**/.DS_Store\n**/*.bak\n**/*.log\n', encoding='utf-8')
Path('LANDING PAGE STITCH/404.html').write_text('<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Página no encontrada | ALARCOM</title><style>body{font:16px/1.5 system-ui;background:#061520;color:#d5e4f5;display:grid;min-height:100vh;place-items:center;margin:0}main{max-width:38rem;padding:2rem}a{color:#f4a340}</style><main><p>Error 404</p><h1>Página no encontrada</h1><p>La dirección no existe o cambió.</p><a href="./">Volver al portal</a></main></html>', encoding='utf-8')
Path('README.md').write_text('''# Landings ALARCOM\n\n## Ejecución\n```bash\ndocker build -t alarcom-landings .\ndocker run --rm -p 8080:80 alarcom-landings\n```\n\n## Pendientes antes de producción\n- Sustituir `{{META_PIXEL_ID}}` cuando Marketing entregue el identificador.\n- Validar razón social y domicilio del responsable del aviso de privacidad.\n- Confirmar el endpoint de formularios, validación servidor, CSRF, rate limiting, cifrado y retención.\n- Terminar TLS en el proxy/CDN y habilitar HSTS allí.\n\n## QA mínimo\nProbar 320, 375, 768, 1024 y 1440 px; teclado; menú móvil; formularios; enlaces; consentimiento aceptado/rechazado; errores 404 y consola sin errores.\n''', encoding='utf-8')
