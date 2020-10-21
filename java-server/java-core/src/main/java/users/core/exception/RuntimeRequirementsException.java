package users.core.exception;

public class RuntimeRequirementsException extends RuntimeException {

	private static final long serialVersionUID = 560518244002327225L;

	public RuntimeRequirementsException() {
		super();
	}

	public RuntimeRequirementsException(String message, Throwable cause) {
		super(message, cause);
	}

	public RuntimeRequirementsException(String message) {
		super(message);
	}

}
