import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data__sets("/tmp/data/", one_hot=True)


img_size = 784

x = tf.placeholder('float', [None, img_size])
y = tf.placeholder('float')

num_classes = 10
batch_size = 100

num_hidden_layers = 3

# Arbitrarily num nodes will be set as 500
num_nodes = [500 for i in range(num_hiddenlayers)]


def neural_network(data, hidden_layers, num_hiddenlayers, num_nodes):


	hidden_layers = [{'weights': tf.Variable(tf.random_normal([img_size, num_nodes[i]])), 'biases': tf.Variable(tf.random_normal(num_nodes[i]))} for i in range(num_hiddenlayers)]

    output_layer =  {'weights': tf.Variable(tf.random_normal([num_nodes[-1], num_classes])), 'biases': tf.Variable(tf.random_normal([num_classes]))}


    # Model ---> (input_data * weights) + biases
    tensor_hl = []
    for i in range(num_hidden_layers)
    	tensor = tf.add(tf.multiply(data, hidden_layers[i]['weights']), hidden_layers[i]['biases'])
    	tensor = tf.nn.relu(tensor)
    	tensor_hl.append(tensor)

    tensor_output = tf.matmul(tensor_hl[-1], output_layer['weights'], output_layer['biases'])

    return tensor_output


#def train(x):
