import { React, useState } from "react";


const Navbar = () => {

  return (

    <nav className='w-full  bg-gray-950 '>
      <div className='flex justify-between px-4 pt-12'>
        <div className="" >
          {/* <FaBars onClick={() => setSidebarTglD(!sidebarTgl)} /> */}
          <span className="text-white sm:2xl lg:text-3xl lg:ml-3 font-bold ">
            Learning Bridge
          </span>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
