# agents/base_agent.py
class BaseAgent:
    def __init__(self, agent_id, obs_dim, action_dim, config):
        self.agent_id = agent_id
        self.obs_dim = obs_dim
        self.action_dim = action_dim
        self.config = config
        
    def select_action(self, obs):
        raise NotImplementedError
        
    def update(self, batch):
        raise NotImplementedError