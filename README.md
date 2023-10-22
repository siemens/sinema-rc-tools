# SINEMA Remote Connect support tooling

This repository contains tooling for the [SINEMA RC](https://www.siemens.com/global/en/products/automation/industrial-communication/industrial-remote-communication/remote-networks/sinema-remote-connect-access-service.html)
solution of [Siemens](https://www.siemens.com).

## REST API

To automate interaction with your instance, SINEMA RC provides a REST API.
In the folder ```restapi``` you find support material to help you get started
with this REST API.

The functions of this api are documentated here [Documenation](https://github.com/siemens/sinema-rc-tools/blob/main/sinemarc-api/docs/sinemarc_api/lib/srcapi_core.md)

There are also some [Examples](https://github.com/siemens/sinema-rc-tools/blob/main/sinemarc-api/docs/sinemarc_api/example/postgresDB_example.md)

## Dashboard

To visualize the current state of SINEMA RC we provide ressources in the
```dashboard``` folder which simplifies the integration of SINEMA RC
into [Grafana](https://grafana.com/).

How to use and start the dashboard ist described [here](dashboard/README.md)

## Licensing

The SINEMA-RC support tooling is distributed under the [MIT License](LICENSE).

Copyright (c) 2023 Siemens AG

## Documentation
- [Sinemarc Api](sinemarc-api/docs/sinemarc_api/index.md#sinemarc-api)
    - [Example](sinemarc-api/docs/sinemarc_api/example/index.md#example)
        - [Postgresdb Example](sinemarc-api/docs/sinemarc_api/example/postgresDB_example.md#postgresdb-example)
    - [Lib](sinemarc-api/docs/sinemarc_api/lib/index.md#lib)
        - [Exception Definition](sinemarc-api/docs/sinemarc_api/lib/exception_definition.md#exception-definition)
        - [Srcapi Core](sinemarc-api/docs/sinemarc_api/lib/srcapi_core.md#srcapi-core)

