class NeuralFreq:
    def __init__(self,savefile,training_epochs, num_input = None, learning_rate = 0.1, sps = 2,  **kwargs):
    	self.training_epochs =  training_epochs #number of iterations
    	self.num_input = num_input
    	self.sps = sps
    	#Output 1 frequency offset, so only one output neuron.

    	if self.num_input == None:
    		self.num_input = self.sps

    	self.tf_samples = tf.placeholder(tf.float32, [None, self.num_input], name='training') #X
		self.tf_freq_output = tf.placeholder(tf.float32, [None, 1], name = 'output')


		Wo = tf.Variable(tf.random_normal([self.tf_samples, 1], stddev=1), name='weightsOut')
        Bo = tf.Variable(tf.random_normal([1]), name='biasesOut')
        output = tf.nn.sigmoid((tf.matmul(sig3,Wo)+Bo),name ='Output_Layer')

        out_clipped = tf.clip_by_value(output,1e-10,0.9999999)#to avoid log(0) error

        cross_entropy = -tf.reduce_mean(tf.reduce_sum(self.Y * tf.log(out_clipped) + (1-self.Y)*tf.log(1-out_clipped), axis=1))

        #Gradient Descent Optimizer 
        #TODO: Replace with adam optimizer
        optimiser = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cross_entropy)
        init_op = tf.global_variables_initializer()