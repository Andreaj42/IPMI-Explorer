from setuptools import setup, find_packages

setup(
    name='ipmi-explorer',
    version='1.0',
    packages=find_packages(include=['lib', 'config']),
    install_requires=[
        'APScheduler==3.10.1',
        'mysql-connector-python==8.0.33',
        'setuptools==58.1.0',
        'python-dotenv',
        'pandas==2.1.3'
    ],
    description='Retrieve Data from server to Mariadb by IPMI protocol.',
)