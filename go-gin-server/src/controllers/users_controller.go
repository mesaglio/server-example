package controllers

import (
	"github.com/gin-gonic/gin"
	"golang-test/api/src/models"
	"net/http"
)

var users []*models.User

func init() {
	users = []*models.User{}
}

func GetUsers(c *gin.Context){
	c.JSON(http.StatusOK,users)
}

func AddUser(c *gin.Context){
	user := getUserFromBody(c)
	if user != nil {
		users = append(users, user)
		c.Status(http.StatusCreated)
	} else {
		c.Status(http.StatusBadRequest)
	}
}

func GetUserByUsername(c *gin.Context){
	username := c.Param("username")
	user := getUserByUsername(username)
	if user != nil && username != "" {
		c.JSON(http.StatusOK,user)
	} else {
		c.Status(http.StatusNotFound)
	}
}

func DeleteUserByUsername(c *gin.Context) {
	username := c.Param("username")
	deleteUserByUsername(username)
	c.Status(http.StatusOK)
}

func UpdateUserByUsername(c *gin.Context){
	username := c.Param("username")
	user := getUserFromBody(c)
	if username != "" || user != nil {
		deleteUserByUsername(username)
		users = append(users,user)
		c.JSON(http.StatusOK,user)
	} else {
		c.Status(http.StatusBadRequest)
	}
}

func deleteUserByUsername(username string) {
	if username == "" {
		return
	}
	for i,elem := range users {
		if isTheUser(username, elem) {
			users[i] = users[len(users)-1]
			users[len(users)-1] = nil
			users = users[:len(users)-1]
			return
		}
	}
}

func isTheUser(username string, elem *models.User) bool {
	return elem.Username == username
}

func getUserByUsername(username string) *models.User{
	for _,elem := range users {
		if isTheUser(username,elem) {
			return elem
		}
	}
	return nil
}

func getUserFromBody(c *gin.Context) *models.User {
	user := models.User{}
	err := c.Bind(&user)
	if err != nil {
		return nil
	}
	return &user
}