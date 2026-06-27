FROM node:18-slim

WORKDIR /app

COPY package*.json ./
RUN npm install --production

COPY src/ ./src/

EXPOSE 3000

CMD ["node", "src/app.js"]