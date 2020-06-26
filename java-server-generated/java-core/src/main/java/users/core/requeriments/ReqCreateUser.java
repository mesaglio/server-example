package users.core.requeriments;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import users.core.abstracts.HandlerRequirements;
import users.core.manager.UsersManager;
import users.core.models.User;

@Component
public class ReqCreateUser extends HandlerRequirements<User, Void> {

	@Autowired
	private UsersManager userManagers;

	@Override
	protected Void execute(User request) {
		userManagers.addUser(request);
		return null;
	}

}
