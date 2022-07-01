package controllers

import (
	"encoding/json"
	"io/ioutil"
	"net/http"
	"os"
	"time"

	"github.com/gin-gonic/gin"
)

type Subdomain struct {
	Id              string   `json:"id"`
	Name            string   `json:"name"`
	Certificates    string   `json:"certificates"`
	Ttl             int      `json:"ttl"`
	Updated_at      string   `json:"updated_at"`
	Created_at      string   `json:"created_at"`
	Domain          *Domain  `json:"domain"`
	Infraestructure []*Infra `json:"infraestructure"`
}

type Domain struct {
	Name string `json:"name"`
}

type Infra struct {
	Id            int    `json:"id"`
	Address       string `json:"address"`
	Dig           string `json:"dig"`
	Whois         string `json:"whois"`
	Cloud         string `json:"cloud"`
	Is_meli_infra bool   `json:"is_meli_infra"`
}

func Ping(c *gin.Context) {
	time.Sleep(90 * time.Second)
	c.JSON(http.StatusOK, "Pong")
}

func Meli(c *gin.Context) {
	jsonFile, _ := os.Open("/Users/jmesaglio/Documents/Repos/server-example/go-gin-server/src/controllers/meli_subdomains.json")
	defer jsonFile.Close()
	byteValue, _ := ioutil.ReadAll(jsonFile)
	var subdominios []Subdomain
	json.Unmarshal(byteValue, &subdominios)
	c.JSON(http.StatusOK, subdominios)
}
