package users.core.manager;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import javax.annotation.PostConstruct;

import org.apache.commons.lang3.StringUtils;
import org.springframework.stereotype.Component;

import users.core.exception.RuntimeRequirementsException;
import users.core.models.User;
import users.core.models.UserWithUsername;

@Component
public class UsersManager {

	private List<User> users;

	@PostConstruct
	public void postConstructor() {
		users = new ArrayList<>();
	}

	public void addUser(User user) {
		if (users.stream().anyMatch(listUser -> StringUtils.equals(listUser.getUsername(), user.getUsername())))
			throw new RuntimeRequirementsException("El username ya esta utilizado");
		users.add(user);
	}

	public void deleteUserByUsername(String username) {
		users.removeIf(user -> StringUtils.equals(user.getUsername(), username));
	}

	public User getUserByUsername(String username) {
		return users.stream()
				.filter(user -> StringUtils.equals(user.getUsername(), username))
				.findFirst()
				.orElse(null);
	}

	public List<User> getUsers() {
		return users;
	}

	public User updateUser(UserWithUsername request) {
		users = users.stream().map(user -> isTheUser(user, request)).collect(Collectors.toList());
		return request.getUser();

	}

	private User isTheUser(User user, UserWithUsername userWithUsername) {
		if (StringUtils.equals(user.getUsername(), userWithUsername.getUsername()))
			return userWithUsername.getUser();
		return user;
	}

}
