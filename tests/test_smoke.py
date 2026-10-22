import engine

def test_engine_importable() -> None:
    assert engine.__name__ == "engine"