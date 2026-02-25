from weather_api import get_weather


def test_get_weather_returns_dict(monkeypatch):
    """Проверяем, что функция возвращает словарь при корректном ответе API."""

    class MockResponse:
        def json(self):
            return {"main": {"temp": 20}, "weather": [{"description": "clear sky"}]}

        def raise_for_status(self):
            pass

    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    result = get_weather("Sofia")
    assert isinstance(result, dict)
    assert "main" in result
    assert "weather" in result
