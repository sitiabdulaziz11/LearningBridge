import Navbar from './components/Navbar.jsx';
import NavLayout from './Layout/NavLayout.jsx';
import { React, useState } from 'react';
import desi from './assets/desi.PNG'
import { Link } from "react-router-dom";

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
      <h1 className='text-5xl pt-6 ml-20 font-bold'>Welcom to Learning Bridge <span className='text-6xl'>E-</span>Learing</h1>

      <div className='flex'>
        <div className='w-3/6 p-20'>
          <h1 className='text-4xl font-bold'>Student Managment System</h1>
          <h1 className='text-4xl pt-10  font-bold'>Your Partner in Your Child's Educational Journey!</h1>
          <h1 className='text-4xl pt-10  font-bold pb-10'>Join Today – Simplifying Teaching and Learning for Parents, Teachers, and Students.</h1>

          <Link to="/signup">
            <button className='bg-purple-950 hover:bg-blue-700 mt-10 text-white font-bold py-6 px-10 mb-20 rounded '>Get Started</button>
          </Link>
        </div>
        <div className='flex justify-end w-full h-full p-8 px-2'>
          <img className='ml-80 pr-20' src={desi} alt='bg' />
        </div>
      </div>
      <div className='bg-gray-900 pt-20 pl-20 text-white'>
        <h2 className='text-3xl mb-10'>Features</h2>
        <p className='text-2xl ml-5 mb-10'>Track Your Child's Progress with Real-Time Updates and Personalized Insights.</p>

        <p className='text-2xl ml-5 mb-10'>Stay Informed and Involved in Your Child's Education – Anytime, Anywhere.</p>

        <p className='text-2xl ml-5 pb-20'>Empowering Students to Achieve Their Best, One Step at a Time.</p>
      </div>
    </>
  );
}
