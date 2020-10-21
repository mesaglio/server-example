package usuarios.api.wrapper;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import users.core.models.UserWithUsername;
import usuarios.api.abstracts.ApiAbstractWrapper;
import usuarios.api.models.UsuarioUsername;

@Component
public class UsuarioUsernameWrapper extends ApiAbstractWrapper<UsuarioUsername, UserWithUsername> {

	@Autowired
	private UsuarioWrapper usuarioWrapper;

	@Override
	protected UserWithUsername wrapModel(UsuarioUsername model) {
		return UserWithUsername.builder()
				.user(usuarioWrapper.wrap(model.getUsuario()))
				.username(model.getUsername())
				.build();
	}

	@Override
	protected UsuarioUsername unwrapModel(UserWithUsername model) {
		return UsuarioUsername.builder()
				.username(model.getUsername())
				.usuario(usuarioWrapper.unwrap(model.getUser()))
				.build();
	}

}
