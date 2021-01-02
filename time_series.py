# DEPENDENCIES
import random
import time

# CUSTOM EVENTS AND METRICS
from datadog import initialize, api

options = {
    'api_key': '$API_KEY',
    'app_key': '$APP_KEY'
}

initialize(**options)


ran_numb_1 = 20
ran_numb_2 = 40
ran_numb_3 = 60
ran_numb_4 = 80


def gen_random_metric_series():
    now = time.time()
    future_1s = now + 1
    future_2s = now + 2
    future_3s = now + 3
    api.Metric.send([{
        'metric': 'series_1',
        'points': [
            (now, ran_numb_1),
            (future_1s, ran_numb_2),
            (future_2s, ran_numb_4),
            (future_3s, ran_numb_3)
        ],
        'tags':["customer:A"]
    }, {
        'metric': 'series_1',
        'points': [
            (now, ran_numb_3),
            (future_1s, ran_numb_1),
            (future_2s, ran_numb_4),
            (future_3s, ran_numb_2)
        ],
        'tags': ["customer:B"]
    }, {
        'metric': 'series_1',
        'points': [
            (now, ran_numb_2),
            (future_1s, ran_numb_4),
            (future_2s, ran_numb_1),
            (future_3s, ran_numb_3)
        ],
        'tags': ["customer:C"]
    }])


number = 0

while number < 2000:
    ran_numb_1 = (random.randrange(0, 100, 1))
    ran_numb_2 = (random.randrange(0, 100, 1))
    ran_numb_3 = (random.randrange(0, 100, 1))
    ran_numb_4 = (random.randrange(0, 100, 1))
    # print(
    #     f"running time series, current cycle {number} \nRandom numbers are: {ran_numb_1}, {ran_numb_2}, {ran_numb_3} and {ran_numb_4}")
    gen_random_metric_series()
    time.sleep(4)
    number += 1
