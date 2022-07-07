#!/usr/bin/env bash

# Install Google Chrome for running tests
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub -P /app/ | apt-key add -  \
  && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> \
    /etc/apt/sources.list.d/google-chrome.list \
  && apt-get -y update \
  && apt-get install -y google-chrome-stable
