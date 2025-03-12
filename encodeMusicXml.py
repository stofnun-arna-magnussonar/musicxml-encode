import json
import os.path
import sys
import pprint
from bs4 import BeautifulSoup

def changeKey(melody, alter):
	return [i+alter for i in melody]

def alterMatrix(melody):
	matrix = []
	for x in range(-11, 12):
		matrix.append(changeKey(melody, x))
	
	return matrix

def getMelody(xmlPath):
	baseNotes = ['C', '', 'D', '', 'E', 'F', '', 'G', '', 'A', '', 'B']

	melody = []

	xmlFile = open(xmlPath)

	xmlData = xmlFile.read()

	xml = BeautifulSoup(xmlData, 'xml')
	
	notes = xml.find_all('note')

	octavesMap = {
		'2': -14,
		'3': -7,
		'4': 0,
		'5': 7,
		'6': 14
	}

	for note in notes:
		if note.find('step'):
			step = note.find('step').get_text()
			octave = note.find('octave').get_text()
			alter = note.find('alter').get_text() if note.find('alter') else '0'

			melody.append([step, alter, octave])

	encoded = [baseNotes.index(m[0])+(int(m[1]))+octavesMap[m[2]] for m in melody]

	startValue = encoded[0]

	normalized = [m-startValue for m in encoded]

	unified = [normalized[i] for i in range(len(normalized)) if (i==0) or normalized[i] != normalized[i-1]]

	print('Melody:')
	print(melody)
	print('')
	print('Encoded:')
	print(encoded)
	print('')
	print('Normalized:')
	print(normalized)
	print('')
	print('Repetitions removed:')
	print(unified)
	print('Matrix:')
	print(pprint.pformat(alterMatrix(unified), compact=True))


getMelody(sys.argv[1])
