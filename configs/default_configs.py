# configs/default_configs.py
from dataclasses import dataclass

@dataclass
class EnvConfig:
    max_steps: int = 200
    max_episodes: int = 1000
    gamma: float = 0.99
    learning_rate: float = 1e-4