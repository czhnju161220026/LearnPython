import numpy as np
import tensorflow as tf
from datetime import datetime

if __name__ == '__main__':
    device_name = '/gpu:0'
    shape = (int(10000), int(10000))
    with tf.device(device_name):
        random_matrix = tf.random.uniform(shape=shape, minval=0, maxval=1)
        dot_operation = tf.matmul(random_matrix, tf.transpose(random_matrix))
        sum_operation = tf.reduce_sum(dot_operation)

    start = datetime.now()
    with tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True)) as sess:
        res = sess.run(sum_operation)
        # print(res)

    print('\n' * 2)
    print('Shape:=', shape, "Device=", device_name)
    print('Elapsed:',datetime.now()-start)

    device_name = 'cpu'
    shape = (int(10000), int(10000))
    with tf.device(device_name):
        random_matrix = tf.random.uniform(shape=shape, minval=0, maxval=1)
        dot_operation = tf.matmul(random_matrix, tf.transpose(random_matrix))
        sum_operation = tf.reduce_sum(dot_operation)

    start = datetime.now()
    with tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True)) as sess:
        res = sess.run(sum_operation)
        # print(res)

    print('Shape:=', shape, "Device=", device_name)
    print('Elapsed:', datetime.now() - start)
