import Navbar from './components/Navbar.jsx';
import NavLayout from './Layout/NavLayout.jsx';
import { React, useState } from 'react';
import desi from './assets/desi.PNG'

export default function App() {
  const [sidebarToggle, setSidebarToggle] = useState(false);

  return (
    <>
      <div className='flex justify-between'>
        <Navbar
          sidebarTgl={sidebarToggle}
          setSidebarTglD={setSidebarToggle} />

        <div>
          <NavLayout />
        </div>
      </div>
      <div className='flex ' >

        <div className='p-6'>
          <p className='text-4xl pt-8  font-bold'>Learning Bridge </p>
          <p className='text-4xl pt-8 font-bold'>Student Managment System</p>
        </div>
        <div className='flex justify-center w-full h-full p-8 px-2'>
          <img src={desi} alt='bg' />
        </div>

      </div>

    </>
  );
}
