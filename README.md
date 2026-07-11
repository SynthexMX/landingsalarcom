# Landings ALARCOM

## Ejecución
```bash
docker build -t alarcom-landings .
docker run --rm -p 8080:80 alarcom-landings
```

## Pendientes antes de producción
- Sustituir `{{META_PIXEL_ID}}` cuando Marketing entregue el identificador.
- Validar razón social y domicilio del responsable del aviso de privacidad.
- Confirmar el endpoint de formularios, validación servidor, CSRF, rate limiting, cifrado y retención.
- Terminar TLS en el proxy/CDN y habilitar HSTS allí.

## QA mínimo
Probar 320, 375, 768, 1024 y 1440 px; teclado; menú móvil; formularios; enlaces; consentimiento aceptado/rechazado; errores 404 y consola sin errores.
