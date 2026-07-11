(() => {
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
