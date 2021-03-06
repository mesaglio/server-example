import { Router } from "https://deno.land/x/oak/mod.ts"

import {
    getAllUsers,
    getUserByUsername,
    deleteUser,
    updateUser,
    createUser
} from "../controllers/userController.ts"

import {
    ping
} from "../controllers/statusController.ts"

const router = new Router();

router
    .post("/usuarios", createUser)
    .get("/usuarios", getAllUsers)
    .get("/usuarios/:username", getUserByUsername)
    .delete("/usuarios/:username", deleteUser)
    .patch("/usuarios/:username", updateUser)
    .get("/ping", ping);

export default router;
