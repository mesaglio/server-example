package models

type User struct {
	Documento		string `json:"documento" binding:"required"`
	Username		string `json:"username" binding:"required"`
	Nombres			string `json:"nombres" binding:"required"`
	Apellidos		string `json:"apellidos" binding:"required"`
	Genero			string `json:"genero" binding:"required"`
	FechaNacimiento	string `json:"fechaNacimiento" binding:"required"`
}
