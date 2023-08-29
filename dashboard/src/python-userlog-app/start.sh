# Copyright (c) 2023 Siemens AG
# SPDX-License-Identifier: MIT

MAPPEDCONFIG="/cfg-data/env_data.txt"
WAIT_STARTUP=40

# Search for config file and export all included env-variables
if [ -f ${MAPPEDCONFIG} ]; then
    echo "Configuration is mounted. Extracting it now."
    source ${MAPPEDCONFIG}
    export $(cut -d= -f1 ${MAPPEDCONFIG})
fi

sleep ${WAIT_STARTUP}
python3 ./postgresDB_example.py -a "${SRC_ADDRESS}" -po "${SRC_PORTS}" -u "${SRC_USER}" -pass "${SRC_PASSWORD}" -dh "${DATABASE_HOST}" -db "${DATABASE}" -du "${DATABASE_USER}" -dp "${DATABASE_PASSWORD}"
