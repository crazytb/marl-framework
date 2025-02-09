# environments/base_env.py
import gymnasium as gym

class BaseEnvironment(gym.Env):
    def __init__(self, config):
        super().__init__()
        self.config = config
        
    def reset(self, seed=None):
        """Reset the environment and return initial observation."""
        super().reset(seed=seed)  # gym.Env의 reset 호출
        # 기본 구현은 빈 딕셔너리 반환
        return {}, {}
        
    def step(self, action):
        raise NotImplementedError