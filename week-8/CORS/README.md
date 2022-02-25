# Test CORS (Cross-Origin Resource sharing)

While client side web broswer try to access the resource which is not the same as origin domain/protocol/port, it will create a cross-origin HTTP request.
XMLHttpRequest and Fetch all follow the same-origin policy. The same-origin policy limit all the API can only be used in the same domain othewise they must  
to use CORS header to query the API in different domain.

Reference: https://developer.mozilla.org/zh-TW/docs/Web/HTTP/CORS



## Fetch https://www.google.com/

### Error Response
```
Access to fetch at 'https://www.google.com/' from origin 'null' has been blocked by CORS policy: Response to preflight request doesn't pass access control check
: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to 
fetch the resource with CORS disabled.
```
### Test Result and Issue
![image](https://user-images.githubusercontent.com/63384830/155639294-57bdf539-7aad-42f5-b6ab-6867cae5c39f.png)

## Fetch https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json

### Error Response:
```
Access to fetch at 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json' from origin 'null' has been blocked 
by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the 
requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
```
### Test Result and Issue
![image](https://user-images.githubusercontent.com/63384830/155639123-4d69ede5-b83f-4439-8f93-8e5a17dbfa3a.png)
