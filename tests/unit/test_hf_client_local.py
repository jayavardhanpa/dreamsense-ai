from dreams.services.hf_client_local import LocalHFClient

def test_classify_emotion():
    client = LocalHFClient(default_sentiment_model="dummy-model")

    result = client.classify_emotion("I feel happy")
    assert isinstance(result, list)
    assert result[0]["label"] == "joy"
