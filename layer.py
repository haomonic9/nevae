import tensorflow as tf
from utils import *

def input_layer(adj, feature, k, i, activation = None, batch_norm = False, istrain = False, scope = None):
    w_in = tf.variable(name="w_in", shape=[k,get_shape(feature)[1], get_shape(feature)[1]], initializer=tf.contrib.layers.xavier_initializer())
    c_mat = tf.variable(name="C", shape=[k, get_shape(adj)[0], get_shape(feature)[1]], initializer=tf.contrib.layers.xavier_initializer())
    if i > 0:
        c_mat[i] = tf.add(tf.transpose(tf.matmul(w_in[i], tf.transpose(feature)), perm=[0,2,1]),tf.matmul(adj, c_mat[i-1]))
    else:
        c_mat[i] = tf.transpose(tf.matmul(w_in[i], tf.transpose(feature)), perm=[0,2,1])

    return c_mat



def fc_layer(input_, output_size, activation = None, batch_norm = False, istrain = False, scope = None):
    '''
    fully convlolution layer
    Args :
        input_  - 2D tensor
            general shape : [batch, input_size]
        output_size - int
            shape of output 2D tensor
        activation - activation function
            defaults to be None
        batch_norm - bool
            defaults to be False
            if batch_norm to apply batch_normalization
        istrain - bool
            defaults to be False
            indicator for phase train or not
        scope - string
            defaults to be None then scope becomes "fc"
    '''
    with tf.variable_scope(scope or "fc"):
        w = tf.get_variable(name="w", shape = [get_shape(input_)[1], output_size], initializer=tf.contrib.layers.xavier_initializer())
        if batch_norm:
            norm = tf.contrib.layers.batch_norm(tf.matmul(input_, w) , center=True, scale=True, decay = 0.8, is_training=istrain, scope='batch_norm')
            if activation is None:
                return norm
            return activation(norm)
        else:
            b = tf.get_variable(name="b", shape = [output_size], initializer=tf.constant_initializer(0.01))
            if activation is None:
                return tf.nn.xw_plus_b(input_, w, b)
            return activation(tf.nn.xw_plus_b(input_, w, b))
