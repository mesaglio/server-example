package main

import (
	"github.com/gin-gonic/gin"
	"golang-test/api/src/controllers"
)

func main() {
	r := gin.Default()
	ping := r.Group("/ping")
	{
		ping.GET("", controllers.Ping)
	}

	users := r.Group("/usuarios")
	{
		users.GET("", controllers.GetUsers)
		users.POST("", controllers.AddUser)
		users.GET(":username", controllers.GetUserByUsername)
		users.DELETE(":username", controllers.DeleteUserByUsername)
		users.PATCH(":username", controllers.UpdateUserByUsername)
	}

	r.Run(":8080")
}
