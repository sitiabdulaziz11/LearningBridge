import React from "react";
import Navbar from "./Navbar.jsx";

const Dashboard = ({ isSidebarOpen, setSidebarTgl }) => {
  return (
    <div
      className={`w-full ${isSidebarOpen ? "" : "sm:ml-[13rem] lg:ml-[22rem]"}`}
    >
      <Navbar sidebarTgl={isSidebarOpen} setSidebarTglD={setSidebarTgl} />
    </div>
  );
};

export default Dashboard;
