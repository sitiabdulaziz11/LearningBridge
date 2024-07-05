import {React, useState} from 'react'
import StudentResultForm from './StudentResultForm.jsx'

const ParentComponent = () => {
    const [message, setMessage] = useState('');

    const handleSave = (savedData) => {
        console.log('Saved student result:', savedData);
        setMessage('Result uploaded successfully');
        // Optionally update state, refresh data, etc.
    };

    return (
        <>
            <div className="w-full justify-center min-h-screen bg-gray-200">
                <h1 className="text-3xl text-center mt-10">Student Result Form</h1>
                {message && <div className="mb-4 text-center text-xl text-green-500">{message}</div>}
                <StudentResultForm onSave={handleSave} />
            </div>
        </>
    )
}

export default ParentComponent;
