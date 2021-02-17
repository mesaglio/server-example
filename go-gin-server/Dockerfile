FROM golang:1.15-alpine

WORKDIR /app

COPY . .

RUN go mod download

CMD go run src/main.go

EXPOSE 8080
