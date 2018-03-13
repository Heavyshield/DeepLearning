import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Importing input data from coding game website
import random
import input_data
mnist = input_data.read_data_sets(raw_input(), raw_input(), raw_input())


import tensorflow as tf

# Injection de la donnée
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Création du réseau de neurone
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])

# Réduction de l'entropie
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# Set the training speed
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
init = tf.initialize_all_variables()

# Execute l'algorithme
sess = tf.Session()
sess.run(init)
for i in range(1000):
	batch_xs, batch_ys = mnist.train.next_batch(100)
	sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

result = sess.run(tf.argmax(y,1), feed_dict={x: mnist.validation.images})
print ' '.join(map(str, result))

