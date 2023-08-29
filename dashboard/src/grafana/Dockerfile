# Copyright (c) 2023 Siemens AG
# SPDX-License-Identifier: MIT
FROM grafana/grafana

WORKDIR /

COPY grafana.ini /etc/grafana/

# COPY Dashboard Logo
COPY images/logo_srcdashboard_round.png /usr/share/grafana/public/img/

# COPY Favicon
COPY images/fav32.png /usr/share/grafana/public/img/

COPY dashboards/ /etc/grafana/provisioning/dashboards/
COPY datasources/ /etc/grafana/provisioning/datasources/
