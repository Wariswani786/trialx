import { useState } from "react";
import api from "../api/api";
import { motion } from "framer-motion";

function Profile() {
  const [age, setAge] = useState("");
  const [gender, setGender] = useState("");
  const [condition, setCondition] = useState("");
  const [medications, setMedications] = useState("");
  const [message, setMessage] = useState("");
  const [profileExists, setProfileExists] = useState(false);

  const handleLoad = async () => {
    try {
      const res = await api.get("/my-profile/");
      if (res.status === 200 && res.data.age !== null) {
        setProfileExists(true);
        setAge(res.data.age);
        setGender(res.data.gender);
        setCondition(res.data.condition);
        setMedications(res.data.medications);
        setMessage("✅ Profile loaded.");
      } else {
        setMessage("No existing profile found.");
        setProfileExists(false);
      }
    } catch (err) {
      setMessage("❌ Error loading profile.");
    }
  };

  const handleAdd = async () => {
    try {
      const res = await api.post("/my-profile/", {
        age,
        gender,
        condition,
        medications,
      });
      if (res.status === 201) {
        setMessage("✅ Profile added successfully!");
        setProfileExists(true);
      }
    } catch (err) {
      setMessage("❌ " + (err.response?.data?.detail || "Failed to add profile."));
    }
  };

  const handleUpdate = async () => {
    try {
      const res = await api.put("/my-profile/", {
        age,
        gender,
        condition,
        medications,
      });
      if (res.status === 200) {
        setMessage("✅ Profile updated!");
      }
    } catch (err) {
      setMessage("❌ " + (err.response?.data?.detail || "Failed to update profile."));
    }
  };

  return (
    <motion.div
      className="max-w-xl mx-auto mt-16 bg-white dark:bg-gray-900 shadow-lg rounded-xl p-6"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      <h2 className="text-2xl font-bold text-teal-700 dark:text-teal-300 mb-4">My Profile</h2>

      <div className="space-y-4">
        <input
          type="number"
          placeholder="Age"
          value={age}
          onChange={(e) => setAge(e.target.value)}
          className="w-full border dark:bg-gray-800 dark:text-white rounded px-3 py-2"
        />

        <select
          value={gender}
          onChange={(e) => setGender(e.target.value)}
          className="w-full border dark:bg-gray-800 dark:text-white rounded px-3 py-2"
        >
          <option value="">Select Gender</option>
          <option>Male</option>
          <option>Female</option>
          <option>Other</option>
        </select>

        <input
          type="text"
          placeholder="Condition"
          value={condition}
          onChange={(e) => setCondition(e.target.value)}
          className="w-full border dark:bg-gray-800 dark:text-white rounded px-3 py-2"
        />

        <input
          type="text"
          placeholder="Medications"
          value={medications}
          onChange={(e) => setMedications(e.target.value)}
          className="w-full border dark:bg-gray-800 dark:text-white rounded px-3 py-2"
        />

        <div className="flex flex-wrap gap-4">
          <button
            onClick={handleLoad}
            className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600 transition"
          >
            Load Profile
          </button>

          <button
            onClick={handleAdd}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
          >
            Add Profile
          </button>

          <button
            onClick={handleUpdate}
            className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition"
          >
            Update Profile
          </button>
        </div>

        {message && (
          <p className="text-sm mt-4 text-center text-red-500 dark:text-red-400">{message}</p>
        )}
      </div>
    </motion.div>
  );
}

export default Profile;
