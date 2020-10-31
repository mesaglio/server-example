const ping = ({ response }: { response: any }) => {
    response.status = 200;
    response.body = { msg: "Pong" };
}

export { ping };