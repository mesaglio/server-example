package swagger

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestPing(t *testing.T) {
	request, _ := http.NewRequest(http.MethodGet, "/", nil)
	response := httptest.NewRecorder()
	Ping(response, request)
	t.Run("returns Pepper's score", func(t *testing.T) {
		got := response.Body.String()
		want := "Pong"

		if got != want {
			t.Errorf("got %q, want %q", got, want)
		}
	})
}
