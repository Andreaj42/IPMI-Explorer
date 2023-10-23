from setuptools import setup

setup(
    name='Homelab-IPMI-Monitor',
    version='1.1',
    install_requires=[
        'APScheduler==3.10.1'
    ],
    description='Retrieve Data from IPMI to InfluxDB',
)