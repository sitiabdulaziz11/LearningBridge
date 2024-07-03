import Navbar from './components/Navbar.jsx';
import NavLayout from './Layout/NavLayout.jsx';
import { useState } from 'react';

export default function App() {
  const [sidebarToggle, setSidebarToggle] = useState(false);
  return (
    <>
      <div className='flex justify-between bg-gray-950'>
        <Navbar
          sidebarTgl={sidebarToggle}
          setSidebarTglD={setSidebarToggle} />

        <div>
          <NavLayout />
        </div>
      </div>
      
    </>
  );
}
