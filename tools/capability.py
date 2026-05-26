"""Capability framework — abstracción universal de tools.

Clase abstracta agnóstica al LLM. Se traduce a tools (Mistral/OpenAI/Claude/Groq),
skills (Claude Skills), o agents (BMAD) según el adapter del LLM.

Referencias:
- PRD §5.2.2 Capability framework
- MCP entity Decisiones_Cerebrito_26_05_2026 (DECISION E)

Estado: PLACEHOLDER — a implementar en Fase 1.
"""

from typing import Any


class Capability:
    """Clase abstracta universal de una capacidad/herramienta.

    Subclases concretas (VaultRead, PDFExtract, etc.) heredan de aquí.
    Los adapters por LLM la traducen al formato nativo (function call, skill, agent).
    """

    name: str
    description: str
    triggers: list[str]
    verification_level: str = "medium"  # off / soft / medium / strict
    requires_confirm: bool = False
    vertiente: list[str] = []  # escritor / estudiante / abogado / opos / autonomo / investigador

    def execute(self, **kwargs: Any) -> Any:
        raise NotImplementedError("Subclases deben implementar execute()")
