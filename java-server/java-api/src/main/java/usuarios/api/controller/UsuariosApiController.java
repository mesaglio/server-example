package usuarios.api.controller;

import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;

import users.core.models.User;
import users.core.requeriments.ReqCreateUser;
import users.core.requeriments.ReqDeleteUser;
import users.core.requeriments.ReqGetAllUsers;
import users.core.requeriments.ReqGetUser;
import users.core.requeriments.ReqUpdateUser;
import usuarios.api.models.Usuario;
import usuarios.api.models.UsuarioUsername;
import usuarios.api.wrapper.UsuarioUsernameWrapper;
import usuarios.api.wrapper.UsuarioWrapper;

@Controller
public class UsuariosApiController implements UsuariosApi {

	/**
	 * Requerimientos
	 */
	@Autowired
	private ReqCreateUser reqCreateUser;

	@Autowired
	private ReqDeleteUser reqDeleteUser;

	@Autowired
	private ReqGetUser reqGetUser;

	@Autowired
	private ReqGetAllUsers reqGetAllUsers;

	@Autowired
	private ReqUpdateUser reqUpdateUser;

	/**
	 * Wrappers
	 */
	@Autowired
	private UsuarioWrapper usuarioWrapper;

	@Autowired
	private UsuarioUsernameWrapper usuarioUsernameWrapper;

	@Override
	public ResponseEntity<Usuario> actualizarUsuarioByUsername(@Valid Usuario body, String username) {
		UsuarioUsername usuarioConUsername = UsuarioUsername.builder()
				.username(username)
				.usuario(body)
				.build();
		User user = reqUpdateUser.run(usuarioUsernameWrapper.wrap(usuarioConUsername));
		return ResponseEntity.ok(usuarioWrapper.unwrap(user));
	}

	@Override
	public ResponseEntity<Void> crearUsuario(@Valid Usuario body) {
		reqCreateUser.run(usuarioWrapper.wrap(body));
		return ResponseEntity.ok().build();
	}

	@Override
	public ResponseEntity<Void> eliminarUsuarioByUsername(String username) {
		reqDeleteUser.run(username);
		return ResponseEntity.ok().build();
	}

	@Override
	public ResponseEntity<Usuario> obtenerUsuarioByUsername(String username) {
		User user = reqGetUser.run(username);
		return ResponseEntity.ok(usuarioWrapper.unwrap(user));
	}

	@Override
	public ResponseEntity<List<Usuario>> obtenerUsuarios() {
		List<User> users = reqGetAllUsers.run(null);
		return ResponseEntity.ok(usuarioWrapper.unwrapList(users));
	}

}
