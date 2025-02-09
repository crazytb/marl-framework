from configs.default_configs import EnvConfig
from environments.custom_envs.your_env import YourEnvironment
from agents.networks.custom_networks import YourNetwork
from core.trainer import Trainer

def main():
    # 설정 생성
    config = EnvConfig()
    
    # 환경 생성
    env = YourEnvironment(config)
    
    # 에이전트 생성
    agents = [YourAgent(i, env.observation_space.shape[0],
              env.action_space.n, config) 
              for i in range(env.n_agents)]
    
    # 학습 실행
    trainer = Trainer(env, agents, config)
    trainer.train()

if __name__ == "__main__":
    main()