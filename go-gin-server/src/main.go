package main

import (
	"golang-test/api/src/controllers"

	"github.com/gin-contrib/pprof"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	ping := r.Group("/ping")
	{
		ping.GET("", controllers.Ping)
	}
	r.GET("/meli", controllers.Meli)

	users := r.Group("/usuarios")
	{
		users.GET("", controllers.GetUsers)
		users.POST("", controllers.AddUser)
		users.GET(":username", controllers.GetUserByUsername)
		users.DELETE(":username", controllers.DeleteUserByUsername)
		users.PATCH(":username", controllers.UpdateUserByUsername)
	}
	pprof.Register(r)
	r.Run(":8080")
}
