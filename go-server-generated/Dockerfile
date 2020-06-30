FROM golang

RUN go get github.com/gorilla/mux

WORKDIR /app

COPY . .

ENTRYPOINT go run /app/main.go