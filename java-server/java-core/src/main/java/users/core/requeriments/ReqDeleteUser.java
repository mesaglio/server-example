package users.core.requeriments;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import users.core.abstracts.HandlerRequirements;
import users.core.manager.UsersManager;

@Component
public class ReqDeleteUser extends HandlerRequirements<String, Void> {

	@Autowired
	private UsersManager userManager;

	@Override
	protected Void execute(String request) {
		userManager.deleteUserByUsername(request);
		return null;
	}

}
