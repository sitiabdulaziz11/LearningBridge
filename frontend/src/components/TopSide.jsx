import { React, useState } from 'react'
import Navbar from './Navbar.jsx'
import { FaBars, FaBell, FaSearch, FaUserCircle, FaTimes } from 'react-icons/fa'


const TopSide = ({isSidebarOpen, setSidebarTgl}) => {
  
  return (
    <div className=''>
      <Navbar
      sidebarTgl={isSidebarOpen}
      setSidebarTglD={setSidebarTgl}/>
      
    </div>
  )
}

export default TopSide
