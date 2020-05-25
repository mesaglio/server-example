package swagger

import "encoding/json"

type Error struct {
	Mensaje string
}

func errorToJson(error Error) string {
	e, _ := json.Marshal(&error)
	return string(e)
}
