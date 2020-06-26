package users.core.requeriments;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import users.core.abstracts.HandlerRequirements;
import users.core.manager.UsersManager;
import users.core.models.User;

@Component
public class ReqGetUser extends HandlerRequirements<String, User> {

	@Autowired
	private UsersManager userManager;

	@Override
	protected User execute(String request) {
		return userManager.getUserByUsername(request);
	}

}
