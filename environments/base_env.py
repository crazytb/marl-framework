# environments/base_env.py
import gymnasium as gym

class BaseEnvironment(gym.Env):
    def __init__(self, config):
        super().__init__()
        self.config = config
        
    def reset(self):
        raise NotImplementedError
        
    def step(self, action):
        raise NotImplementedError