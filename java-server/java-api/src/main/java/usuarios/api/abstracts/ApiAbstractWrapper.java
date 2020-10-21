package usuarios.api.abstracts;

import java.util.Collections;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

public abstract class ApiAbstractWrapper<T, Y> {

	protected abstract Y wrapModel(T model);

	protected abstract T unwrapModel(Y model);

	public List<Y> wrapList(List<T> models) {
		return Optional.ofNullable(models).orElse(Collections.emptyList()).stream().map(this::wrap)
				.collect(Collectors.toList());
	}

	public List<T> unwrapList(List<Y> models) {
		return Optional.ofNullable(models).orElse(Collections.emptyList()).stream().map(this::unwrap)
				.collect(Collectors.toList());
	}

	public Y wrap(T model) {
		if (model == null)
			return null;
		return wrapModel(model);
	}

	public T unwrap(Y model) {
		if (model == null)
			return null;
		return unwrapModel(model);
	}
}
