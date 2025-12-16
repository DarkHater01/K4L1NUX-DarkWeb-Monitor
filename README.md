# 🕵️‍♂️ K4L1NUX Dark Web Monitor

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Tor Required](https://img.shields.io/badge/Tor-Required-orange.svg)](https://www.torproject.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Monitor defensivo que escanea la Dark Web para detectar filtraciones de datos antes de que sean explotadas**

⚠️ **Aviso importante**: Este proyecto es 100% educativo. No almacena datos personales y usa hashing para proteger la privacidad.

---

## ⚡ Demo rápida

```bash
# Clona y prueba en 30 segundos
git clone https://github.com/tuusuario/K4L1NUX-DarkWeb-Monitor.git
cd K4L1NUX-DarkWeb-Monitor
python3 src/main.py --test
```

---

## 🎯 ¿Para quién es esto?

- 🔐 **Equipos de SOC** - Monitoreo proactivo de filtraciones
- 🏢 **Empresas** - Protección de datos corporativos  
- 🎓 **Estudiantes de ciberseguridad** - Aprender sobre OSINT/Tor
- 🔍 **Investigadores** - Búsqueda ética en la dark web

---

## 📊 Métricas que detecta

| Tipo | Ejemplo | Alerta |
|------|---------|--------|
| 🔑 Credenciales | emails@empresa.com | ⚠️ Alta |
| 💳 Tarjetas | 4111-1111-1111-1111 | ⚠️ Crítica |
| 🔐 Hashes | 5f4dcc3b5aa765d61d8327deb882cf99 | 🔍 Media |
| 📧 Dominios | @empresa.com | 👁️ Monitoreo |

---

## 🚀 Características Principales

- ✔ Scraping anónimo a través de **Tor**
- ✔ Soporte para múltiples sitios **.onion**
- ✔ **Anti-detection** básico (random user agents, delays, rotación)
- ✔ Detección de keywords en tiempo real
- ✔ Alertas por **Telegram, Discord y Email**
- ✔ Exportación en **JSON y Markdown**
- ✔ Arquitectura modular (fácil de extender)
- ✔ Dockerfile incluido (ejecución aislada)
- ✔ Logs limpios y cifrado/hash para privacidad

---

## 🛡️ Características de Seguridad

- ✅ **Sin almacenamiento de datos crudos** - Todo se hashea
- ✅ **Solo lectura** - No interactúa con sitios
- ✅ **Anonimato completo** - Todo pasa por Tor
- ✅ **Logs sanitizados** - No expone información sensible

---

## 🧱 Estructura del proyecto

```
K4L1NUX-DarkWeb-Monitor/
├── src/
│   ├── core/           # Tor Client, Scraper Framework, Parser, Hasher, Alerts
│   ├── modules/        # Sitios específicos (.onion)
│   ├── utils/          # Logger, Config Loader
│   └── main.py         # Entry point
├── config/             # Configuración y keywords
├── output/             # Resultados exportados
├── requirements.txt    # Dependencias Python
└── Dockerfile          # Contenedor aislado
```

---

## 🔧 Requisitos

- Python 3.10+
- Tor instalado y corriendo en socks5://127.0.0.1:9050
- Linux recomendado

### Instalar dependencias:

```bash
pip install -r requirements.txt
```

### Instalar Tor (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install tor
sudo systemctl start tor
```

---

## ▶️ Uso básico

```bash
# Ejecutar con keywords por defecto
python3 src/main.py

# Especificar archivo de keywords personalizado
python3 src/main.py --keywords config/my_keywords.txt

# Especificar archivo de salida
python3 src/main.py --output output/mis_resultados.json

# Modo debug (más información)
python3 src/main.py --debug
```

---

## 📦 Docker

### Build de la imagen:

```bash
docker build -t k4linux-darkweb-monitor .
```

### Ejecutar con Docker:

```bash
docker run -it --network host k4linux-darkweb-monitor
```

### Docker Compose (recomendado):

```yaml
version: '3.8'
services:
  monitor:
    build: .
    network_mode: "host"
    volumes:
      - ./config:/app/config
      - ./output:/app/output
```

---

## ⚙️ Configuración

### Archivo `config/settings.yaml`:

```yaml
tor:
  proxy: "socks5h://127.0.0.1:9050"
  timeout: 30

scraping:
  delay_min: 2
  delay_max: 5
  user_agents: "config/user_agents.txt"

alerts:
  telegram:
    enabled: false
    bot_token: ""
    chat_id: ""
  discord:
    enabled: false
    webhook_url: ""
```

### Archivo `config/keywords.txt`:

```
@miempresa.com
admin@
password
credit card
database leak
```

---

## 🗺️ Roadmap 2024

### Q2 2024 - v1.0 (Estable)
- [x] Core scraping engine
- [ ] 10+ módulos de foros .onion
- [ ] Alertas en tiempo real
- [ ] Dashboard web básico

### Q3 2024 - v2.0 (ML)
- [ ] Detección automática de leaks con IA
- [ ] API REST
- [ ] Plugins para SIEM (Splunk, Elastic)

### Q4 2024 - v3.0 (Enterprise)
- [ ] Autenticación multiusuario
- [ ] Reportes automáticos PDF
- [ ] Integración con VirusTotal, HaveIBeenPwned

---

## 🛡️ Ética & Legal

Este proyecto es solo para **fines educativos y de ciberseguridad defensiva**.  
El scraping de la Dark Web implica riesgos; úsalo bajo tu responsabilidad.

### Normas de uso ético:
1. Solo monitorea datos de organizaciones que tienes autorización para proteger
2. No almacenes información personal identificable (PII)
3. Respeta los términos de servicio de los sitios
4. No uses para actividades ilegales

---

## ⭐ Contribuciones

Las contribuciones están abiertas. Sigue estos pasos:

1. Haz fork del repositorio
2. Crea una rama (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Issues sugeridos para empezar:
- 🔧 Añadir soporte para más sitios .onion
- 📊 Mejorar sistema de exportación
- 🎨 Crear interfaz web básica
- 🔍 Optimizar detección de patrones

---

## 📚 Aprende más

- [Documentación de Tor](https://support.torproject.org/)
- [OSINT Framework](https://osintframework.com/)
- [Ética en ciberseguridad](https://www.eccouncil.org/cybersecurity-exchange/ethical-hacking/ethical-hacking-ethics/)

---

## 🤝 ¿Te gusta este proyecto?

1. **Dale una estrella** ⭐ - Ayuda a que más gente lo descubra
2. **Haz fork** - Mejora tu versión
3. **Contribuye** - Mira [CONTRIBUTING.md](CONTRIBUTING.md)
4. **Comparte** - En Twitter, LinkedIn, con tu equipo

## 📢 ¿Usas esto en tu empresa?
¡Nos encantaría saberlo! Abre un issue o contáctanos.

## ☕ ¿Quieres apoyar el desarrollo?
Considera [sponsorizar](https://github.com/sponsors/tuusuario) para nuevas features.

---

## 📄 Licencia

Distribuido bajo la licencia MIT. Ver `LICENSE` para más información.

## 📞 Contacto

Tu Nombre - [@tu_twitter](https://twitter.com/tu_twitter) - email@ejemplo.com

Link del proyecto: [https://github.com/tuusuario/K4L1NUX-DarkWeb-Monitor](https://github.com/tuusuario/K4L1NUX-DarkWeb-Monitor)

---

```
🛡️ K4L1NUX 
   ___       __   __    ___  _   _ _  __
  / _ \___  / /  / /   / _ \/ | / | |/ /
 / // / _ \/ /__/ /__ / , _/| |/ /|   / 
/____/\___/____/____/_/|_| |___/ |__/  
     DARK WEB MONITOR v0.1
```

**"Protegiendo datos, preservando privacidad"** 🔒