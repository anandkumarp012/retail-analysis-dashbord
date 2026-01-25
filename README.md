# Retail-Dashboard: AI Inventory Forecasting System

A comprehensive retail management system featuring AI-powered demand forecasting, inventory optimization, and sales analytics. Built with **FastAPI** (Backend) and **React** (Frontend).

## 🚀 Getting Started

If you have received this project, follow these steps to set it up and run it on your local machine.

### Prerequisites

Ensure you have the following installed:
- **Python 3.8+**
- **Node.js (v18 or higher)** & **npm**
- **MongoDB** (Running locally on `mongodb://localhost:27017`)

---

## 🛠️ Backend Setup (FastAPI)

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:** `venv\Scripts\activate`
   - **macOS/Linux:** `source venv/bin/activate`

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the backend server:**
   ```bash
   python -m uvicorn main:app --reload
   ```
   The backend will be available at `http://127.0.0.1:8000`.

---

## 💻 Frontend Setup (React + Vite)

1. **Open a new terminal and navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the development server:**
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:5173`.

---

## 📂 Project Structure

- `backend/`: FastAPI application, ML engine (Prophet/XGBoost), and database models.
- `frontend/`: React application with Tailwind CSS and Recharts.
- `backend/main.py`: Main entry point for the API.
- `backend/ml_engine.py`: AI logic for demand forecasting.

## 📊 Database Configuration

By default, the application connects to a local MongoDB instance:
- **URL**: `mongodb://localhost:27017`
- **Database Name**: `retail_dashboard`

You can customize these by creating a `.env` file in the `backend/` directory:
```env
MONGO_URL=mongodb://localhost:27017
DATABASE_NAME=retail_dashboard
```

## 📝 Usage

1. **Login**: Use default credentials or sign up.
2. **Upload Data**: Go to the "Upload Data" section and upload a CSV with sales history (SKU, Date, Quantity).
3. **Forecast**: The AI will automatically process the data and generate forecasts.
4. **Dashboard**: View trends, KPIs, and inventory risk alerts.
