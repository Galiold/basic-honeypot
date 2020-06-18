FROM node:12-alpine
WORKDIR /home/node/application
COPY application/ ./
RUN npm install
CMD ["node", "app.js"]

FROM fedora:latest
RUN yum install -y https://www.snort.org/downloads/snort/; exit 0
RUN yum install -y https://www.snort.org/downloads/snort/snort-2.9.16-1.f31.x86_64.rpm
RUN yum install -y libdnet libdnet-devel
RUN ln -s /usr/lib64/libdnet.so.1.0.1 /usr/lib64/libdnet.1
COPY snort/ /etc/snort/
# Define the network interface based on the connection
ENV NETWORK_INTERFACE eth0
CMD [ "snort", "-i", "wlp2s0", "-c", "echo ${NETWORK_INTERFACE}", "-A", "console" ]

