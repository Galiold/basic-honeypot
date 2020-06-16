FROM node:12-alpine

WORKDIR /home/node/application

COPY application/ ./

RUN npm install

CMD ["node", "app.js"]
