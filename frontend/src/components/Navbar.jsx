import { React, useState } from 'react'
import { FaBars, FaBell, FaSearch, FaUserCircle, FaTimes } from 'react-icons/fa'
import { Link } from "react-router-dom";


const Navbar = ({ sidebarTgl, setSidebarTglD }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu1 = () => {
    setIsOpen(!isOpen);
    setSidebarTglD(!sidebarTgl);
  };

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen); // !false = true
  };

  return (
    <nav className='p-4'>
      <div className='px-4 py-7 flex justify-between'>

        {/* hamburger for meddel device */}
        <div className='flex items-center text-xl'>
          {isOpen ? (
            <FaTimes
              className='text-white sm:h-5 sm:w-5 lg:h-7 lg:w-7 me-4 cursor-pointer'
              onClick={toggleMenu1}
            />
          ) : (
            <FaBars
              className='text-white sm:h-5 sm:w-5 lg:h-7 lg:w-7 me-4 cursor-pointer'
              onClick={toggleMenu1}
            />
          )}

          {/* <FaBars onClick={() => setSidebarTglD(!sidebarTgl)} /> */}
          <span className='text-white sm:2xl lg:text-3xl lg:ml-3 font-bold '>Learning Bridge</span>
        </div>

        {/* hamburger icon for small device */}
        <div className='md:hidden flex items-center text-xl'>
          {isMenuOpen ? (
            <FaTimes
              className='text-white sm:h-5 sm:w-5 lg:h-7 lg:w-7 me-4 cursor-pointer'
              onClick={toggleMenu}
            />
          ) : (
            <FaBars
              className='text-white sm:h-5 sm:w-5 lg:h-7 lg:w-7 me-4 cursor-pointer'
              onClick={toggleMenu}
            />
          )}
        </div>

        {/* navbar for middle device */}
        <div>
          <ul className='hidden md:flex space-x-7 text-zinc-200 font-bold text-2xl'>
            <li className='py-2 px-6'><Link to="/home">Home</Link></li>
            <li className='py-2 px-6'><Link to="/dashboard">Dashboards</Link></li>
            <li className='py-2 px-6'><Link to="/about">About</Link></li>
            <li className='py-2 px-6'><Link to="/login">Login</Link></li>
          </ul>
        </div>

        {/* search bar for middle device */}
        <div className='flex items-center gap-x-5'>
          <div className='relative md:w-65'>
            <span className='relative md:absolute inset-y-0 left-0 flex items-center pl-2'><button className='p-1 focus:outline-none text-white md:text-black'><FaSearch /></button></span>
            <input type="text" className='w-full px-4 py-1 pl-12 rounded shadow outline-none hidden md:block' />
          </div>

          {/* bell for meddle device */}
          <div className='text-white'><FaBell className='w-6 h-6' /></div>

          {/* profile for meddle device */}
          <div className='relative'>
            <button className='text-white group'>
              <FaUserCircle className='w-8 h-8 mt-1' />
              <div className='z-10 hidden absolute bg-white rouded-lg shadow w-32 group-focus:block top-full right-0'>
                <ul className='py-2 text-sm text-gray-800'>
                  <li><a href="">Profile</a></li>
                  <li><a href="">Setting</a></li>
                  <li><a href="">Log out</a></li>
                </ul>
              </div>
            </button>
          </div>
        </div>
      </div>

      {/* navbar for small device */}
      {isMenuOpen ? (
        <ul className='flex-col md:hidden text-semibold text-2xl text-zinc-200 inset-0 p-8'>
          <li className='py-6 px-6'><Link to="/home">Home</Link></li>
          <li className='py-2 px-6'><Link to="/dashboards">Dashboards</Link></li>
          <li className='py-6 px-6'><Link to="/about">About</Link></li>
          <li className='py-6 px-6'><Link to="/login">Login</Link></li>
        </ul>
      ) : null}
    </nav>
  );
};

export default Navbar
