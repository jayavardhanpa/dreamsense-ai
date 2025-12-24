from dreams.services.nlp_pipeline import process_text

class MockHFClient:
    def classify_emotion(self, text):
        return [{"label": "fear"}]

    def embed(self, texts):
        return [[0.1, 0.2, 0.3] for _ in texts]

def test_process_text():
    result = process_text("I was running and scared", MockHFClient())

    assert result["emotion"] == "fear"
    assert result["embedding"] is not None
    assert len(result["embedding"]) == 3
    assert result["clean_text"] == "I was running and scared"