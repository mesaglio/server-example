package swagger

import (
	"net/http"
	"net/url"
	"strings"
)

func printUsuarios() string {
	var _usuarios = ""
	for i := 0; i < len(usuarios); i++ {
		_usuarios = _usuarios + toJson(usuarios[i])
	}
	return "[" + _usuarios + "]"
}

func buscarUsuarioPorUsername(username string) (*Usuario, *int) {
	for i := 0; i < len(usuarios); i++ {
		usuario := usuarios[i]
		if usuario.Username == username {
			return usuario, &i
		}
	}
	return nil, nil
}

func getPathParam(w http.ResponseWriter, r *http.Request) *string {
	_url, err := url.Parse(r.URL.Path)
	username := strings.Split(string(_url.Path), "/")[2]
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return nil
	}
	return &username
}

func removeByUsername(username string) bool {
	_, indice := buscarUsuarioPorUsername(username)
	if indice == nil {
		return false
	}
	usuarios[len(usuarios)-1], usuarios[*indice] = usuarios[*indice], usuarios[len(usuarios)-1]
	usuarios = usuarios[:len(usuarios)-1]
	return true
}
