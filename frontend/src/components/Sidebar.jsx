import React from 'react'
import { Link } from "react-router-dom";
import { FaHome } from 'react-icons/fa'

const Sidebar = ({ isSidebarOpen }) => {

  return (
    
    <div className={`${isSidebarOpen ? "hidden" : "block"} sm:w-[13.5rem] lg:w-[19.25rem] bg-gray-950 fixed h-full px-4 py-2`}>
      <div className='my-2 mb-4'>
        <h1 className='text-2xl text-white font-bold'>Dashboard</h1>
      </div>
      <hr />
      <ul className='mt-3 text-xl text-zinc-300 font-semibold'>
        <li className='mb-2 hover:bg-blue-950 py-2'>
          <Link to='/teacherdashboard' className=''>
            Teacher Dashboard
          </Link>
        </li>
        <li className='mb-2 hover:bg-blue-950 py-2'>
          <Link to='/studentdashboard' className=''>
            Student Dashboard
          </Link>
        </li>
        <li className='mb-2 hover:bg-blue-950 py-2'>
          <Link to='' className=''>
            Parent Dashboard
          </Link>
        </li>
        <li className='mb-2 hover:bg-blue-950 py-2'>
          <Link to='' className=''>
            Admin Dashboard
          </Link>
        </li>
        <li className='mb-2 hover:bg-blue-950 py-2 '><Link to="/results">Results Dashboard</Link></li>
        <li className='mb-2 hover:bg-blue-950 py-2 '><Link to="">Announcement Dashboard</Link></li>
        <li className='mb-2 hover:bg-blue-950 py-2'><Link to="">Registration Dashboard</Link></li>
      </ul>

    </div>
  )
}

export default Sidebar