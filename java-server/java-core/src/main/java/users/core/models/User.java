package users.core.models;

import lombok.Builder;
import lombok.Getter;

@Builder
@Getter
public class User {
	private String document;
	private String username;
	private String names;
	private String lastNames;
	private String gender;
	private String birthday;
}
