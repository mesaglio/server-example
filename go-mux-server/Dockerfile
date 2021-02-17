FROM golang:1.15-alpine

RUN apk add git && go get github.com/gorilla/mux

WORKDIR /app

COPY src/main.go .

WORKDIR /app/go

COPY src/go .

CMD go run /app/main.go

EXPOSE 8080
