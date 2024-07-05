import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './index.css';
import Signup from './pages/Signup.jsx';
import Home from './pages/Home.jsx';  
import About from './pages/About.jsx'; 
import Login from './pages/Login.jsx';
import ResultsList from './pages/ResultsList.jsx';
import Dashboards from './pages/Dashboards.jsx';
import TeacherDashboard from './pages/TeacherDashboard.jsx';
import Nopages from './pages/Nopages.jsx';

import {
    createBrowserRouter,    
    RouterProvider,
} from 'react-router-dom';
import StudentDashboard from './pages/StudentDashboard.jsx';


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
    path: "/dashboards/*",
    element: <Dashboards/>,
  },
  {
    path: "/teacherdashboard",
    element: <TeacherDashboard/>,
  },
  {
    path: "/studentdashboard",
    element: <StudentDashboard/>,
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
    path: "/signup",
    element: <Signup/>,
  },
  {
    path: "/results",
    element: <ResultsList/>,
  },
  {
    path: "*",
    element: <Nopages/>,
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(<RouterProvider router={router} />);
