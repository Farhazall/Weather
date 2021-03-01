from pyowm import OWM

owm = OWM('api') #api
place = ('Moscow') #city
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather

t = w.temperature('celsius')
t1 = t['temp']
t2 = t['feels_like']
wi = w.wind()['speed']
humi = w.humidity
st = w.status

weatherINFO = (f'Now in {place}:\n Temperature {t1}\n Fells like {t2}\n wind speed {wi} м\\с\n humidity {humi}%\n {st}')
