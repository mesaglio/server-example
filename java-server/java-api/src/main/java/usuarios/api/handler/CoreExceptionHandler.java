package usuarios.api.handler;

import org.springframework.core.Ordered;
import org.springframework.core.annotation.Order;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

import users.core.exception.RuntimeRequirementsException;

@Order(Ordered.HIGHEST_PRECEDENCE)
@ControllerAdvice
public class CoreExceptionHandler extends ResponseEntityExceptionHandler {

	@ExceptionHandler(RuntimeRequirementsException.class)
	protected ResponseEntity<String> handlerRuntimeRequirementsException(RuntimeRequirementsException exception) {
		return ResponseEntity.ok(exception.getMessage());
	}

}
