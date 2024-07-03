<<<<<<< HEAD
import React from "react";
import Navbar from "./Navbar.jsx";
const Dashboard = () => {
  return (
    <div className="w-full">
      <Navbar />
=======
import React from 'react'
import Navbar from './Navbar.jsx'

const Dashboard = ({isSidebarOpen, setSidebarTgl}) => {
  return (
    <div className={`w-full ${isSidebarOpen ? '' : 'sm:ml-[13rem] lg:ml-[22rem]'}`}>
      <Navbar
      sidebarTgl={isSidebarOpen}
      setSidebarTglD={setSidebarTgl}/>
>>>>>>> 8dbcca62d84bd0c3a7b66c5f008b0e9f6f7e0716
    </div>
  );
};

export default Dashboard;
