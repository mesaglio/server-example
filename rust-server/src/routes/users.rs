use serde::{Deserialize, Serialize};

#[get("/")]
pub fn users() -> String {
    let user = [&User {
        id: 1,
        name: String::from("asd"),
    }];
    serde_json::to_string(&user).unwrap()
}

#[derive(Serialize, Deserialize, Debug)]
struct User {
    id: i32,
    name: String,
}
