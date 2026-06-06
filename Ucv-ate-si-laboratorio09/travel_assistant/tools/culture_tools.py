def get_local_culture_recommendations(destination: str) -> dict:
    """Return basic local culture recommendations for a destination."""
    destination_normalized = destination.lower().strip()

    if "cusco" in destination_normalized:
        return {
            "status": "success",
            "destination": destination,
            "foods": ["Cuy al horno", "Chiri uchu", "Sopa de quinua"],
            "customs": [
                "Saludar cordialmente antes de pedir ayuda.",
                "Respetar los espacios arqueológicos y no tocar estructuras antiguas.",
                "Comprar artesanías locales puede apoyar a comunidades de la zona.",
            ],
            "useful_phrases": [
                "¿Cuánto cuesta?",
                "¿Dónde está la plaza principal?",
                "Gracias, muy amable.",
            ],
        }

    return {
        "status": "success",
        "destination": destination,
        "foods": ["Consultar platos típicos locales del destino."],
        "customs": ["Respetar normas culturales, horarios y costumbres locales."],
        "useful_phrases": [
            "Hola",
            "Gracias",
            "¿Dónde puedo encontrar información turística?",
        ],
    }
