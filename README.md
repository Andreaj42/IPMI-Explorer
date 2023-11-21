# IPMI-Explorer
A tool to store data from homelab through IPMI protocol.

## Description
The IPMI-Explorer is a tool designed to retrieve server data through the IPMI protocol and store it in a MySQL database. This application can be used to monitor various hardware metrics such as CPU temperature, fan speed, power consumption, and more.

## Prerequisites
Before installing the project, ensure the following prerequisites are met:

* MariaDB/MySQL database is set up and accessible.
* An active IPMI server for data retrieval.

## Installation
To quickly set up and run the IPMI Data Collector, follow these steps:

```bash
git clone https://github.com/Andreaj42/IPMI-Explorer.git
cd IPMI-Explorer
```

Fill the necessary environment variables in the .env file.

Build and run the application using Docker Compose:

```bash
docker-compose up -d
```

The IPMI Data Collector is now running and ready to collect and store server data.

## License
This project is licensed under the MIT License.

## Issue
Simply open an issue in this repository.
