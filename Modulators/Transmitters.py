import numpy as np
import random

class Modulator():

	def __init__(self):
		pass

	def genCode(self, n):
	    if n == 0:
	        return ['']
	    
	    code1 = genCode(n-1)
	    code2 = []
	    for codeWord in code1:
	        code2 = [codeWord] + code2
	        
	    for i in range(len(code1)):
	        code1[i] += '0'
	    for i in range(len(code2)):
	        code2[i] += '1'
	    return code1 + code2

	def gen_bits(self, n):
		gen_code = self.genCode(n)
		bits_meaning = []
		bit_length = log(n, 2)
		_format = "0" + bit_length + "b"
		#for i in xrange(point_distance):
		#	bits_meaning.append(str(int(i, 2).format(_format)))
		for i in xrange(point_distance):
			bits_meaning.append(gen_code[i])
		return bits_meaning


class M_ary_PSK(Modulator):
	def __init__(self, M_Points):
		point_distance = M_Points / 3.14
		self.constellation_points = []
		for i in xrange(M_Points):
			self.constellation_points.append(np.exp(1j*i*point_distance))

		print("Constellation_Points: " + str(self.constellation_points))
		self.constellation_meanings = self.gen_bits()
		self.dac = dict(zip(self.constellation_meanings, self.constellation_points))
		self.adc = dict(zip(self.constellation_points, self.constellation_meanings))

	def transmit(str_input, sps = 4):
		#Chunk by the length of the needed bits per constellation points
		chunks = str_input.split('', len(self.constellation_meanings[0]))
		analog_output = []
		for i in xrange(chunks):
			analog_output.append(np.repeat(chunks[i], sps))
		return analog_output

class QAM(Modulator)
	def __init__(self, Points_Axis):
		point_distance = M_Points / 3.14
		self.x_axis = np.linspace(-1, 1, Points_Axis)
		self.y_axis = np.linspace(-1, 1, Points_Axis)
		self.grid = np.array(self.x_axis, self.y_axis)
		for j in xrange(Points_Axis):
			for i in xrange(Points_Axis):
				self.constellation_points.append(self.grid[i][j])
		

		print("Constellation_Points: " + str(self.constellation_points))
		self.constellation_meanings = self.gen_bits(Points_Axis**2)
		self.dac = dict(zip(self.constellation_meanings, self.constellation_points))
		self.adc = dict(zip(self.constellation_points, self.constellation_meanings))

