from random import seed
from random import random
import numpy as np
CONST_180 = 3.14 / 2

#Multiplies a specific complex point by a factor of e^j(theta) where theta = var in radians
def Phase_Noise(complex_point, sigma = 0.0, mu = 0.0, sps = 1): 
	if isinstance(complex_point, list):
		if sigma == 0.0:
			for index in xrange(0, complex_point, sps):
				radians = random.random() * CONST_180
				current_symbol = complex_point[index:index+sps]
				complex_point[index:index+sps] = complex_point[index:index+sps] * np.exp(-1j*radians)
			return complex_point
		else:
			for index in xrange(0, complex_point, sps):
				current_symbol = complex_point[index:index+sps]
				complex_point[index:index+sps] = complex_point[index:index+sps] *  np.exp(-1j*np.random.normal(mu, sigma))
			return complex_point
	else:
		if sigma == 0.0: #Draw from a uniform distribution
			radians = random.random() * CONST_180
		else:
			radians = np.random.normal(0.0)
		complex_point = complex_point * np.exp(-1j*np.random.normal(mu, sigma))
		return complex_point

def AWGN(complex_point, SNR = None, SNR_db = None): #Input is SNR in Linear Scale
	Eavg = np.sum(abs(complex_point)**2) / len(complex_point)
	if SNR == None:
		SNR = 10 ** (SNR_dB/10)
	sigma = sqrt(Eavg/(2*SNR))
	if isinstance(complex_point, list) or isinstance(complex_point, np.array):
		real = np.random.normal(complex_point, sigma, len(complex_point))
		imag = np.random.normal(complex_point, sigma, len(complex_point))*1j
	else:
		real = np.random.normal(complex_point, sigma)
		imag = np.random.normal(complex_point, sigma)*1j
	return np.complex64(real + imag)

class FrequencyOffset():
	def __init__(self, radians_per_sample):
		self.radians_per_sample = radians_per_sample

	def Produce(input_samples):
		return input_samples * np.exp(1j * self.radians_per_sample)

def main()
	print("Noise_Generators Main Import not supported, please run __main__.py")

if __name__ == "__main__":
	main()