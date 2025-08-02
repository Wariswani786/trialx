import { useState } from "react";
import api from "../api/api";
import { motion } from "framer-motion";

function AddTrial() {
  const [title, setTitle] = useState("");
  const [inclusion, setInclusion] = useState("");
  const [exclusion, setExclusion] = useState("");
  const [location, setLocation] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async () => {
    try {
      const res = await api.post("/trials/", {
        title,
        inclusion_criteria: inclusion,
        exclusion_criteria: exclusion,
        location,
      });
      if (res.status === 201) {
        setMessage("✅ Trial added successfully!");
        setTitle("");
        setInclusion("");
        setExclusion("");
        setLocation("");
      }
    } catch (err) {
      setMessage("❌ " + (err.response?.data?.detail || "Error adding trial."));
    }
  };

  return (
    <motion.div
      className="max-w-2xl mx-auto mt-16 bg-white dark:bg-gray-900 text-black dark:text-white shadow-lg rounded-xl p-6"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      <h2 className="text-2xl font-bold text-indigo-700 dark:text-indigo-300 mb-6 text-center">
        Add Trial - Admin Panel
      </h2>

      <div className="space-y-4">
        <input
          type="text"
          placeholder="Trial Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="w-full border border-gray-300 dark:border-gray-600 rounded px-3 py-2 bg-white dark:bg-gray-800 text-black dark:text-white"
        />

        <textarea
          placeholder="Inclusion Criteria"
          value={inclusion}
          onChange={(e) => setInclusion(e.target.value)}
          className="w-full border border-gray-300 dark:border-gray-600 rounded px-3 py-2 bg-white dark:bg-gray-800 text-black dark:text-white"
          rows={3}
        />

        <textarea
          placeholder="Exclusion Criteria"
          value={exclusion}
          onChange={(e) => setExclusion(e.target.value)}
          className="w-full border border-gray-300 dark:border-gray-600 rounded px-3 py-2 bg-white dark:bg-gray-800 text-black dark:text-white"
          rows={3}
        />

        <input
          type="text"
          placeholder="Location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          className="w-full border border-gray-300 dark:border-gray-600 rounded px-3 py-2 bg-white dark:bg-gray-800 text-black dark:text-white"
        />

        <button
          onClick={handleSubmit}
          className="w-full bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded transition"
        >
          Add Trial
        </button>

        {message && (
          <p className="text-sm mt-4 text-center text-red-500 dark:text-red-400">{message}</p>
        )}
      </div>
    </motion.div>
  );
}

export default AddTrial;
