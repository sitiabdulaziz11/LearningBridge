import { BrowserRouter, Routes, Route } from 'react-router-dom';
import About from './pages/About.jsx';
import Home from './pages/Home.jsx';
import Dashboard from './components/Dashboard.jsx';
import Sidebar from './components/Sidebar.jsx';
import { useState } from 'react';

export default function App() {
  const [sidebarToggle, setSidebarToggle] = useState(false)
  return (
    <>
      <div className='flex bg-gray-950'>
        <Sidebar isSidebarOpen={sidebarToggle}/>
        <Dashboard 
        isSidebarOpen={sidebarToggle}
        setSidebarTgl={setSidebarToggle}/>
      </div>

      {/* <div>
        <BrowserRouter>
          <Routes>
            <Route index element={<Home />} />
            <Route path="/home" element={<Home />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </BrowserRouter>
      </div>*/}
    </>
    
  );
}
