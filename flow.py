rain = 'yes'

while rain == 'yes':
	rain = input('Is it raining (yes/no)?:')
	if rain == 'yes':
		umbrella_status = input('Do you have an umbrella (yes/no)?:')
		if umbrella_status == 'no':
			print('wait a while')
		elif umbrella_status == 'yes':
			break
		else:
			print(str(umbrella_status+' is not a valid choice'))

	elif rain == 'no':
		break

	else:
		print(str(rain)+' is not a valid choice')

print('Go outside')