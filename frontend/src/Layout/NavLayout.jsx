import { React, useState } from 'react'
import { Link } from "react-router-dom";
import { FaBars, FaBell, FaSearch, FaUserCircle, FaTimes } from 'react-icons/fa'

const NavLayout = () => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    const toggleMenu = () => {
        setIsMenuOpen(!isMenuOpen); // !false = true
    };

    return (
        <>
            <nav className='w-full p-4  bg-gray-950'>
                <div className='flex justify-between px-4 py-6'>
                    {/* Navbar links for medium and larger devices */}
                    <div>
                        <ul className='hidden md:flex space-x-7 text-zinc-200 font-bold text-2xl'>
                            <li className='py-2 px-6'><Link to="/home">Home</Link></li>
                            <li className='py-2 px-6'><Link to="/dashboards/*">Dashboards</Link></li>
                            <li className='py-2 px-6'><Link to="/about">About</Link></li>
                            <li className='py-2 px-6'><Link to="/login">Login</Link></li>
                            <li className='py-2 px-6'><Link to="/signup">Signup</Link></li>
                        </ul>
                    </div>

                    {/* hamburger icon for small device */}
                    <div className='md:hidden flex items-center text-xl mr-12 p-4'>
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
                {/* Dropdown menu for small devices */}
                {isMenuOpen ? (
                    <ul className='flex-col md:hidden font-bold text-2xl text-zinc-200'>
                        <li className='py-6 '><Link to="/home">Home</Link></li>
                        <li className='py-6 '><Link to="/dashboards">Dashboards</Link></li>
                        <li className='py-6 '><Link to="/about">About</Link></li>
                        <li className='py-6 '><Link to="/login">Login</Link></li>
                        <li className='py-6 '><Link to="/result">Resu</Link></li>
                    </ul>
                ) : null}
            </nav>

        </>
    )
}

export default NavLayout
