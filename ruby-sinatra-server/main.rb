require 'sinatra'
require 'sinatra/json'

set :port, 8080
set :bind, "0.0.0.0"

usuarios = Array.new

helpers do
  def get_body
    JSON.parse(request.body.read) rescue nil
  end

  def valid_body?(body)
    body.has_key?("documento") and body.has_key?("username") and body.has_key?("nombres") and body.has_key?("apellidos") and body.has_key?("genero") and body.has_key?("fechaNacimiento")
  end

  def get_user_index(username, usuarios)
    usuarios.index { |usuario| usuario['username'] == username }
  end
end

get '/ping' do
  json('Pong')
end

get '/usuarios' do
  json(usuarios)
end

post '/usuarios' do
  body = get_body
  if valid_body?(body)
    usuarios.push(body)
    status 200
    json('Success')
  else
    status 400
  end
end

get '/usuarios/:username' do |username|
  i = get_user_index(username, usuarios)
  if i
    json(usuarios[i])
  else
    status 404
  end
end

delete '/usuarios/:username' do |username|
  i = get_user_index(username, usuarios)
  if i
    usuarios.delete_at(i)
  end
  status 200
end

patch '/usuarios/:username' do |username|
  body = get_body
  i = get_user_index(username, usuarios)
  unless i
    status 404
    return
  end
  if valid_body?(body)
    usuarios.delete_at(i)
    usuarios.push(body)
    status 200
    json('Success')
  else
    status 400
  end
end
