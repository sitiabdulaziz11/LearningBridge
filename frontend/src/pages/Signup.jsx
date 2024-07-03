import React, { useState } from "react";
import { Link } from "react-router-dom";

const Signup = () => {
  const [userType, setUserType] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [isRegistered, setIsRegistered] = useState(false);

  const handleSignup = (event) => {
    event.preventDefault();
    // Here you would typically validate the user and set the registration state
    setIsRegistered(true);
  };

  if (isRegistered) {
    return <Link to="/login" />;
  }

  return (
    <div className="flex items-center w-full justify-center min-h-screen bg-gray-200">
      <form
        className="m-4 p-6 bg-white rounded shadow-md"
        onSubmit={handleSignup}
      >
        <label className="block mb-2">
          Name:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>
        <label className="block mb-2">
          User Type:
          <select
            className="w-full p-2 mt-1 border rounded"
            value={userType}
            onChange={(e) => setUserType(e.target.value)}
          >
            <option value="">Select...</option>
            <option value="admin">Admin</option>
            <option value="teacher">Teacher</option>
            <option value="parent">Parent</option>
            <option value="student">Student</option>
          </select>
        </label>
        <label className="block mb-2">
          Email:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>
        <label className="block mb-2">
          Password:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <label className="block mb-2">
          Confirm Password:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
        </label>
        <input
          className="w-full p-2 mt-4 text-white bg-blue-600 rounded cursor-pointer hover:bg-blue-500"
          type="submit"
          value="Sign Up"
        />
      </form>
    </div>
  );
};

export default Signup;
