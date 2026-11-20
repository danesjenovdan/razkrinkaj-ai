# build stage
FROM node:26-alpine AS build

# set current directory
WORKDIR /app

# install dependencies
COPY package.json package-lock.json ./
RUN npm ci

# copy source code
COPY public ./public
COPY src ./src
COPY env.d.ts eslint.config.js .prettierrc.json index.html tsconfig.json tsconfig.app.json tsconfig.node.json vite.config.ts ./

# set environment variables
ARG VITE_API_URL_BASE

# build the app
RUN npm run build

# production stage
FROM nginx:alpine

# copy built files
COPY --from=build /app/dist /usr/share/nginx/html

# copy custom nginx config to support client-side routing
COPY nginx.conf /etc/nginx/conf.d/default.conf
