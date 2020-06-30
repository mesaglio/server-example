With docker:
```
$ docker build -t java-server .
$ docker run -p 8080:8080 java-server
```

Without docker:
```
$ mvn -f java-api/ install 
$ java -jar java-api/tarjet/api-0.0.1-SNAPSHOT.jar
```
