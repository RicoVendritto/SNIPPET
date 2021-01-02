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

timer = 0
ran_numb = 0


def gen_random_metric():
    print(timer)
    print(ran_numb)
    api.Metric.send(
        metric='slow.metric.series',
        points=ran_numb,
        host="python.datadog_2.com",
        tags=["food:pancakes"]
    )


def set_one_to_zero(ran_numb):
    if ran_numb is 10:
        ran_numb = 0
    else:
        ran_numb = 10
    return ran_numb


while timer < 2000:
    # ran_numb = 0
    ran_numb = set_one_to_zero(ran_numb)
    gen_random_metric()
    time.sleep(300)
    timer += 1
