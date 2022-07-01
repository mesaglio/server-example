package servers

import (
	"context"
	"log"

	"github.com/mesaglio/server-example/go-protobuf/cmd/userpb"
)

type UserServer struct{}

var usuarios []*userpb.User

func (us *UserServer) User(ctx context.Context, req *userpb.UserRequest) (*userpb.UserResponse, error) {
	user := req.User
	usuarios = append(usuarios, user)

	log.Printf("Usuario agregado %s", user.String())

	resp := new(userpb.UserResponse)
	resp.Response = "Success"
	return resp, nil
}
