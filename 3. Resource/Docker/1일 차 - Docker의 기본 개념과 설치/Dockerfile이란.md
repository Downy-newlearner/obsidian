
```
FROM openjdk:17

WORKDIR /app

COPY build/libs/smart_score-0.0.1-SNAPSHOT.jar app.jar

ENTRYPOINT ["java", "-jar", "app.jar"]
```


![[Pasted image 20250110025218.png]]


![[Pasted image 20250110025224.png]]
인스트럭션은 키워드라고 생각하면 된다.

![[Pasted image 20250110025327.png]]

![[Pasted image 20250110025410.png]]

![[Pasted image 20250110025436.png]]

![[Pasted image 20250110025455.png]]

![[Pasted image 20250110025544.png]]


![[Pasted image 20250110025554.png]]

