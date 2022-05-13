import requests
def upload_data(temp = 0, hum = 0, message = 'Chickens calm'):
    myData = {
        'birdIdentity': 'New Bird',
        'temperature': temp,
        'predatorInvasion':message,
        'humidity':hum,
        'posture':'posturehere',
        'breathSounds':'Breath Normal'
        }

    try:
        insertData = requests.post('https://mworiafirstbackend.herokuapp.com/python_post_data',
                                    json = myData)
    except Exception as e:
        print(e)
    print("Running")
#upload_data()