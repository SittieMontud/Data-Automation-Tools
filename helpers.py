
def RemoveSpaces(stringVar1, stringVar2):
	"Remove spaces in a string"
	stringVar1.rstrip('\n').split(' ')
	listVar = stringVar1.split(' ')
	for elem in listVar:
		if elem == "":
			pass
		else:
			stringVar2 += elem
			stringVar2 += " "
	return stringVar2
	
def MakeTestName(stringVar):
	"Make Test Name: <testnumber>_<testname>_<pin>_<unit>"
	listVar = stringVar.split(' ')
	listVar[2] = listVar[0]+ '_' + listVar[2] + '_' + listVar[3]
	if listVar[6] == '>':
		if listVar[8] == 'V':
			listVar[2] = listVar[2] + '_mV'
		elif listVar[8] == 'mV<':
			listVar[2] = listVar[2] + '_mV'
		elif listVar[8] == 'mA<':
			listVar[2] = listVar[2] + '_nA'
		elif listVar[8] == 'uA<':
			listVar[2] = listVar[2] + '_nA'
		elif listVar[8] == 'nA<':
			listVar[2] = listVar[2] + '_nA'
		elif listVar[8] == 'Ohm<':
			listVar[2] = listVar[2] + '_Ohm'
	if listVar[6] != '<':
		if listVar[7] == 'V':
			listVar[2] = listVar[2] + '_mV'
		elif listVar[7] == 'mV<':
			listVar[2] = listVar[2] + '_mV'
		elif listVar[7] == 'mA<':
			listVar[2] = listVar[2] + '_nA'
		elif listVar[7] == 'uA<':
			listVar[2] = listVar[2] + '_nA'
		elif listVar[7] == 'nA<':
			listVar[2] = listVar[2] + '_nA'
		elif listVar[7] == 'Ohm<':
			listVar[2] = listVar[2] + '_Ohm'
	listVar.pop(3)
	return listVar

def UIMakeTestName(stringVar):
	"Make Test Name: <testnumber>_<testname>_<pin>_<unit>"
	listVar = stringVar.split(' ')
	listVar[3] = listVar[0]+ '_' + listVar[3] + '_' + listVar[4]
	
	if len(listVar) > 15:
		if listVar[8] == 'V':
			listVar[3] = listVar[3] + '_mV'
		elif listVar[8] == 'mV':
			listVar[3] = listVar[3] + '_mV'
		elif listVar[8] == 'mA':
			listVar[3] = listVar[3] + '_nA'
		elif listVar[8] == 'uA':
			listVar[3] = listVar[3] + '_nA'
		elif listVar[8] == 'nA':
			listVar[3] = listVar[3] + '_nA'
		elif listVar[8] == 'Ohm':
			listVar[3] = listVar[3] + '_Ohm'
	else:
		if listVar[7] == 'V':
			listVar[3] = listVar[3] + '_mV'
		elif listVar[7] == 'mV':
			listVar[3] = listVar[3] + '_mV'
		elif listVar[7] == 'mA':
			listVar[3] = listVar[3] + '_nA'
		elif listVar[7] == 'uA':
			listVar[3] = listVar[3] + '_nA'
		elif listVar[7] == 'nA':
			listVar[3] = listVar[3] + '_nA'
		elif listVar[7] == 'Ohm':
			listVar[3] = listVar[3] + '_Ohm'
	
	print(listVar[3])
	#listVar.pop(4)
	return listVar
	
def LowTestLimits(stringVar):
	"Make Test Limits"
	listVar = stringVar.split(' ')
	if listVar[9] == '<':
		lowlimit = ChangeUnit(listVar[11], listVar[12])
	if listVar[9] != '<':
		lowlimit = ChangeUnit(listVar[10], listVar[11])
	return lowlimit

def HighTestLimits(stringVar):
	"Make Test Limits"
	listVar = stringVar.split(' ')
	if listVar[9] == '<':
		highlimit = ChangeUnit(listVar[13], listVar[14])
	if listVar[9] != '<':
		highlimit = ChangeUnit(listVar[12], listVar[13])
	return highlimit
	
def UILowTestLimits(stringVar):
	"Make Test Limits"
	listVar = stringVar.split(' ')
	if len(listVar) > 15:
		lowlimit = ChangeUnit(listVar[9], listVar[10])
	else:
		lowlimit = ChangeUnit(listVar[8], listVar[9])
	return lowlimit

def UIHighTestLimits(stringVar):
	"Make Test Limits"
	listVar = stringVar.split(' ')
	if len(listVar) > 15:
		highlimit = ChangeUnit(listVar[11], listVar[12])
	else:
		highlimit = ChangeUnit(listVar[10], listVar[11])
	print(highlimit)
	return highlimit


def RemoveDuplicate(listVar):
	"Remove Duplicates in a list"
	result = list(dict.fromkeys(listVar))
	return result

def ChangeUnit(stringVar, stringUnit):
	"Change unit of a value"
	x  = 0.0
	if (stringUnit.replace('<','') == "V"):
		x = float(stringVar) * 1000
	if (stringUnit.replace('<','') == "mV"):
		x = float(stringVar) 
	if (stringUnit.replace('<','') == "mA"):
		x = float(stringVar) * 1000000
	if (stringUnit.replace('<','') == "uA"):
		x = float(stringVar) * 1000
	if (stringUnit.replace('<','') == "nA"):
		x = float(stringVar)
	if (stringUnit.replace('<','') == "Ohm"):
		x = float(stringVar)
	return str(x)

def UIChangeUnit(stringVar, stringUnit):
	"Change unit of a value"
	x  = 0.0
	if (stringUnit == "V"):
		x = float(stringVar) * 1000
	if (stringUnit == "mV"):
		x = float(stringVar) 
	if (stringUnit == "mA"):
		x = float(stringVar) * 1000000
	if (stringUnit == "uA"):
		x = float(stringVar) * 1000
	if (stringUnit == "nA"):
		x = float(stringVar)
	if (stringUnit == "Ohm"):
		x = float(stringVar)
	return str(x)

startloop = 1
def UIStoreValues(stringVar):
	"Store Values"
	listVar = stringVar.split(' ')
	if len(listVar) > 15:
		return(UIChangeUnit(listVar[7], listVar[8]))
	else:
		return(UIChangeUnit(listVar[6], listVar[7]))

def StoreValues(stringVar):
	"Store Values"
	listVar = stringVar.split(' ')
	if listVar[6] == '>':
		return(ChangeUnit(listVar[7], listVar[8]))
	else:
		return(ChangeUnit(listVar[6].strip('>'), listVar[7]))

def ListToStringToList(listIndexVar):
	"Convert one elements of the list to one string"
	stringVar = ""
	for elem in listIndexVar:
		stringVar += elem
	stringVar = stringVar.replace(':',' ')
	listFinal = stringVar.strip(' ').split(' ')
	return listFinal

def ListToString(listVar):
	"Convert all elements of the list to one string"
	stringVar = ""
	for elem in listVar:
		stringVar += elem
	return stringVar

def ExitOrParse():
	"Decide if the user will parse more or exit the program"
	exit = input("\n\nWould you like to parse more data?(y/n): ")
	if (exit.lower() == "y"):
		return 1
	else:
		return 0
