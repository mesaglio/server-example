#[get("/")]
pub fn ping() -> String {
    String::from("Pong")
}
