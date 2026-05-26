"""Telemetría local Niveles 1+2 (RGPD-friendly, sin papeleo legal).

Eventos registrados en ~/.cerebrito/telemetry.jsonl:
- tool_called: qué herramienta y duración
- model_used: proveedor + modelo
- error_occurred: tipo y mensaje (sin contenido)
- session_duration: cuánto duró la sesión
- tokens_consumed: aproximado

NUNCA registra contenido del usuario, notas, ni respuestas del LLM.
Nivel 3 (envío anónimo) NO implementado inicialmente.

Referencias:
- PRD §11.4 Telemetría 3 niveles legalidad RGPD
- MCP entity Decisiones_Cerebrito_26_05_2026 (DECISION H)

Estado: PLACEHOLDER — a implementar en Fase 1
"""
