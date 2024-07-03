import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import PrivateRoute from "./components/PrivateRoute.jsx";
import Dashboard from "./components/Dashboard.jsx";
import { Login } from "./components/Login.jsx";
import MainLayout from "./components/MainLayout.jsx";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Dashboard />} />
        <Route
          path="/"
          element={
            <PrivateRoute>
              <MainLayout />
            </PrivateRoute>
          }
        >
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/settings" element={<Navigate to="/dashboard" />} />
        </Route>
      </Routes>
    </Router>
  );
};

export default App;
