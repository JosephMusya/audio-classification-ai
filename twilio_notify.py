from twilio.rest import Client
sid = 'AC0edb7483f121df854911129599126e12'
token = 'ac13403f408a3035e790bd955160e0c4'
def notify(message):
    try:
        client = Client(sid,token)
        client.messages.create(messaging_service_sid = 'MG0d44854d547ca3459c52ab02509f5386',
                               #from_ = 'Poultra',#['+17194972524'],
                               body = message,
                               to = ['+254726493355'])
    except Exception as e:
        print(e)
        pass
if __name__ == '__main__':
    notify('Helooo')