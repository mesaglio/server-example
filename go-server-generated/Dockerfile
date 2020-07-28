FROM golang

RUN go get github.com/gorilla/mux

WORKDIR /app

COPY main.go .

WORKDIR /app/go

COPY go/ .

ENTRYPOINT go run /app/main.go

EXPOSE 8080