# Family Expense Tracker 💰
A full-stack, role-based **family finance management web application** that enables structured fund control, transparent expense tracking, and real-time analytics.
---

## 1. Project Overview

### 📌 Project Description

**Family Expense Tracker** is a web application designed to manage shared family finances through a **request–approval workflow**.
Family members request money for expenses, while a designated **Admin (Fund Manager)** controls funds, approves or rejects requests, records expenses, and monitors analytics.

The system ensures:

* No overspending beyond available funds
* Clear accountability for each expense
* Centralized expense history
* Real-time analytics and data export

The application is **fully built, tested, and deployed online**.

---

### ❓ Problem Statement

Traditional family expense tracking is usually done using:

* WhatsApp messages
* Verbal communication
* Notes or Excel sheets

This leads to:

* No approval mechanism
* No expense validation
* Confusion about remaining balance
* No history or analytics
* High chances of overspending

This project solves these issues by introducing a **controlled, digital expense management system**.

---

### 🎯 Target Users

* **Family Members**

  * Request money
  * Track request status
  * View total family expenses
  * Export expense data
* **Admin (Fund Manager)**

  * Add and manage funds
  * Approve / reject / send requests
  * Track expenses
  * View analytics dashboards

---

### 🎯 Core Purpose

To provide a **secure, transparent, and structured system** for managing shared family expenses with:

* Fund balance enforcement
* Role-based access
* Accurate accounting
* Visual analytics

---

## 2. Project Objectives

### ✅ Primary Objectives

* Implement a request-based expense flow
* Prevent expenses exceeding available funds
* Maintain accurate fund and expense records
* Separate member and admin responsibilities

---

### 🔁 Secondary Objectives

* Enable real-time request tracking
* Provide data export functionality
* Offer visual analytics using charts
* Ensure responsive UI for all devices

---

### 🚀 Long-Term Goals

* Add advanced authentication (JWT/session)
* Support multiple families or groups
* Improve analytics with filters
* Add notifications and audit logs

---

## 3. Application Flow (End-to-End)

### 👤 Member Flow

1. Login as **Member**
2. View Member Dashboard:

   * Total family expense
   * Member-wise expense cards
3. Request Money:

   * Select member name
   * Enter amount and reason
   * System checks available fund **before submitting**
4. Request Status Page:

   * View all requests with real-time status
5. Export Page:

   * Preview expense data
   * Download expense history as CSV
6. Logout

---

### 👨‍💼 Admin Flow

1. Login as **Admin**
2. Analytics Dashboard:

   * Total fund
   * Total expense
   * Current balance
   * Member-wise expense distribution (Pie Chart)
   * Weekly / Monthly / yearly expense trends (Bar Chart)
3. Add Fund:

   * Add funds with reason
   * View fund history
4. Requests Management:

   * View new requests
   * Approve or reject requests
   * Send money (records expense)
   * Requests move to history only after reject or send
5. Logout

---

## 4. Key Features

### 🔐 Role-Based Authentication

* Separate login credentials for **Admin** and **Members**
* Access control enforced at UI and API level

---

### 📨 Request-Based Expense System

* Members submit expense requests
* Status lifecycle:

  * `pending`
  * `approved`
  * `rejected`
  * `sent`
  * `insufficient`
* Requests exceeding available funds are **blocked immediately**

---

### 💰 Fund Management

* Admin adds funds manually
* Fund history stored and displayed
* Current balance calculated dynamically

---

### 📊 Expense Tracking

* Expenses recorded **only when admin sends money**
* No duplicate expense entries
* Expenses linked to request IDs

---

### 📈 Analytics Dashboard

* Total fund, expense, and balance KPIs
* Member-wise expense distribution (Pie Chart)
* Weekly / Monthly / yearly expense trends (Bar Chart)
* Charts powered by **Chart.js**

---

### 📤 Data Export

* Members can preview expense data
* Export expense history as CSV file

---

### 📱 Responsive UI

* Fully responsive for:

  * Mobile
  * Tablet
  * Laptop
  * Desktop
* Sidebar-based navigation for admin
* Clean dashboards for members
---


2.second part 

---

## 4. Tech Stack

### Frontend

* **Framework / Library**

  * Vanilla **HTML5, CSS3, JavaScript**
  * No frontend frameworks (React/Vue) used to keep the system lightweight and dependency-free

* **Styling**

  * Custom CSS
  * Responsive layout using Flexbox and Grid
  * Sidebar-based navigation for Admin
  * Card-based dashboards for Members
  * Chart styling handled by Chart.js defaults

