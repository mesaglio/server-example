package users.core.models;

import lombok.Builder;
import lombok.Getter;

@Builder
@Getter
public class UserWithUsername {
	private User user;
	private String username;
}
