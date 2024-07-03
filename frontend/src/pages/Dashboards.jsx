import { FaBars, FaBell, FaSearch, FaUserCircle, FaTimes } from 'react-icons/fa'
import Sidebar from '../components/Sidebar.jsx';
import { React, useState } from 'react';
import NavLayout from '../Layout/NavLayout.jsx';

const Dashboards = () => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleMenu1 = () => {
        setIsOpen(!isOpen);
    };

    return (
        <>
            {/* sidebar component */}
            <Sidebar isSidebarOpen={isOpen} />

            <div className='w-full bg-gray-950 '>
                <div className={`flex justify-between text-xl ${isOpen ? '' : 'sm:ml-[15rem] lg:ml-[22rem]'}`} >
                    <div className='pt-12'> {/*solved 2 hamberger overlap and one move to top issue */}
                        {/* hamburger for meddel device */}
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
                    </div>
                    <div className='pt-11 '>
                        <span className='text-white sm:2xl lg:text-3xl lg:ml-3 font-bold '>Learning Bridge</span>
                    </div>
                    <div>
                        {/* top side component */}
                        <NavLayout />
                    </div>
                </div>
            </div>
        </>
    );

}

export default Dashboards
