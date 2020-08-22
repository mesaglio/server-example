package usuarios.api.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/")
public class RedirectController {
	
	@GetMapping
	private String pingRedirect() {
		return "redirect:ping";
	}
}
