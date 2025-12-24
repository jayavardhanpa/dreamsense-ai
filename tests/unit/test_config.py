from dreams.config import load_properties

def test_load_properties(sample_config):
    props = load_properties(sample_config)
    assert props["ENV"] == "dev"
    assert props["LOG_LEVEL"] == "DEBUG"
    assert props["HF_MODEL"] == "test-model"

def test_env_var_override(monkeypatch, sample_config):
    monkeypatch.setenv("LOG_LEVEL", "INFO")
    props = load_properties(sample_config)
    # env vars override properties
    assert props["LOG_LEVEL"] == "INFO"