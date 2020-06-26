package usuarios.api.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;

@Controller
public class PingApiController implements PingApi {

	@Override
	public ResponseEntity<String> ping() {
		return ResponseEntity.ok("Pong");
	}

}
