import numpy as np
import random

from collections import deque
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow import keras


class DDQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95  # discount rate
        self.epsilon = 0.5  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.8
        self.learning_rate = 0.001
        self.model = self._build_model()
        self.target_model = self._build_model()
        self.update_weights()
        self.replay_counter = 0

    def _build_model(self):

        model = Sequential()
        model.add(Dense(8, input_dim=self.state_size, activation='relu'))
        model.add(Dense(16, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        # Function adds information to the memory about last action and its results
        self.memory.append((state, action, reward, next_state, done))

    def get_action(self, state):
        """
        Compute the action to take in the current state, including exploration.
        With probability self.epsilon, we should take a random action.
            otherwise - the best policy action (self.get_best_action).

        Note: To pick randomly from a list, use random.choice(list).
              To pick True or False with a given probability, generate uniform number in [0, 1]
              and compare it with your probability
        """

        if np.random.random() <= self.epsilon:
            chosen_action = np.random.randint(0, self.action_size)
        else:
            chosen_action = self.get_best_action(state)

        return chosen_action

    def get_best_action(self, state):
        """
        Compute the best action to take in a state.
        """

        return np.argmax(self.target_model.predict(state))

    def replay(self, batch_size):
        """
        Function learn network using randomly selected actions from the memory. 
        First calculates Q value for the next state and choose action with the biggest value.
        Target value is calculated according to:
                Q(s,a) := (r + gamma * max_a(Q(s', a)))
        except the situation when the next action is the last action, in such case Q(s, a) := r.
        In order to change only those weights responsible for choosing given action, the rest values should be those
        returned by the network for state state.
        The network should be trained on batch_size samples.
        Also every time the function replay is called self.epsilon value should be updated according to equation:
        self.epsilon *= self.epsilon_decay
        After each 10 Q Network trainings parameters should be copied to the target Q Network
        """
        #
        # INSERT CODE HERE to train network
        #
        batch = random.sample(self.memory, batch_size)
        states = []
        targets = []

        for state, action, reward, next_state, done in batch:
            states.append(state.flatten())
            target = self.model.predict(state)
            if done:
                target[0][action] = reward
            else:
                q_future = max(self.target_model.predict(next_state)[0])
                target[0][action] = reward + q_future * self.gamma
            targets.append(target.flatten())

        self.model.train_on_batch(np.array(states), np.array(targets))

        self.replay_counter += 1

        if self.replay_counter == 10:
            self.replay_counter = 0
            self.update_weights()

    def update_weights(self):
        """copy trained Q Network params to target Q Network"""
        #
        # INSERT CODE HERE to train network
        #
        self.target_model.set_weights(self.model.get_weights())

    def update_epsilon_value(self):
        # Every each epoch epsilon value should be updated according to equation:

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def save(self):
        self.model.save("my_model")
        self.target_model.save("my_target_model")

    def load(self):
        self.model = keras.models.load_model('my_model')
        self.target_model = keras.models.load_model('my_target_model')
