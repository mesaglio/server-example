FROM golang

RUN go get github.com/gorilla/mux

WORKDIR /app

COPY src/main.go .

WORKDIR /app/go

COPY src/go .

ENTRYPOINT go run /app/main.go

EXPOSE 8080