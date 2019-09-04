import tensorflow as tf

hello = tf.constant("Hello tf!")
with tf.Session() as sess:
    print(sess.run(hello))
