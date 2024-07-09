import React, { useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

const initialFormData = {
  userType: "",
  password: "",
  confirmPassword: "",
  email: "",
  name: "",
  phoneNo: "",
  firstname: "",
  middlename: "",
  lastname: "",
  mother_first_name: "",
  birthDate: "",
  imageFile: "",
  age: "",
  address: "",
  section: "",
  grade: "",
  hireDate: "",
};

const Signup = () => {
  const [formData, setFormData] = useState(initialFormData);
  const [isRegistered, setIsRegistered] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSignup = async (event) => {
    event.preventDefault();

    // Validation and data handling
    if (formData.password !== formData.confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    if (
      (formData.userType === "admin" || formData.userType === "teacher" || formData.userType === "parent") &&
      !formData.phoneNo
    ) {
      alert("Phone number is mandatory for Admin, Teacher, and Parent");
      return;
    }

    const userData = {
      ...formData,
      section: (formData.userType === "teacher" || formData.userType === "student") ? formData.section : undefined,
      grade: (formData.userType === "student") ? formData.grade : undefined,
      hireDate: (formData.userType === "admin" || formData.userType === "teacher") ? formData.hireDate : undefined,
      mother_first_name: (formData.userType === "parent") ? formData. mother_first_name : undefined,
      mother_middle_name: (formData.userType === "parent") ? formData.mother_middle_name : undefined,
      mother_last_name: (formData.userType === "parent") ? formData.mother_last_name : undefined,
      motherPhNo: (formData.userType === "parent") ? formData.motherPhNo : undefined,
    };

    try {
      const response = await axios.post("/api/v1/students", userData);
      if (response.status === 201) {
        setIsRegistered(true);
      }
    } catch (error) {
      console.error("There was an error registering!", error);
    }
  };

  if (isRegistered) {
    return <Link to="/login" />;
  }

  return (
    <div className="flex items-center w-full justify-center min-h-screen bg-gray-200">
      <form className="m-4 p-6 bg-white rounded shadow-md" onSubmit={handleSignup}>
        <label className="block mb-2">
          Name:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
          />
        </label>
        <label className="block mb-2">
          User Type:
          <select
            className="w-full p-2 mt-1 border rounded"
            name="userType"
            value={formData.userType}
            onChange={handleChange}
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
            name="email"
            value={formData.email}
            onChange={handleChange}
          />
        </label>
        <label className="block mb-2">
          Phone Number:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="text"
            name="phoneNo"
            value={formData.phoneNo}
            onChange={handleChange}
          />
        </label>
        <label className="block mb-2">
          First Name:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="text"
            name="firstname"
            value={formData.firstname}
            onChange={handleChange}
          />
        </label>
        <label className="block mb-2">
          Middle Name:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="text"
            name="middlename"
            value={formData.middlename}
            onChange={handleChange}
          />
        </label>
        <label className="block mb-2">
          Last Name:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="text"
            name="lastname"
            value={formData.lastname}
            onChange={handleChange}
          />
        </label>
        <label className="block mb-2">
          Birth Date:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="date"
            name="birthDate"
            value={formData.birthDate}
            onChange={handleChange}
          />
        </label>
        <label className="block mb-2">
          Image File:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="file"
            name="imageFile"
            onChange={(e) => setFormData({ ...formData, imageFile: e.target.files[0] })}
          />
        </label>
        <label className="block mb-2">
          Age:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="number"
            name="age"
            value={formData.age}
            onChange={handleChange}
          />
        </label>
        <label className="block mb-2">
          Address:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="text"
            name="address"
            value={formData.address}
            onChange={handleChange}
          />
        </label>
        {(formData.userType === "teacher" || formData.userType === "student") && (
          <label className="block mb-2">
            Section:
            <input
              className="w-full p-2 mt-1 border rounded"
              type="text"
              name="section"
              value={formData.section}
              onChange={handleChange}
            />
          </label>
        )}
        {formData.userType === "student" && (
          <label className="block mb-2">
            Grade:
            <input
              className="w-full p-2 mt-1 border rounded"
              type="text"
              name="grade"
              value={formData.grade}
              onChange={handleChange}
            />
          </label>
        )}
        {(formData.userType === "admin" || formData.userType === "teacher") && (
          <label className="block mb-2">
            Hire Date:
            <input
              className="w-full p-2 mt-1 border rounded"
              type="date"
              name="hireDate"
              value={formData.hireDate}
              onChange={handleChange}
            />
          </label>
        )}
        <label className="block mb-2">
          Password:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
          />
        </label>
        <label className="block mb-2">
          Confirm Password:
          <input
            className="w-full p-2 mt-1 border rounded"
            type="password"
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleChange}
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
