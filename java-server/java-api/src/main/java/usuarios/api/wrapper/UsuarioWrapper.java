package usuarios.api.wrapper;

import org.springframework.stereotype.Component;

import users.core.models.User;
import usuarios.api.abstracts.ApiAbstractWrapper;
import usuarios.api.models.Usuario;

@Component
public class UsuarioWrapper extends ApiAbstractWrapper<Usuario, User> {

	@Override
	protected User wrapModel(Usuario model) {
		return User.builder()
				.birthday(model.getFechaNacimiento())
				.document(model.getDocumento())
				.gender(model.getGenero())
				.lastNames(model.getApellidos())
				.names(model.getDocumento())
				.username(model.getUsername())
				.build();
	}

	@Override
	protected Usuario unwrapModel(User model) {
		return new Usuario()
				.apellidos(model.getLastNames())
				.documento(model.getDocument())
				.fechaNacimiento(model.getBirthday())
				.genero(model.getGender())
				.nombres(model.getNames())
				.username(model.getUsername());
	}

}