* **State Management**

  * Browser **LocalStorage**

    * Stores logged-in user role
    * Stores current member identity
  * No external state management library used

---

### Backend

* **Language**

  * Python

* **Framework**

  * Flask (REST API-based architecture)

* **Authentication Mechanism**

  * Role-based login (Admin / Member)
  * Credential validation against MongoDB
  * Session handled via frontend routing + LocalStorage
  * No JWT or OAuth used (intentionally kept simple)

* **APIs**

  * Authentication APIs (`/login`)
  * Request APIs (`/add-request`, `/member-requests`)
  * Admin APIs (`/admin-requests`, `/update-request`)
  * Fund APIs (`/add-fund`, `/fund-history`)
  * Analytics APIs (`/analytics`)
  * Export APIs (`/export-expenses`)
  * Expense APIs (`/all-expenses`, `/member-expenses`)

---

### Database

* **Database Type**

  * MongoDB Atlas (Cloud NoSQL database)

* **Driver**

  * `pymongo` (official MongoDB Python driver)

* **Collections Used**

  * `users`
  * `funds`
  * `requests`
  * `expenses`

* **Design Choice**

  * No MongoDB `_id` exposed to frontend
  * Custom `requestId` used for tracking and linking records

---

### Infrastructure

* **Hosting Platform**

  * Backend API: **Render**
  * Frontend: **Netlify**
  * Database: **MongoDB Atlas**

* **Deployment Method**

  * Backend deployed using **Gunicorn WSGI server**
  * Frontend deployed as static assets
  * Environment variables configured via Render dashboard

* **Version Control**

  * Git
  * GitHub (public repository)

---

## 5. High-Level Architecture

### Architecture Type

* **Client–Server Architecture**
* RESTful API-based communication
* Clear separation of frontend and backend

---

### Major Components

1. **Frontend (Client)**

   * HTML pages for Member and Admin dashboards
   * JavaScript handles:

     * API calls
     * DOM updates
     * Role-based routing
   * Hosted independently on Netlify

2. **Backend (Server)**

   * Flask application exposing REST APIs
   * Handles:

     * Business logic
     * Validation
     * Fund balance enforcement
     * Request lifecycle
   * Hosted on Render

3. **Database**

   * MongoDB Atlas
   * Stores persistent data for users, funds, requests, and expenses

---

### Data Flow Overview

1. User logs in from frontend
2. Frontend sends credentials to backend `/login`
3. Backend validates user and returns role
4. Frontend routes user based on role
5. Member actions (request money, view status) call backend APIs
6. Admin actions (approve, reject, send, add fund) update database
7. Analytics APIs aggregate data from MongoDB
8. Frontend dashboards render real-time data

---

## 6. Folder Structure

### Frontend Folder

```
frontend/
│── css/
│   ├── admin-analytics.css
│   ├── admin-requests.css
│   ├── admin-add-fund.css
│   ├── member-home.css
│   ├── request.css
│   ├── status.css
│   └── export.css/ landing.css / login.css
│
│── js/
│   ├── login.js
│   ├── member-home.js
│   ├── request.js
│   ├── status.js
│   ├── export.js
│   ├── admin-analytics.js
│   ├── admin-requests.js
│   └── admin-add-fund.js/ landing.js
│
│── login.html
│── member-home.html
│── request.html
│── status.html
│── export.html
│── admin-analytics.html
│── admin-requests.html
│── admin-add-fund.html / landing.html
```

**Purpose**

* UI rendering
* API integration
* Role-based navigation
* Client-side validation

---

### Backend Folder

```
backend/
│── main.py
│── requirements.txt
│── .env
│
├── app/
│   ├── config/
│   │   └── db.py
│   │
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── request_routes.py
│   │   ├── admin_routes.py
│   │   ├── expense_routes.py
│   │   └── analytics_routes.py
│   │
│   ├── controllers/
│   │   ├── request_controller.py
│   │   ├── admin_controller.py
|   |   ├── auth_controller.py
|   |   ├── expense_controller.py
│   │   └── analytics_controller.py
│   │
│   └── services/
│   |    ├── request_service.py
│   |    ├── admin_service.py
|   |    ├── auth_service.py
|   |    ├── expense_service.py
|   |    ├── searilezer_service.py
│   |    └── analytics_service.py 
|   | 
|   |___ models/
|       |__ expese_model.py
|       |__ user_model.py
|       |__ request_model.py 
|   
```

**Purpose**

* API routing
* Business logic separation
* Database operations
* Analytics calculations

---

### Configuration Folder

