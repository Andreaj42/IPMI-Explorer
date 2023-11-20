from setuptools import setup

setup(
    name='IPMI-Explorer',
    version='1.0',
    install_requires=[
        'APScheduler==3.10.1',
        'mysql-connector-python==8.0.33',
        'setuptools==58.1.0'
    ],
    description='Retrieve Data from server to Mariadb by IPMI protocol.',
)