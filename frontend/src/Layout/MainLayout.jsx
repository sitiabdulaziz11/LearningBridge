import React from 'react'
import Navbar from '../components/Navbar'

function MainLayout({children}) {
  return (
    <div>
        {/* <Navbar /> */}
        <h2>{children}</h2>
    </div>
  )
}

export default MainLayout
