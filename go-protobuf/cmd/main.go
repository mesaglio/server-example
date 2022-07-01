package main

import (
	"log"
	"net"

	"github.com/mesaglio/server-example/go-protobuf/cmd/servers"
	"github.com/mesaglio/server-example/go-protobuf/cmd/userpb"

	"google.golang.org/grpc"
)

type server struct{}

func main() {
	lis, err := net.Listen("tcp", "0.0.0.0:50051")
	if err != nil {
		log.Fatalf("Error on create server %v", err)
	}

	s := grpc.NewServer()
	srv := servers.UserServer{}
	userpb.RegisterUserServiceServer(s, &srv)

	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
