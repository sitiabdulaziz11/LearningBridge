import Dashboard from "./components/Dashboard.jsx";
import Sidebar from "./components/Sidebar.jsx";
import { useState } from "react";
import Nav from "./components/Nav.jsx";

export default function App() {
  const [sidebarToggle, setSidebarToggle] = useState(false);
  return (
    <>
      {/* <Nav /> */}
      <div className="flex bg-gray-950">
        <Sidebar isSidebarOpen={sidebarToggle} />
        <Dashboard
          isSidebarOpen={sidebarToggle}
          setSidebarTgl={setSidebarToggle}
        />
      </div>
    </>
  );
}
