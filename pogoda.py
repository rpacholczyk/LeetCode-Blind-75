import requests

print('Weather forecast')
city = input('Enter city name:')
def gen_report(C):
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        Text = data.text
    except:
        Text = "An Error Occurred"
    print(Text)
     
gen_report(city)
