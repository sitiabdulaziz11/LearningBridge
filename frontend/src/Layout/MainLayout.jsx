import React from 'react'

function MainLayout({children}) {
  return (
    <div>
        {/* <Navbar /> */}
        <h2>{children}</h2>
    </div>
  )
}

export default MainLayout
