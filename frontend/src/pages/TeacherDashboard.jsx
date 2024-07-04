import React from 'react'
import NavLayout from '../Layout/NavLayout'
import Navbar from '../components/Navbar'
import StudentResultForm from '../components/StudentResultForm.jsx'



const TeacherDashboard = () => {
    return (
        <>
            <div className='flex'>
                <Navbar />
                <NavLayout />
            </div>

            <div className=' '>
               <StudentResultForm /> 
            </div>     
        </>
    )
}

export default TeacherDashboard
