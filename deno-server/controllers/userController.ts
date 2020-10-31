import { User } from "./../models/user.ts";
let users: Array<User> = [];

const getAllUsers = ({ response }: { response: any }) => {
	response.body = users;
};

const getUserByUsername = ({ params, response }: {
	params: { username: string };
	response: any;
}) => {
	const user =
		users.filter((listUser: User) => listUser.username === params.username)[0];
	if (user) {
		response.status = 200;
		response.body = user;
	} else {
		response.status = 404;
		response.body = { msg: "Not found" };
	}
};

const createUser = async ({ request, response }: {
	request: any;
	response: any;
}) => {
	const body = await request.body();
	const user: User = await body.value;
	users.push(user);
	response.status = 201;
};

const updateUser = async ({
	params,
	request,
	response,
}: {
	params: { username: string };
	request: any;
	response: any;
}) => {
	const user =
		users.filter((listUser: User) => listUser.username === params.username)[0];
	if (user) {
		const body = await request.body();
		const newUser: User = await body.value;
		user.apellidos = await newUser.apellidos;
		user.documento = await newUser.documento;
		user.fechaNacimiento = await newUser.fechaNacimiento;
		user.genero = await newUser.genero;
		user.nombres = await newUser.nombres;
		user.username = await newUser.username;
		response.status = 200;
		response.body = user;
	} else {
		response.status = 404;
		response.body = { msg: "Not found" };
	}
};

const deleteUser = ({
	params,
	response,
}: {
	params: { username: string };
	response: any;
}) => {
	users = users.filter((user) => user.username !== params.username);
	response.status = 200;
};

export { getAllUsers, getUserByUsername, updateUser, deleteUser, createUser };

