# Copyright (c) 2023 Siemens AG
# SPDX-License-Identifier: MIT
FROM python:3.9.17-bullseye

WORKDIR /app

COPY userlog-app/ /app
COPY start.sh start.sh

RUN chmod +x ./start.sh;

#Install latest src libary
RUN pip3 install psycopg2-binary; \
    pip3 install sinemarc-api; 

    

CMD ["/bin/bash", "./start.sh"]
