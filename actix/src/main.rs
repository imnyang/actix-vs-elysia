use actix_web::{web, App, HttpServer, Responder, HttpResponse, get, post};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[get("/")]
async fn index() -> impl Responder {
    "Hi"
}

#[get("/id/{id}")]
async fn get_id(
    id: web::Path<String>,
    query: web::Query<HashMap<String, String>>
) -> impl Responder {
    let name = query.get("name").cloned().unwrap_or_default();
    HttpResponse::Ok()
        .insert_header(("x-powered-by", "benchmark"))
        .body(format!("{} {}", id, name))
}

#[derive(Debug, Serialize, Deserialize)]
struct JsonData {
    hello: String,
}

#[post("/json")]
async fn post_json(data: web::Json<JsonData>) -> impl Responder {
    HttpResponse::Ok().json(data.into_inner())
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(index)
            .service(get_id)
            .service(post_json)
    })
    .bind(("127.0.0.1", 3001))?
    .run()
    .await
}
