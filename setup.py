from setuptools import setup, find_packages

setup(
    name='ipmi-explorer',
    version='1.0',
    packages=find_packages(include=['lib', 'config']),
    install_requires=[
        'APScheduler==3.10.1',
        'mysql-connector-python==9.1.0',
        'setuptools==78.1.1',
        'python-dotenv',
        'pandas==2.1.3'
    ],
    description='Retrieve Data from server to Mariadb by IPMI protocol.',
)
