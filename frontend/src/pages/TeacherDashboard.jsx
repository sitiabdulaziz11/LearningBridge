import React from 'react'
import NavLayout from '../Layout/NavLayout'
import Navbar from '../components/Navbar'
import StudentResultForm from '../components/TopSide.jsx'


const TeacherDashboard = () => {
    return (
        <>
            <div className='flex'>
                <Navbar />
                <NavLayout />
            </div>

            <div className='m-10 p-20 text-gray-50 '>
               <StudentResultForm /> 
            </div>     
        </>
    )
}

export default TeacherDashboard
