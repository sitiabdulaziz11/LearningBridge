import React from 'react'
import {FaHome} from 'react-icons/fa'

const Sidebar = ({isSidebarOpen}) => {
 
  return (
    <div className={`${isSidebarOpen ? "hidden" : "block"} sm:w-[13.5rem] lg:w-[19.25rem] bg-gray-950 fixed h-full px-4 py-2`}>
      <div className='my-2 mb-4'>
        <h1 className='text-2xl text-white font-bold'>Dashboard</h1>
      </div>
      <hr />
      <ul className='mt-3 text-2xl text-zinc-300 font-bold'>
        <li className='mb-2 hover:bg-blue-950 py-2'>
          <a href='' className='px-3'>
            Teacher Dashboard
          </a>
        </li>
        <li className='mb-2 hover:bg-blue-950 py-2'>
          <a href='' className='px-3'>
            Student Dashboard
          </a>
        </li>
      </ul>
      
    </div>
  )
}

export default Sidebar
