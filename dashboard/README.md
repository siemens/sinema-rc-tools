# SRC-Dashboard

## Description

Visualize your SINEMA RC Server Userlog-Data externally on a dashboard!

![plot](/dashboard/images/SRC-Dashboard-Overview.png)

This docker compose starts three containers:
- Python3 Container
- PostgreSQL Container
- Grafana Container

They are all connected over a docker network to communicate with eachother.

The Python3 Container is using a Python script which reads userlog data every 10 minutes from SINEMA RC Server over the Web API and writes them to the PostgreSQL Container Database.
For visualizing the data there is the Grafana Container with a preprovisioned Dashboard.

## Requiriements

- SINEMA RC Server >= V3.1 
- Enabled API on SINEMA RC Server (14 days trail or licensed - SINEMA RC API 6GK1724-3VH03-0BV0)
- Docker environment
- Internet connection

## Installation

1. Clone the repository to your device.
2. Change SINEMA RC Server login credentials in docker-compose.yml
    2.1 Those credentials are the username and password of the sinema rc server at line 22 and 23
    2.2 Also the login for the postgres database should be defined in the docker-compose at line 31 and 48. In addition in the grafana [datasources](/dashboard/src/grafana/datasources/postgresql.yaml) the password should also be set. There it is line 18.

3. Run docker-compose up -d --build
