import React, { useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

const Login = () => {
  const [userType, setUserType] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [isLoggedIn, setIsLoggedIn] = useState(false); // State for login status

  const handleLogin = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post("http://localhost:5000/api/v1/login", {
        email,
        password,
      });

      localStorage.setItem("token", response.data.token);
      setIsLoggedIn(true); // Set login status to true
    } catch (error) {
      console.error(error);
    }
  };

  if (isLoggedIn) {
    switch (userType) {
      case "admin":
        return <Link to="/admin-dashboard" />;
      case "teacher":
        return <Link to="/teacher-dashboard" />;
      case "parent":
        return <Link to="/parent-dashboard" />;
      case "student":
        return <Link to="/student-dashboard" />;
      default:
        return <Link to="/register" />;
    }
  }

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-200">
      <form
        className="m-4 p-6 bg-white rounded shadow-md"
        onSubmit={handleLogin}
      >
        <label className="block mb-2">
          User Type:
          <select
            className="w-full p-2 mt-1 border rounded"
            value={userType}
            onChange={(e) => setUserType(e.target.value)}
            required
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
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>

        <label className="block mb-2">
          Password:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>

        <button
          className="w-full p-2 mt-4 text-white bg-blue-600 rounded cursor-pointer hover:bg-blue-500"
          type="submit"
        >
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;
