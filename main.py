from tensorflow.python.keras.layers import Conv2D, MaxPooling2D, Flatten

from dqn_agent import DQNAgent
from t_rex_game_dqn import TRexGame
import numpy as np
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

from utils.settings import Settings

if __name__ == '__main__':

    env = TRexGame()

    state_size = env.state_size
    action_size = env.action_size
    learning_rate = 0.001

    model = Sequential()

    model.add(Conv2D(32, kernel_size=3, activation='relu', input_shape=(
        Settings.thumb_height, Settings.thumb_width, Settings.n_in_series)))
    model.add(MaxPooling2D(pool_size=(5, 5), strides=(2, 2)))
    model.add(Conv2D(64, (4, 4), activation='relu', strides=(1, 1)))
    model.add(MaxPooling2D(pool_size=(7, 7), strides=(3, 3)))
    model.add(Conv2D(128, (1, 1), strides=(1, 1), activation='relu'))
    model.add(MaxPooling2D(pool_size=(3, 3), strides=(3, 3)))
    model.add(Flatten())
    model.add(Dense(384, activation='relu'))
    model.add(Dense(64, activation="relu", name="layer1"))
    model.add(Dense(8, activation="relu", name="layer2"))
    model.add(Dense(action_size, activation="linear", name="layer3"))
    model.compile(loss='mse',
                  optimizer=Adam(lr=learning_rate))

    model.summary()

    # model.add(Dense(8, input_dim=state_size, activation='relu'))
    # model.add(Dense(16, activation='relu'))
    # model.add(Dense(32, activation='relu'))
    # model.add(Dense(action_size, activation='linear'))
    # model.compile(loss='mse',
    #               optimizer=Adam(lr=learning_rate))

    agent = DQNAgent(state_size, action_size, model)

    agent.epsilon = 0.75

    done = False
    batch_size = 64
    EPISODES = 1000
    counter = 0
    total_reward = 0

    # env.turn_off_display()

    for e in range(EPISODES):
        # if e == 2:
        #     env.turn_on_display()

        summary = []
        for _ in range(100):
            total_reward = 0
            env_state = env.reset()

            #
            # INSERT CODE HERE to prepare appropriate format of the state for network
            #
            state = np.array([env_state])

            for time in range(100):
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
                    print(env.text.score)
                    print(total_reward)
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
