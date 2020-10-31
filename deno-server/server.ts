import { Application } from "https://deno.land/x/oak/mod.ts";
import router from "./router/router.ts"

const HOST = "127.0.0.1";
const PORT = 8080;

const app = new Application();

app.use(router.routes());
app.use(router.allowedMethods());

console.log(`Welcome API Deno :) ${HOST}:${PORT}...`);
await app.listen(`${HOST}:${PORT}`);