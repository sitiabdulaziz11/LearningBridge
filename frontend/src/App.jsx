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

<<<<<<< HEAD
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
=======
import Dashboard from './components/Dashboard.jsx';
import Sidebar from './components/Sidebar.jsx';
import { useState } from 'react';

import Nav from './components/Nav.jsx';

export default function App() {
  const [sidebarToggle, setSidebarToggle] = useState(false)
  return (
    <>
      {/* <Nav /> */}
      <div className='flex bg-gray-950'>
        <Sidebar isSidebarOpen={sidebarToggle}/>
        <Dashboard 
        isSidebarOpen={sidebarToggle}
        setSidebarTgl={setSidebarToggle}/>
      </div>

    </>
>>>>>>> 8dbcca62d84bd0c3a7b66c5f008b0e9f6f7e0716
  );
};

export default App;
