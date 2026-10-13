# Security Policy

## Uso previsto

K4L1NUX DarkWeb Monitor es una herramienta **defensiva**. Sirve para detectar
filtraciones de datos en contenido que el operador ya posee o está autorizado a
analizar (p. ej. un dump propio, un volcado de auditoría o una fuente pública).

Está prohibido usarla para acceder o exfiltrar datos de terceros sin
autorización explícita. El autor no se responsabiliza del mal uso.

## Privacidad por diseño

- El monitor **nunca** persiste el valor crudo de un hallazgo.
- Cada coincidencia se guarda solo como `fingerprint` SHA-256 y valor enmascarado.
- Puedes añadir sal con la variable de entorno `K4L1NUX_SALT`.
- No se interactúa con los sitios: solo lectura.

## Reportar una vulnerabilidad

Abre un aviso privado en el repositorio (Security > Report a vulnerability) o
contacta por email. No publiques exploits en issues abiertos.
