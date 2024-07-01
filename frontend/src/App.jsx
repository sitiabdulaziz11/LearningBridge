
import Dashboard from './components/Dashboard.jsx';
import Sidebar from './components/Sidebar.jsx';
import { useState } from 'react';

export default function App() {
  const [sidebarToggle, setSidebarToggle] = useState(false)
  return (
    <div className='flex bg-gray-950'>
      <Sidebar isSidebarOpen={sidebarToggle}/>
      <Dashboard 
      isSidebarOpen={sidebarToggle}
      setSidebarTgl={setSidebarToggle}
      />
    </div>
  );
}
