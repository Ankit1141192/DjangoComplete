# MVT Architecture in Django

Django follows the **MVT (Model–View–Template)** architectural pattern.  
It separates the application into three core components, making the code more organized, reusable, and easier to maintain.

---

## What is MVT?

**MVT** stands for:

- **Model** – Handles data and database logic
- **View** – Handles business logic and processes requests
- **Template** – Handles the presentation layer (HTML)

Django internally manages the controller logic, allowing developers to focus on application development.

---

## Components of MVT

### 1. Model
- Represents the database structure
- Defines data fields and relationships
- Handles data creation, retrieval, update, and deletion (CRUD)
- Written using Django ORM

### 2. View
- Receives HTTP requests from the user
- Contains business logic
- Interacts with the model to fetch or save data
- Sends data to the template

### 3. Template
- Defines how data is presented to the user
- Written using HTML with Django Template Language (DTL)
- Displays dynamic data sent by views

---

## MVT Workflow

The MVT workflow defines how a request from the user is processed and how the response is returned.

---

## MVT Workflow – Step by Step

1. **User sends a request (URL)**  
   The user requests a page through the browser.

2. **URL Dispatcher maps the request to a View**  
   Django’s URL configuration (`urls.py`) determines which view should handle the request.

3. **View interacts with Model**  
   The view processes the request and communicates with the model to get or save data.

4. **View sends data to Template**  
   After processing, the view passes the data to a template.

5. **Template renders HTML**  
   The template generates dynamic HTML using the received data.

6. **HTML is sent as a response to the user**  
   Django returns the rendered HTML page to the user’s browser.

---

## MVT vs MVC

Django’s **MVT** architecture is a **variation of the traditional MVC (Model–View–Controller)** pattern.  
The core concept remains the same; only the terminology differs.

### MVC (Model–View–Controller)

- **Model** – Manages data and database logic
- **View** – Handles the user interface
- **Controller** – Handles request processing and business logic

### MVT (Model–View–Template)

- **Model** – Manages data and database logic
- **View** – Handles request processing and business logic  
  *(Acts like the Controller in MVC)*
- **Template** – Handles the presentation layer (HTML)

### Key Difference

- In **MVC**, the **Controller** manages the logic
- In **Django MVT**, the **View** acts as the Controller
- **Template** replaces the traditional View of MVC

> ✔️ The architecture is conceptually the same — only the naming convention is different.

---

## Summary

- MVT separates data, logic, and presentation
- Improves code readability and maintainability
- Allows faster and more scalable development
- Automatically handled by the Django framework

---

## Conclusion

The **MVT architecture** is one of the core strengths of Django.  
It provides a clean structure that helps developers build secure, scalable, and maintainable web applications efficiently.
