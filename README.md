# Project Overview and Features


### 1. Landing Page
Components: Home, About Us, Services, Departments, Staff, Blogs, Testimonials, Contact.
![1](https://github.com/MohammedHabib123/Django_hospital_Management_System/assets/130642209/189755de-fd03-4376-8979-a235a04db056)





### 2. User Authentication
Features: Sign In, Sign Up.<br>
Implementation:<br>
Use Django's built-in auth system for user registration and authentication.<br>
Custom user model if you need to extend the default user attributes.<br>
Provide different roles (patient, doctor,admision , admin).<br>
![2](https://github.com/MohammedHabib123/Django_hospital_Management_System/assets/130642209/ad287c8a-b641-4fde-86ef-e4b1529823bf)


### 3. Appointment Booking
Features: Choose a doctor, select time, book an appointment.<br>
Implementation:<br>
Create models for Doctors and Appointments.<br>
Provide views and forms for patients to book appointments.<br>
![4](https://github.com/MohammedHabib123/Django_hospital_Management_System/assets/130642209/b358c1e3-2378-425a-88c9-0001c5f57f8c)




### 4. Admin Dashboard
Features: Manage users, appointments, and access privileges<br>
Implementation:<br>
Use Django Admin for robust admin functionalities.<br>
Create custom admin views or use third-party admin enhancement tools (like django-grappelli or django-admin-interface).<br>
![5](https://github.com/MohammedHabib123/Django_hospital_Management_System/assets/130642209/649ca2c6-8ddc-4b96-aaa9-4066587471b0)
![6](https://github.com/MohammedHabib123/Django_hospital_Management_System/assets/130642209/443e5c09-5ad5-4d9a-a5bb-fba28a90d425)



### 5. User Roles and Permissions
Roles: Admin, Doctor,admision , Patient.<br>
Implementation:<br>
Use Django's permissions framework to assign different access levels.<br>
Admin: Full access to manage users and appointments.<br>
Doctor: Access to patient history and create medical records.<br>
Patient: Access to their bookings and personal information.<br>
admison:Provide access to booking details and management functionalities.<br>


### 6. Patient History
Features: Doctors can create and update patient records.<br>
Implementation:<br>
Create a model for Patient History.<br>
Allow doctors to add, update, and view patient records.<br>
Secure access to patient records based on roles.<br>
![7](https://github.com/MohammedHabib123/Django_hospital_Management_System/assets/130642209/970bd344-f64f-4d9a-a5fb-52ff003eb73d)
![8](https://github.com/MohammedHabib123/Django_hospital_Management_System/assets/130642209/da0da7dc-cbd3-4997-83a1-2f9e1eaa4f75)




### 7. Bokking details
Features: Admission has access to patient booking records, and it can delete them if they have been cancelled.<br>
admison:Provide access to booking details and management functionalities.<br>
![9](https://github.com/MohammedHabib123/Django_hospital_Management_System/assets/130642209/8626db04-cf36-4a44-90e7-3084bd93dc8f)
![10](https://github.com/MohammedHabib123/Django_hospital_Management_System/assets/130642209/f2567a54-3504-4942-8fc9-786be9cf9cba)
