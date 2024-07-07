import { FaBars, FaTimes } from 'react-icons/fa'
import { React, useState } from 'react'
import { Link } from "react-router-dom";
import NavLayout from '../Layout/NavLayout.jsx';

const StudentDashboard = () => {
    const [isOpen, setIsOpen] = useState(false);


    const toggleMenu1 = () => {
        setIsOpen(!isOpen);
    };

    return (
        <>
            <div className={`${isOpen ? "hidden" : ""} sm:w-[13.5rem] lg:w-[19.25rem] bg-gray-950 fixed h-full px-4 py-2`}>
                <div className='my-2 mb-4'>
                    <Link to='/studentdashboard' className=''>
                        <h1 className='text-2xl mt-12 text-white font-bold' >Student Dashboard</h1>
                    </Link>
                </div>
                <hr />
                <ul className='mt-3 text-2xl text-zinc-300 font-bold'>
                    <li className='py-4 hover:bg-blue-950 '>
                        <Link to="/results">Results Dashboard</Link>
                    </li>
                    <li className='hover:bg-blue-950 py-4'>
                        <Link to='' className=''>Attendance Dashboard</Link>
                    </li>
                    <li className='hover:bg-blue-950 py-4'>
                        <Link to='' className=''>
                            Conduct Dashboard
                        </Link>
                    </li>
                </ul>

            </div>
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

    )
}

export default StudentDashboard
