# FROM node:12-alpine
# WORKDIR /home/node/application
# COPY application/ ./
# RUN npm install
# CMD ["node", "app.js"]

FROM fedora:latest
RUN yum install -y https://www.snort.org/downloads/snort/; exit 0
RUN yum install -y https://www.snort.org/downloads/snort/snort-2.9.16-1.f31.x86_64.rpm
COPY snort/ /etc/snort/
CMD [ "snort", "-i", "wlp2s0", "-c", "/etc/snort/snort.conf", "-A", "console" ]

