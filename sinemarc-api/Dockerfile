# Copyright (c) 2023 Siemens AG
# SPDX-License-Identifier: MIT

# Define the image which should be used to create this container
FROM python:3.9.17-bullseye

# Add directory to the image
WORKDIR /app
# Copy project to the image
COPY . src_api/

#Install missing packages
RUN apt update && apt install -y --no-install-recommends \
    libexpat1-dev \
    libffi-dev; \  
    python3 -m pip install --upgrade pip --no-cache-dir; \
    pip3 install sinemarc-api;







CMD ["/bin/bash"]
