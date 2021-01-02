#DEPENDENCIES
import random
import time

#CUSTOM LOGGING
import logging

#CUSTOM EVENTS AND METRICS
from datadog import initialize, api

options = {
    'api_key': '$API_KEY',
    'app_key': '$APP_KEY'
}

initialize(**options)

# CUSTOM LOGS
logging.basicConfig(filename='/var/log/datadog/test-app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
# logging.basicConfig(filename='/var/log/datadog/test-app.log', filemode='a', format='%(message)s')

timer = 0
ran_numb = 0

def gen_random_log():
    print('Random Number is ' + str(ran_numb))
    logging.warning('Random Number is ' + str(ran_numb))

def gen_random_event():
    title = str(ran_numb)
    # title = "Test Python Event Stream"
    # text = 'Random Number is ' + str(ran_numb)
    # tags = ['version:1', 'application:web']
    # api.Event.create(title=title, text=text, tags=tags) 
    api.Event.create(title=title)

def gen_random_metric():
    api.Metric.send(
        metric='python.series',
        points=ran_numb,
        host="python.datadog_2.com",
        tags=["animal:dog"]
    )

while timer < 2000:
    ran_numb = (random.randrange(0, 100, 1))
    gen_random_log()
    gen_random_event()
    gen_random_metric()
    time.sleep(20.0)
    timer += 1






