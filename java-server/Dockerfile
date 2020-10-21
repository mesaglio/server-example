FROM maven:3.6.2-jdk-8 AS MAVEN_BUILD
COPY . /build/
RUN mvn -f /build/java-core install && mvn -f /build/java-api install

FROM openjdk:8-jre-alpine
WORKDIR /app
COPY --from=MAVEN_BUILD /build/java-api/target/api-0.0.1-SNAPSHOT.jar /app/
ENTRYPOINT ["java", "-jar", "api-0.0.1-SNAPSHOT.jar"]