package swagger

import (
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

func TestActualizarUsuarioByUsernameFailFormato(t *testing.T) {
	request, _ := http.NewRequest(http.MethodPatch, "/usuarios/juan", strings.NewReader(""))
	response := httptest.NewRecorder()
	t.Run("Actualizar usuario por username con mal formato", func(t *testing.T) {
		ActualizarUsuarioByUsername(response, request)
		got := response.Code
		want := 400
		checkHttpStatus(t, got, want)
	})
}

func TestActualizarUsuarioByUsernameFailNoExiste(t *testing.T) {
	var body = strings.NewReader("{\n    \"documento\": \"39453024\",\n    \"username\": \"JuanM\",\n    \"nombres\": \"juan ignacio\",\n    \"apellidos\": \"mesaglio\",\n    \"genero\": \"M\",\n    \"fechaNacimiento\": \"10/01/1996\"\n}")
	request, _ := http.NewRequest(http.MethodPatch, "/usuarios/JuanM", body)
	response := httptest.NewRecorder()
	t.Run("Actualizar usuario por username que no existe.", func(t *testing.T) {
		ActualizarUsuarioByUsername(response, request)
		got := response.Code
		want := 404
		checkHttpStatus(t, got, want)
	})
}
func TestCrearUsuarioFail(t *testing.T) {
	request, _ := http.NewRequest(http.MethodPost, "/usuarios", strings.NewReader(""))
	response := httptest.NewRecorder()
	t.Run("Crear usuario con mal formato.", func(t *testing.T) {
		CrearUsuario(response, request)
		got := response.Code
		want := 400
		checkHttpStatus(t, got, want)
	})
}
func TestEliminarUsuarioByUsernameFail(t *testing.T) {
	request, _ := http.NewRequest(http.MethodDelete, "/usuarios/JuanM", nil)
	response := httptest.NewRecorder()
	t.Run("Eliminar usuario que no existe.", func(t *testing.T) {
		EliminarUsuarioByUsername(response, request)
		got := response.Code
		want := 404 // tiene que ser un 404
		checkHttpStatus(t, got, want)
	})
}
func TestObtenerUsuarioByUsernameFail(t *testing.T) {
	request, _ := http.NewRequest(http.MethodGet, "/usuarios/JuanM", nil)
	response := httptest.NewRecorder()
	t.Run("Obtener usuario que no existe.", func(t *testing.T) {
		ObtenerUsuarioByUsername(response, request)
		got := response.Code
		want := 404
		checkHttpStatus(t, got, want)
	})
}
func TestObtenerUsuariosEmpty(t *testing.T) {
	request, _ := http.NewRequest(http.MethodGet, "/usuarios", nil)
	response := httptest.NewRecorder()
	t.Run("Obtener usuarios vacios.", func(t *testing.T) {
		ObtenerUsuarios(response, request)
		got := response.Code
		want := 200
		users := response.Body.String()
		checkHttpStatus(t, got, want)
		s := "[]"
		if users != s {
			t.Errorf("got %s, want %s", s, users)
		}
	})
}

func TestCrearUsuario(t *testing.T) {
	var body = strings.NewReader("{\n    \"documento\": \"39453024\",\n    \"username\": \"JuanM\",\n    \"nombres\": \"juan ignacio\",\n    \"apellidos\": \"mesaglio\",\n    \"genero\": \"M\",\n    \"fechaNacimiento\": \"10/01/1996\"\n}")
	request, _ := http.NewRequest(http.MethodPost, "/usuarios", body)
	response := httptest.NewRecorder()
	t.Run("Crear usuario correctamente.", func(t *testing.T) {
		CrearUsuario(response, request)
		got := response.Code
		want := 201
		checkHttpStatus(t, got, want)
	})
}
func TestObtenerUsuarios(t *testing.T) {
	userString := "{\n    \"documento\": \"39453024\",\n    \"username\": \"JuanM\",\n    \"nombres\": \"juan ignacio\",\n    \"apellidos\": \"mesaglio\",\n    \"genero\": \"M\",\n    \"fechaNacimiento\": \"10/01/1996\"\n}"
	var body = strings.NewReader(userString)
	createRequest, _ := http.NewRequest(http.MethodPost, "/usuarios", body)
	createResponse := httptest.NewRecorder()
	request, _ := http.NewRequest(http.MethodGet, "/usuarios", nil)
	response := httptest.NewRecorder()
	t.Run("Obtener usuarios.", func(t *testing.T) {
		CrearUsuario(createResponse,createRequest)
		ObtenerUsuarios(response, request)
		got := response.Code
		want := 200
		users := response.Body.String()
		checkHttpStatus(t, got, want)
		if strings.Contains(users,userString) {
			t.Errorf("got %s, want %s", userString, users)
		}
	})
}
func TestEliminarUsuarioByUsername(t *testing.T) {
	var body = strings.NewReader("{\n    \"documento\": \"39453024\",\n    \"username\": \"JuanM\",\n    \"nombres\": \"juan ignacio\",\n    \"apellidos\": \"mesaglio\",\n    \"genero\": \"M\",\n    \"fechaNacimiento\": \"10/01/1996\"\n}")
	createRequest, _ := http.NewRequest(http.MethodPost, "/usuarios", body)
	createResponse := httptest.NewRecorder()
	request, _ := http.NewRequest(http.MethodDelete, "/usuarios/JuanM", nil)
	response := httptest.NewRecorder()
	t.Run("Eliminar usuario que existe.", func(t *testing.T) {
		CrearUsuario(createResponse, createRequest)
		EliminarUsuarioByUsername(response, request)
		got := response.Code
		want := 200
		checkHttpStatus(t, got, want)
	})
}
func checkHttpStatus(t *testing.T, got int, want int) {
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}
