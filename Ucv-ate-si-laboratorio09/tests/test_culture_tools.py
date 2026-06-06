from travel_assistant.tools.culture_tools import get_local_culture_recommendations


def test_get_local_culture_recommendations_for_cusco():
    result = get_local_culture_recommendations("Cusco")

    assert result["status"] == "success"
    assert result["destination"] == "Cusco"
    assert len(result["foods"]) >= 1
    assert len(result["customs"]) >= 1
    assert len(result["useful_phrases"]) >= 1


def test_get_local_culture_recommendations_default_case():
    result = get_local_culture_recommendations("Paris")

    assert result["status"] == "success"
    assert len(result["foods"]) >= 1
    assert len(result["customs"]) >= 1
    assert len(result["useful_phrases"]) >= 1
