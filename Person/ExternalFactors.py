class ExternalFactors:
    class ShortTerm:
        def __init__(self, noise_level=1, market_stability=1, tech_level=1):
            self.noise_level = noise_level
            self.market_stability = market_stability
            self.tech_level = tech_level

    class LongTerm:
        def __init__(self):
            pass
