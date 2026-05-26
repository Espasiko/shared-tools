"""Operaciones sobre vault Obsidian via Local REST API plugin (puerto 27123).

Funciones:
- read_note(path): GET /vault/{path}
- create_note(path, content): PUT /vault/{path}
- update_note(path, content): PATCH /vault/{path}
- delete_note(path): DELETE /vault/{path}
- move_note(src, dst): POST /vault/{src}/_move
- list_notes(folder): GET /vault/{folder}/

Referencias:
- PRD §5.1 Tools universales
- Obsidian Local REST API: https://github.com/coddingtonbear/obsidian-local-rest-api

Estado: PLACEHOLDER — a implementar en Fase 1 (migrando desde OPOS_GEMINI_1/backend/agents/chandra_tools.py)
"""
