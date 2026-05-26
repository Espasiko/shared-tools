"""Tests placeholder. Smoke tests para verificar imports."""


def test_imports():
    """Smoke test: todos los módulos importables sin error."""
    from tools import capability, pdf_tools, search_tools, telemetry, vault_tools, verification

    assert hasattr(capability, "Capability")


def test_capability_abstract():
    """Capability.execute() debe lanzar NotImplementedError en clase base."""
    from tools.capability import Capability

    cap = Capability()
    try:
        cap.execute()
        assert False, "Debería haber lanzado NotImplementedError"
    except NotImplementedError:
        pass
