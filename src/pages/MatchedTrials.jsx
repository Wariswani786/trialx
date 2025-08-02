import { useState } from "react";
import api from "../api/api";
import { motion } from "framer-motion";

function MatchedTrials() {
  const [trials, setTrials] = useState([]);
  const [error, setError] = useState("");

  const handleFetch = async () => {
    setError("");
    setTrials([]);

    try {
      const res = await api.get("/match-trials/");
      if (res.status === 200) {
        if (res.data.length === 0) {
          setError("No matched trials found.");
        } else {
          setTrials(res.data);
        }
      }
    } catch (err) {
      setError("Error fetching matched trials.");
    }
  };

  return (
    <motion.div
      className="max-w-4xl mx-auto mt-10 p-4 bg-white dark:bg-gray-900 text-black dark:text-white rounded-xl shadow-md"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      <h2 className="text-2xl font-bold text-green-700 dark:text-green-300 mb-6 text-center">
        Matched Clinical Trials
      </h2>

      <div className="text-center mb-6">
        <button
          onClick={handleFetch}
          className="bg-green-600 hover:bg-green-700 text-white px-6 py-2 rounded-xl transition"
        >
          Show Matched Trials
        </button>
      </div>

      {error && <p className="text-red-600 dark:text-red-400 text-center">{error}</p>}

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {trials.map((trial) => (
          <div
            key={trial.id}
            className="bg-white dark:bg-gray-800 shadow rounded-xl p-4 border border-gray-200 dark:border-gray-700 hover:shadow-md transition"
          >
            <h3 className="text-lg font-semibold text-green-700 dark:text-green-300">
              {trial.title}
            </h3>
            <p className="text-sm text-gray-700 dark:text-gray-300">
              📍 Location: {trial.location}
            </p>
            <p className="text-sm mt-2">
              <span className="font-semibold">✅ Inclusion:</span> {trial.inclusion_criteria}
            </p>
            <p className="text-sm">
              <span className="font-semibold">❌ Exclusion:</span> {trial.exclusion_criteria}
            </p>
            <p className="text-xs text-gray-500 dark:text-gray-400 mt-2">Trial ID: {trial.id}</p>
          </div>
        ))}
      </div>
    </motion.div>
  );
}

export default MatchedTrials;

