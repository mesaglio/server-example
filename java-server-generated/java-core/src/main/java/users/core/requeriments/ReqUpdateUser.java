package users.core.requeriments;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import users.core.abstracts.HandlerRequirements;
import users.core.manager.UsersManager;
import users.core.models.User;
import users.core.models.UserWithUsername;

@Component
public class ReqUpdateUser extends HandlerRequirements<UserWithUsername, User> {

	@Autowired
	private UsersManager userManager;

	@Override
	protected User execute(UserWithUsername request) {
		return userManager.updateUser(request);
	}

}
