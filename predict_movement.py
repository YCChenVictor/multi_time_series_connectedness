import tensorflow as tf
import pickle
import os
import functions.f_match_in_out as fmio
import numpy as np


# obtain movement and rolling connectedness data
file_path = os.path.dirname(os.path.realpath(__file__))
move_path = file_path + '/docs/' + 'movement.pickle'
roll_conn_path = file_path + '/docs/' + 'roll_conn.pickle'
with open(move_path, 'rb') as f:
    move = pickle.load(f)
with open(roll_conn_path, 'rb') as f:
    roll_conn = pickle.load(f)


# hyperparameters
n_conn = len(roll_conn.columns)-2  # The number of calculated connectedness
n_inst = len(move.columns)-1   # The number of financial instrumnets
n_inputs = n_conn
n_outputs = n_inst
lr = 0.001                  # learning rate
training_iters = 100000     # the limit of train steps
batch_size = 1            # the number of batch to be input
n_steps = 1                 # time steps
n_hidden_units = 128       # neurons in hidden layer


# x y placeholder
"""
The shape of x = [batcch_size, steps, inputs]

batch size means the number of data with shape: n_steps * n_inputs to be input
to model each step.

what we are going to input is penal data; the n_steps means the periods to be
input into in each batch; and n_inputs means the number of datatype to be
input in each batch
"""
x = tf.placeholder(tf.float32, [batch_size, n_steps, n_inputs])
y = tf.placeholder(tf.float32, [batch_size, n_steps, n_outputs])
y_shape = tf.shape(y)


# The initial value of weights biases
weights = {
    # shape (n_inputs, n_hidden_units)
    'in': tf.Variable(tf.random_normal([n_inputs, n_hidden_units])),
    # shape (n_hidden_units, n_classes)
    'out': tf.Variable(tf.random_normal([n_hidden_units, n_outputs]))
}
biases = {
    # shape (n_hidden_units, )
    'in': tf.Variable(tf.constant(0.1, shape=[n_hidden_units, ])),
    # shape (n_classes, )
    'out': tf.Variable(tf.constant(0.1, shape=[n_outputs, ]))
}


def RNN(X, weights, biases):
    # initial X is of three dimension. Turn X into two dimension to dot with
    # weights
    # X ==> (n_batches * n_steps, n_inputs)
    X = tf.reshape(X, [-1, n_inputs])

    # X_in = W*X + b
    X_in = tf.matmul(X, weights['in']) + biases['in']

    # X_in ==> (n_batches, n_steps, n_hidden) back to three dimesion
    X_in = tf.reshape(X_in, [-1, n_steps, n_hidden_units])

    # 使用 basic LSTM Cell.
    lstm_cell = tf.nn.rnn_cell.LSTMCell(n_hidden_units, forget_bias=1.0, state_is_tuple=True)

    # initialize the states to zeros
    init_state = lstm_cell.zero_state(batch_size, dtype=tf.float32)

    # calculates the output and state
    outputs, final_state = tf.nn.dynamic_rnn(lstm_cell, X_in, initial_state=init_state, time_major=False)

    # use the state and weight to calculate the prediction
    results = tf.matmul(final_state[1], weights['out']) + biases['out']

    return results


# get the predictions (not yet turn to 0 and 1)
preds = RNN(x, weights, biases)[0]
preds_0_1 = tf.round(preds)

# compare the prediction and the actual labels to get the cost
cost = tf.reduce_mean(tf.square(preds - y))

# the training is to minimize the cost
optimizer = tf.train.GradientDescentOptimizer(learning_rate=lr)
train = optimizer.minimize(cost)

# get the correct prediction
correct_pred = tf.equal(preds_0_1, y)

# use the number of correct prediction to calculate accuracy
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# initialize tensorflow
init = tf.global_variables_initializer()

# start the tensorflow session
with tf.Session() as sess:
    # initialize
    sess.run(init)
    # if the number of training > training_iters => break
    step = 0

    # get the input and output
    roll_conn_list = fmio.divide_df_into_batches(roll_conn, 1)
    match_dict = fmio.match(roll_conn_list, move)

    for name, item in match_dict.items():

        # get the dataframe of input and output
        Date = match_dict[name]["in"]["Date"]
        batch_xs_df = match_dict[name]["in"].drop(["accuracy", "Date"], axis=1)
        batch_ys_df = match_dict[name]["out"].drop(["Date"], axis=1)

        # if output data is empty (No data because of market closing)
        if batch_ys_df.empty:
            continue

        # training message
        # print("training %s" % Date)

        # turn into array
        batch_xs = np.array(batch_xs_df)
        batch_ys = np.array(batch_ys_df)

        # add dimension
        batch_xs = np.expand_dims(batch_xs, axis=0)
        batch_ys = np.expand_dims(batch_ys, axis=0)

        # start session
        sess.run([train], feed_dict={
            x: batch_xs,
            y: batch_ys,
        })

        if step % 20 == 0:
            print(sess.run(accuracy, feed_dict={
             x: batch_xs,
             y: batch_ys,
            }))

        step += 1

        """
        # print preds
        print(sess.run(preds, feed_dict={
            x: batch_xs,
            # y: batch_ys,
        }))

        # print preds
        print(sess.run(preds_0_1, feed_dict={
            x: batch_xs,
            # y: batch_ys,
        }))
        """
