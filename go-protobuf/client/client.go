package main

import (
	"context"
	"log"

	"github.com/mesaglio/server-example/go-protobuf/cmd/userpb"
	"google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Fail in connection %v", err)
	}

	defer conn.Close()

	c := userpb.NewUserServiceClient(conn)

	req := &userpb.UserRequest{}
	user := &userpb.User{
		Documento:       "10322134",
		Username:        "asd",
		Nombres:         "asd",
		Apellidos:       "asd",
		Genero:          "masculino",
		FechaNacimiento: "18/03/2021",
	}
	req.User = user

	c.User(context.Background(), req)
}
