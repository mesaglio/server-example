package usuarios.api.models;

import lombok.Builder;
import lombok.Getter;

@Builder
@Getter
public class UsuarioUsername {
	private Usuario usuario;
	private String username;
}
