package users.core.abstracts;

import users.core.exception.RuntimeRequirementsException;

public abstract class HandlerRequirements<T, Y> {

	protected abstract Y execute(T request);

	public Y run(T request) {
		try {
			return execute(request);
		} catch (RuntimeRequirementsException e) {
			throw e;
		} catch (Exception e) {
			throw new RuntimeRequirementsException("Ocurrio un erroe inesperado", e);
		}
	}
}
