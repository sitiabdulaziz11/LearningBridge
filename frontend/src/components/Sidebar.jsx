import React from "react";
import { FaHome } from "react-icons/fa";

const Sidebar = ({isSidebarOpen}) => {
 
  return (
<<<<<<< HEAD
    <div className="w-40 bg-gray-950 fixed h-full px-4 py-2">
      <div className="my-2 mb-4">
        <h1 className="text-2xl text-white font-bold">Dashboard</h1>
      </div>
      <hr />
      <ul className="mt-3 text-2xl text-white font-bold">
        <li className="mb-2 rounded hover:shadow hover:bg-blue-500 py-2">
          <a href="" className="px-3">
            <FaHome className="inline-block w-6 h-6 mr-2 -mt-2"></FaHome>
            Home
          </a>
        </li>
        <li className="mb-2 rounded hover:shadow hover:bg-blue-500 py-2">
          <a href="" className="px-3">
            <FaHome className="inline-block w-6 h-6 mr-2 -mt-2"></FaHome>
            Home
          </a>
        </li>
        <li className="mb-2 rounded hover:shadow hover:bg-blue-500 py-2">
          <a href="" className="px-3">
            <FaHome className="inline-block w-6 h-6 mr-2 -mt-2"></FaHome>
            Home
          </a>
        </li>
        <li className="mb-2 rounded hover:shadow hover:bg-blue-500 py-2">
          <a href="" className="px-3">
            <FaHome className="inline-block w-6 h-6 mr-2 -mt-2"></FaHome>
            Home
          </a>
        </li>
        <li className="mb-2 rounded hover:shadow hover:bg-blue-500 py-2">
          <a href="" className="px-3">
            <FaHome className="inline-block w-6 h-6 mr-2 -mt-2"></FaHome>
            Home
=======
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
>>>>>>> 8dbcca62d84bd0c3a7b66c5f008b0e9f6f7e0716
          </a>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;
