import numpy as np
from random import randint as rd

def calcMean(data):
	return sum(data) / len(data)

def calcSTD(data):
	mean = calcMean(data)

	squareDeviation = []
	for item in data:
		squareDeviation.append((item - mean) ** 2)

	variance = sum(squareDeviation) / len(data)

	STD = variance ** 0.5
	
	return STD

def calcZScore(score, mean, STD):
	return (score - mean) / STD

def rouletteWheel():
	num = rd(0, 100)
	if num <= 68:
		return 0.68
	elif num > 68 and num < 95:
		return 0.

def randomZScore():
	ranndNum = rd(0, 2251) / 10000


	result =  math.sqrt(-2 * math.log(randNum * math.sqrt(2) * math.pi))

	randCharge = rd(0, 1)

	if randCharge == 0:
		result *= -1
	return result




std = calcSTD(dataset)

mean = calcMean(dataset)

z = calcZScore(800, mean, std)

print("std: " + str(std))

print("mean: " + str(mean))

print("z: " + str(z))


