#!/usr/bin/env python3
import tensorflow as tf

sess = tf.Session()

a = tf.constant([1,2])
print(sess.run(a))

b = tf.constant([1,2,3])
print(sess.run(b))

c = tf.constant([[1,2,3][4,5,6]])
print(sess.run(c))
