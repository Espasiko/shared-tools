# shared-tools

Almacén común de tools Python para los backends [Cerebrito](https://github.com/Espasiko/cerebrito-backend) y [OPOS_GEMINI_1](https://github.com/Espasiko/OPOS_GEMINI_1) (Chandra Edition).

## Qué hay aquí

Módulos Python reutilizables entre los dos backends. Una sola fuente de verdad para evitar duplicación.

| Módulo | Descripción | Estado |
|---|---|---|
| `capability.py` | Clase abstracta `Capability` (agnóstica al LLM) | Placeholder (Fase 1) |
| `vault_tools.py` | Operaciones sobre vault Obsidian via REST API | Placeholder (Fase 1) |
| `pdf_tools.py` | Cascada: pypdf → Mistral OCR cloud → EasyOCR local | Placeholder (Fase 1) |
| `search_tools.py` | Búsqueda internet: Tavily + DuckDuckGo fallback | Placeholder (Fase 1) |
| `telemetry.py` | Logs locales Niveles 1+2 (RGPD-friendly) | Placeholder (Fase 1) |
| `verification.py` | Anti-alucinación configurable por vertiente | Placeholder (Fase 1) |

## Uso como submódulo git

En el repo padre (`cerebrito-backend` u `OPOS_GEMINI_1`):

```bash
git submodule add https://github.com/Espasiko/shared-tools.git shared-tools
git submodule init
git submodule update
```

Para actualizar a la última versión:

```bash
git submodule update --remote shared-tools
git add shared-tools
git commit -m "chore: bump shared-tools to latest"
```

## Importar en código Python

```python
from shared_tools.tools.capability import Capability
from shared_tools.tools.vault_tools import read_note, create_note
from shared_tools.tools.pdf_tools import extract_pdf
```

## Instalación standalone (para tests)

```bash
pip install -e .              # base
pip install -e ".[ocr-local]" # + EasyOCR
pip install -e ".[dev]"       # + pytest, ruff
```

## Licencia

MIT — ver [LICENSE](LICENSE).

Forkeable y reutilizable. Atribución requerida.

---

*Creado el 26/05/2026 como parte de Fase 0 del proyecto Cerebrito.*
*Documentación: [obsidian-bmo-chatbot-plus/docs_planes/](https://github.com/Espasiko/obsidian-bmo-chatbot-plus/tree/feature/multi-chat/docs_planes)*
