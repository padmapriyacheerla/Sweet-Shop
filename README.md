# Sweet-Shop


# Sweet Management System

## Overview

The Sweet Management System is a full-featured web application developed using Django, designed to efficiently manage the operations of a sweet shop. It allows users to browse a catalog of sweets, place orders, and track the status of their orders. On the other hand, administrators can manage users, products, and orders from a comprehensive dashboard. The system integrates Microsoft SQL Server (MSSQL) to store and manage the data in a highly scalable and secure manner.

This system provides a complete solution for managing a sweet shop, handling both customer-facing functionalities (like ordering and product browsing) and administrative tasks (like product management, order tracking, and user management). The system ensures smooth customer experiences, streamlined administrative operations, and a high level of data integrity.

## Key Features

### For Users:
- **Browse Products**: Users can easily browse a catalog of sweets, filter them based on categories (such as Premium, Traditional, Dry Fruit, Festival Special), and search for specific sweets by name.
- **Order Placement**: After browsing the menu, users can place an order by specifying the quantity of the product, providing their address and contact number, and selecting the payment method.
- **User Registration & Authentication**: Users can create an account, log in to their profile, and securely manage their details, including their personal information and order history.
- **Product Availability**: The system dynamically updates the stock of sweets, ensuring that users can only order items that are available in stock.

### For Admins:
- **Admin Dashboard**: Admins have access to a dashboard that provides detailed analytics and real-time data on users, orders, and products. This includes the number of registered users, total sweets in stock, and the total number of orders.
- **Product Management**: Admins can add, update, and delete sweets from the menu. They can also manage the stock and prices of each product.
- **Order Management**: Admins can view all customer orders, process them, and mark them as delivered or pending. They can also handle changes to orders as necessary.
- **User Management**: Admins can manage registered users, including updating their details, suspending accounts, or deleting users from the system.
- **Contact Form Management**: Admins can view messages submitted by users through the contact form and respond to inquiries.

## Technologies Used

### Backend:
- **Django**: The primary web framework used for building the application. It provides a robust, scalable backend for handling user authentication, data management, and the overall application logic.
- **Python**: The programming language used for writing the logic behind the Django framework.
- **Microsoft SQL Server (MSSQL)**: The database system used for storing data, including users, orders, and sweets information. MSSQL ensures high performance, reliability, and scalability for the system.

### Frontend:
- **HTML, CSS, and JavaScript**: Used for rendering the front-end user interface and handling the dynamic aspects of the website.
- **Bootstrap**: A responsive front-end framework used for building a modern, mobile-first, and responsive design.
- **jQuery**: A JavaScript library used for easier DOM manipulation and Ajax requests.

### Authentication:
- **Django Authentication**: A built-in feature of Django that handles user authentication and authorization, including login, registration, and password management.

## System Architecture

The architecture of the Sweet Management System is organized to ensure flexibility and scalability. Here’s a breakdown of the system’s structure:

### Models:
- **Users**: Stores the details of all registered users, including their full name, email, phone number, and password (hashed).
- **Sweets**: Represents the products (sweets) in the system. It contains fields for the sweet’s name, price, category, image, and stock quantity.
- **Order**: Stores information about customer orders, including the user’s details, the sweet ordered, the quantity, delivery address, and phone number.
- **AdminUsers**: Stores the login details of administrators, including their username, email, and password (hashed).
- **Contact**: Stores messages submitted by users via the contact form on the website.

### Views:
- **Home View**: Displays all available sweets to users. This is the default view when the user visits the site.
- **Login/Registration Views**: Allows users to register or log in. The system validates the inputs and ensures the user is authenticated before granting access.
- **Menu View**: Displays all sweets, with options for filtering by category and searching by name.
- **Order Submission View**: Collects the order details from users, including quantity, address, and phone number, and processes the order.
- **Admin Views**: Provides views for the admin to manage the entire system. This includes managing users, orders, and products from the dashboard.

## Database Design

The MSSQL database is used to store all data related to users, sweets, orders, and messages. The database design includes the following key tables:

- **Users**: Stores user information such as name, email, and phone number.
- **Sweets**: Contains details about each sweet, including name, price, stock, and category.
- **Orders**: Holds order details, such as the user placing the order, the product ordered, and the order’s delivery address.
- **AdminUsers**: Contains details about the admin users for authentication.
- **Contact**: Stores messages sent by users through the contact form.

The database uses foreign key relationships to ensure that orders are linked to both users and sweets.

## Process Flow
1. **User Registration and Login**:
   - The user can create an account by providing their details (name, email, phone number, and password).
   - Passwords are securely hashed before being stored in the database.
   - Upon logging in, the user is authenticated using Django’s built-in authentication system.

2. **Product Browsing**:
   - Users can view a list of sweets available for purchase. They can filter sweets by categories such as "Premium," "Traditional," "Dry Fruit," and "Festival Special."
   - A search feature allows users to search for a specific sweet by name.

3. **Placing an Order**:
   - Once the user selects a sweet, they can specify the quantity and provide delivery details, including their address and phone number.
   - The system checks the availability of the selected quantity in the stock and processes the order if sufficient stock is available. The stock is then updated automatically.

4. **Admin Management**:
   - Admin users can log in to manage the system. They can add, update, or delete products, view orders, and manage user accounts.
   - The admin dashboard gives an overview of total users, total sweets, and the number of orders placed.

5. **Order Management**:
   - Admins can view all orders placed by users and mark them as completed or pending. They can also delete any unwanted orders.

6. **Handling Messages**:
   - Users can send messages through the contact form. Admins can view and respond to these messages.

## Future Enhancements
- **Payment Gateway Integration**: Integrate a payment gateway like Razorpay or Stripe to allow users to make payments directly from the website.
- **SMS Notification**: Send SMS notifications to users when their order is confirmed or shipped.
- **Rating and Review System**: Allow users to rate and review products, helping other customers make informed decisions.
- **Admin Dashboard Improvements**: Enhance the admin dashboard to provide more advanced analytics and filtering options.
- **Stock Replenishment Alerts**: Admins can receive alerts when stock levels are low.

## Conclusion

The Sweet Management System is a robust, feature-rich web application designed to manage the daily operations of a sweet shop. Built with Django and integrated with MSSQL, the system ensures that users can easily browse and order sweets while administrators have the tools they need to manage the catalog, process orders, and maintain customer satisfaction. The system is scalable, user-friendly, and provides an intuitive experience for both users and administrators.
