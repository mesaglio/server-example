package models

type User struct {
	Documento		string `json:"documento"`
	Username		string `json:"username"`
	Nombres			string `json:"nombres"`
	Apellidos		string `json:"apellidos"`
	Genero			string `json:"genero"`
	FechaNacimiento	string `json:"fechaNacimiento"`
}
