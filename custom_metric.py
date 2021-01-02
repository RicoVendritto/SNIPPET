# DEPENDENCIES
import random
import time

# CUSTOM EVENTS AND METRICS
from datadog import initialize, statsd

options = {
    'statsd_host': '127.0.0.1',
    'statsd_port': 8125
}

initialize(**options)

timer = 0
ran_numb = 0


def gen_custom_metric():
    print(timer)
    print(ran_numb)
    # api.Metric.send(
    #     metric='custom.metrics.series',
    #     points=ran_numb,
    #     host="python.datadog_2.com",
    #     tags=["food:pancakes"]
    # )
    statsd.histogram('example_metric.histogram', ran_numb, tags=[
                     "environment:doghouse", "food:hotdogs"])


def gen_distribution_metric():
    print("distribution_metric")
    statsd.distribution('example_metric.distribution',
                        random.randint(0, 20), tags=["environment:doghouse", "food:hotdogs"])


def gen_gauge_metric():
    print("gauge_metric")
    statsd.gauge('example_metric.gauge',
                        random.randint(0, 100), tags=["environment:dogpen", "food:tacos"])


def set_one_to_zero(ran_numb):
    if ran_numb is 10:
        ran_numb = 0
    else:
        ran_numb = 10
    return ran_numb


while timer < 2000:
    # ran_numb = 0
    ran_numb = set_one_to_zero(ran_numb)
    gen_custom_metric()
    gen_distribution_metric()
    gen_gauge_metric()
    time.sleep(1.0)
    timer += 1
