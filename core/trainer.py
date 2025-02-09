# core/trainer.py
class Trainer:
    def __init__(self, env, agents, config):
        self.env = env
        self.agents = agents
        self.config = config
        
    def train(self):
        for episode in range(self.config.max_episodes):
            self.run_episode()
            
    def run_episode(self):
        obs = self.env.reset()
        done = False
        
        while not done:
            actions = {i: agent.select_action(obs[i]) 
                      for i, agent in enumerate(self.agents)}
            next_obs, rewards, done, _ = self.env.step(actions)
            
            # Update agents
            for i, agent in enumerate(self.agents):
                agent.update({
                    'obs': obs[i],
                    'action': actions[i],
                    'reward': rewards[i],
                    'next_obs': next_obs[i],
                    'done': done
                })
            
            obs = next_obs