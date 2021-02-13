# [Sinatra](http://sinatrarb.com/) implementation

Requirements: 
```
Ruby >= 2.6.3
Bundle 2.2.9
```
With docker
```
$ docker build -t ruby-server
$ docker run -p 8080:8080 ruby-server
```

Without docker:
```
$ bundler install && ruby main.rb
```