<<<<<<< HEAD
import ReactDOM from "react-dom/client";

import App from "./App.jsx";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
=======
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import Home from './pages/Home.jsx';  
import About from './pages/About.jsx'; 
import Login from './pages/Login.jsx';
import Dashboards from './pages/Dashboards.jsx';

import Nopages from './pages/Nopages.jsx';

import './index.css';

import {
    createBrowserRouter,    
    RouterProvider,
} from 'react-router-dom';


const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/home",
    element: <Home/>,
  },
  {
    path: "/dashboards",
    element: <Dashboards/>,
  },
  {
    path: "/about",
    element: <About/>,
  },
  {
    path: "/login",
    element: <Login/>,
  },
  {
    path: "*",
    element: <Nopages/>,
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(<RouterProvider router={router} />);
>>>>>>> 8dbcca62d84bd0c3a7b66c5f008b0e9f6f7e0716
