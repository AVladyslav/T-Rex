from ddqn_agent import DDQNAgent
from t_rex_game_ddqn import TRexGame
import numpy as np


if __name__ == '__main__':

    env = TRexGame()

    state_size = env.state_size
    action_size = env.action_size

    agent = DDQNAgent(state_size, action_size)

    agent.epsilon = 0.75

    done = False
    batch_size = 64
    EPISODES = 1000
    counter = 0
    total_reward = 0

    for e in range(EPISODES):
        summary = []
        for _ in range(100):
            total_reward = 0
            env_state = env.reset()

            #
            # INSERT CODE HERE to prepare appropriate format of the state for network
            #
            state = np.array([env_state])

            for time in range(1000):
                action = agent.get_action(state)
                next_state_env, reward, done = env.step(action)
                total_reward += reward

                #
                # INSERT CODE HERE to prepare appropriate format of the next state for network
                #
                next_state = np.array([next_state_env])

                # add to experience memory
                agent.remember(state, action, reward, next_state, done)
                state = next_state
                if done:
                    break

            #
            # INSERT CODE HERE to train network if in the memory is more samples then size of the batch
            #
            if len(agent.memory) > batch_size:
                agent.replay(64)

            summary.append(total_reward)

        agent.update_epsilon_value()

        if np.mean(total_reward) > 195:
            print("You Win!")
            agent.save()
            break
        print("epoch #{}\tmean reward = {:.3f}\tepsilon = {:.3f}".format(e, np.mean(summary), agent.epsilon))

# TODO Change learning process, add points for successfully omitted cactus
# TODO alternatively - change Learning algorithm