* `.env`

  * MongoDB connection URI
* `db.py`

  * MongoDB client initialization
  * Centralized DB access

---

### Documentation

* `README.md`
* Deployment instructions
* Architecture explanation
* API descriptions

---





3. section part
---

## 7. Environment Variables

### Required Environment Variables

| Variable Name | Required | Description                                     |
| ------------- | -------- | ----------------------------------------------- |
| `MONGO_URI`   | ✅ Yes    | MongoDB Atlas connection string                 |
| `FLASK_ENV`   | Optional | Environment mode (`development` / `production`) |
| `PORT`        | Optional | Server port (Render auto-assigns)               |

---

### Purpose of Each Variable

* **MONGO_URI**

  * Stores the MongoDB Atlas connection URL
  * Used by `db.py` to initialize the database connection
  * Example:

    ```
    MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/test_db
    ```

* **FLASK_ENV**

  * Controls Flask debug behavior
  * Used locally for debugging
  * Disabled in production

* **PORT**

  * Required by cloud platforms like Render
  * Flask automatically binds to this port in production

---

## 8. Local Setup & Execution

### Prerequisites

* Python 3.10+
* MongoDB Atlas account
* Git
* Code editor (VS Code recommended)

---

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/VDhanush75/expense-tracker.git
   cd expense-tracker/backend
   ```

2. **Create Virtual Environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate # macOS/Linux
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` File**

   ```env
   MONGO_URI=your_mongodb_connection_string
   ```

5. **Run Backend Server**

   ```bash
   python app.py
   ```

6. **Run Frontend**

   * Open frontend HTML files using Live Server
   * OR open directly in browser

---

### Run Commands Summary

| Component  | Command               |
| ---------- | --------------------- |
| Backend    | `python app.py`       |
| Frontend   | Live Server / Browser |
| Production | `gunicorn app:app`    |

---

## 9. Deployment Overview

### Deployment Platforms

* **Frontend**: Netlify
* **Backend**: Render
* **Database**: MongoDB Atlas

---

### Build Process

#### Backend (Render)

1. Connect GitHub repository
2. Install dependencies from `requirements.txt`
3. Use Gunicorn as WSGI server
4. Set environment variables in Render dashboard
5. Start command:

   ```bash
   gunicorn app:app
   ```

#### Frontend (Netlify)

1. Upload frontend folder
2. Deploy static files
3. Configure backend API base URL
4. Enable HTTPS automatically

---

### Environment Separation

| Environment | Purpose                 |
| ----------- | ----------------------- |
| Local       | Development & debugging |
| Production  | Live deployment         |
| Database    | Shared Atlas cluster    |

---

## 10. CI/CD Readiness

### Pipeline Stages

* Code commit to GitHub
* Auto build triggered on Render & Netlify
* Dependency installation
* Deployment

---

### Automation Scope

* Automatic deployment on `main` branch push
* No manual intervention required
* Environment variables managed securely

---

### Branching Strategy

* `main` branch used for stable deployment
* Feature development can be done using feature branches
* Direct push model used for this project

---

## 11. Documentation References

* **Requirements Document**

  * Defines functional and non-functional requirements

* **Software Specification Document**

  * API definitions
  * Business rules
  * User roles and permissions

* **System Design Document**

  * Architecture
  * Data flow
  * Component interaction

* **Deployment & CI/CD Document**

  * Render + Netlify deployment steps
  * Environment configuration

* **Final Project Report**

  * Complete implementation summary
  * Learnings and outcomes

---

## 12. Limitations

### Known Limitations

* No JWT or token-based authentication
* No password hashing (plaintext for demo purposes)
* No role-based route guarding at backend level
* No pagination for requests or expenses
* No email or notification system

---

### Current Constraints

* Designed for small family use
* Single admin assumption
* Manual role control via login credentials

---

## 13. Future Enhancements

### Planned Improvements

* JWT-based authentication
* Password hashing with bcrypt
* Role-based API authorization
* Request notification system
* Pagination and filters
* Admin CRUD on funds
* Better audit logging

---

### Scalability Plans

* Modular microservice-ready backend
* Redis caching for analytics
* Multi-admin support
* Cloud storage for reports
* Mobile-first UI enhancements

---

## 14. Author & Ownership

### Developer

**V. Dhanush**

### Role

* Full Stack Developer
* System Designer
* Backend Engineer
* Frontend Developer
* Deployment & DevOps

### Contact Information

* GitHub: [https://github.com/VDhanush75](https://github.com/VDhanush75)
* Location: Karnataka, India

---




