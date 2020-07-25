class GameStats():
    """외계인 침공 게임의 기록을 저장합니다."""

    def __init__(self, ai_settings):
        """기록을 초기화합니다."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """게임 도중에 바뀔 수 있는 기록을 초기화합니다."""
        self.ships_left = self.ai_settings.ship_limit