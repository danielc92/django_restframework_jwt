# JWT (JSON Web Tokens) with Django REST Framework
Implementation of JSON Web Token authorization with a Django REST-API.

# Before you get started
- Understanding of APIs
- Understanding of POST, GET requests
- Usage of tool such as POSTMAN (optional)
- Understanding of Django

# Available Routes
- `http://localhost:8000/` FILLIN
- `http://localhost:8000/api-auth/`
- `http://localhost:8000/` - Lists available API routes.
- `http://localhost:8000/api/token/` - Allows user to create their JSON Web Token with a POST request given their credentials are stored in the body.
- `http://localhost:8000/api/token/refresh/` - Allows user to refresh their JWT 
- `http://localhost:8000/programmers/` - Lists programmers from the Programmer database model. Accepts POST/GET
- `http://localhost:8000/languages/` - Lists languages from the Language database model. Accepts POST/GET

# Setup
**How to obtain this repository:**
```sh
git clone https://github.com/danielc92/django_restframework_jwt.git
```

**Modules/dependencies:**
- `Django==2.2.2`
- `djangorestframework==3.9.4`
- `djangorestframework-simplejwt==4.3.0`

# Screenshots

### Successful auth attempt
Returns a valid token with refresh and access keys.
![Successful authorization attempt](https://github.com/danielc92/django_restframework_jwt/blob/master/screenshots/auth-attempt.jpg) 

### Unsuccesful GET request to `languages/` (invalid token)
![Wrong token provided with GET request](https://github.com/danielc92/django_restframework_jwt/blob/master/screenshots/wrong-token.jpg) 

### Successful GET request to `/languages`
![Successful languages GET request](https://github.com/danielc92/django_restframework_jwt/blob/master/screenshots/languages-get.jpg) 

# Contributors
- Daniel Corcoran

# Sources
- Language data pulled from Wikipedia
- [Documentation for `djangorestframework-simplejwt` library](https://pypi.org/project/djangorestframework-simplejwt/)
- [JSON Web Tokens With Django REST Framework by PrettyPrinted](https://www.youtube.com/watch?v=Fhcn2qx-4VQ)
