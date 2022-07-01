#[macro_use]
extern crate rocket;

mod routes;

#[launch]
fn rocket() -> _ {
    rocket::build()
        .mount("/ping", routes![routes::ping::ping])
        .mount("/users", routes![routes::users::users])
}
