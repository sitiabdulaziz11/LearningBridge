
<TopSide
    isSidebarOpen={sidebarToggle}
    setSidebarTgl={setSidebarToggle}
/>
                </div >
    {/* sidebar component */ }
    < Sidebar isSidebarOpen = { sidebarToggle } />



// return (
//     <>
//         <div className='flex bg-slate-600'>
//             <div className={`${isSidebarOpen ? "hidden" : "block"} sm:w-[13.5rem] lg:w-[19.25rem] bg-gray-950 fixed h-full px-4 py-2`}>
//                 <div className='my-2 mb-4'>
//                     <h1 className='text-2xl text-white font-bold'>Dashboard</h1>
//                 </div>
//                 <hr />
//                 <ul className='mt-3 text-2xl text-zinc-300 font-bold'>
//                     <li className='mb-2 hover:bg-blue-950 py-2'>
//                         <Link to='/teacherdashboard' className='px-3'>
//                             Teacher Dashboard
//                         </Link>
//                     </li>
//                     <li className='mb-2 hover:bg-blue-950 py-2'>
//                         <a href='' className='px-3'>
//                             Student Dashboard
//                         </a>
//                     </li>
//                 </ul>
//             </div>

//             {/* hamburger for meddel device */}
//             <nav className='p-4 w-full bg-slate-600 ml-[22rem]'>
//                 <div className='flex items-center text-xl'>
//                     {isOpen ? (
//                         <FaTimes
//                             className='text-white sm:h-5 sm:w-5 lg:h-7 lg:w-7 me-4 cursor-pointer'
//                             onClick={toggleMenu1}
//                         />
//                     ) : (
//                         <FaBars
//                             className='text-white sm:h-5 sm:w-5 lg:h-7 lg:w-7 me-4 cursor-pointer'
//                             onClick={toggleMenu1}
//                         />
//                     )}

//                     <span className='text-white sm:2xl lg:text-3xl lg:ml-3 font-bold '>Learning Bridge</span>
//                 </div>
//             </nav>
//         </div>
//     </>

// )