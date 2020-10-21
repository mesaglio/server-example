package users.core.requeriments;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import users.core.abstracts.HandlerRequirements;
import users.core.manager.UsersManager;
import users.core.models.User;

@Component
public class ReqGetAllUsers extends HandlerRequirements<Void, List<User>> {

	@Autowired
	private UsersManager userManager;

	@Override
	protected List<User> execute(Void request) {
		return userManager.getUsers();
	}

}
