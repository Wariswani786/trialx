import { useState } from "react";
import api from "../api/api";
import { motion } from "framer-motion";

function Bookmarks() {
  const [bookmarks, setBookmarks] = useState([]);
  const [trialIdAdd, setTrialIdAdd] = useState("");
  const [trialIdRemove, setTrialIdRemove] = useState("");
  const [messageAdd, setMessageAdd] = useState("");
  const [messageRemove, setMessageRemove] = useState("");
  const [showBookmarks, setShowBookmarks] = useState(false);

  const fetchBookmarks = async () => {
    try {
      const res = await api.get("/bookmarks/");
      if (res.status === 200) {
        setBookmarks(res.data.filter((b) => b.trial));
      } else {
        setBookmarks([]);
      }
    } catch {
      setBookmarks([]);
    }
  };

  const handleAddBookmark = async () => {
    setMessageAdd("");
    try {
      const id = parseInt(trialIdAdd);
      if (!id) return setMessageAdd("Invalid Trial ID");

      const res = await api.post(`/bookmarks/${id}/toggle/`);
      if (res.status === 200) {
        setMessageAdd(`✅ Bookmark added for trial ID ${id}`);
        setTrialIdAdd("");
      } else {
        setMessageAdd("❌ Error adding bookmark.");
      }
    } catch {
      setMessageAdd("❌ Server error while adding bookmark.");
    }
  };

  const handleRemoveBookmark = async () => {
    setMessageRemove("");
    try {
      const id = parseInt(trialIdRemove);
      if (!id) return setMessageRemove("Invalid Trial ID");

      const res = await api.post(`/bookmarks/${id}/toggle/`);
      if (res.status === 200) {
        setMessageRemove(`✅ Bookmark removed for trial ID ${id}`);
        setTrialIdRemove("");
      } else {
        setMessageRemove("❌ Error removing bookmark.");
      }
    } catch {
      setMessageRemove("❌ Server error while removing bookmark.");
    }
  };

  const handleShowBookmarks = () => {
    fetchBookmarks();
    setShowBookmarks(true);
  };

  return (
    <motion.div
      className="max-w-4xl mx-auto mt-10 p-4 bg-white dark:bg-gray-900 text-black dark:text-white rounded-xl shadow-md"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      <h2 className="text-2xl font-bold text-pink-700 dark:text-pink-300 mb-8 text-center">Bookmarks</h2>

      {/* Add Bookmark Section */}
      <div className="mb-6">
        <h3 className="text-lg font-semibold text-pink-600 dark:text-pink-300 mb-2">➕ Add Bookmark</h3>
        <div className="flex items-center gap-4">
          <input
            type="number"
            placeholder="Trial ID"
            value={trialIdAdd}
            onChange={(e) => setTrialIdAdd(e.target.value)}
            className="border border-gray-300 dark:border-gray-600 dark:bg-gray-800 dark:text-white rounded px-3 py-2 w-48"
          />
          <button
            onClick={handleAddBookmark}
            className="bg-pink-600 text-white px-4 py-2 rounded hover:bg-pink-700 transition"
          >
            Add
          </button>
        </div>
        {messageAdd && <p className="text-sm mt-2 text-red-500 dark:text-red-400">{messageAdd}</p>}
      </div>

      {/* Remove Bookmark Section */}
      <div className="mb-6">
        <h3 className="text-lg font-semibold text-pink-600 dark:text-pink-300 mb-2">❌ Remove Bookmark</h3>
        <div className="flex items-center gap-4">
          <input
            type="number"
            placeholder="Trial ID"
            value={trialIdRemove}
            onChange={(e) => setTrialIdRemove(e.target.value)}
            className="border border-gray-300 dark:border-gray-600 dark:bg-gray-800 dark:text-white rounded px-3 py-2 w-48"
          />
          <button
            onClick={handleRemoveBookmark}
            className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700 transition"
          >
            Remove
          </button>
        </div>
        {messageRemove && <p className="text-sm mt-2 text-red-500 dark:text-red-400">{messageRemove}</p>}
      </div>

      {/* Show Bookmarks Section */}
      <div className="text-center mb-6">
        <button
          onClick={handleShowBookmarks}
          className="bg-purple-600 text-white px-6 py-2 rounded hover:bg-purple-700 transition"
        >
          Show Bookmarks
        </button>
      </div>

      {showBookmarks && bookmarks.length === 0 && (
        <p className="text-center text-gray-600 dark:text-gray-400">No bookmarks found.</p>
      )}

      {showBookmarks && bookmarks.length > 0 && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {bookmarks.map((b) => {
            const t = b.trial;
            return (
              <div
                key={t.id}
                className="bg-white dark:bg-gray-800 text-black dark:text-white shadow rounded-xl p-4 border border-gray-200 dark:border-gray-700 hover:shadow-md transition"
              >
                <h3 className="text-lg font-semibold text-pink-700 dark:text-pink-300">{t.title}</h3>
                <p className="text-sm text-gray-700 dark:text-gray-300">📍 Location: {t.location}</p>
                <p className="text-sm mt-2">
                  <span className="font-semibold">✅ Inclusion:</span> {t.inclusion_criteria}
                </p>
                <p className="text-sm">
                  <span className="font-semibold">❌ Exclusion:</span> {t.exclusion_criteria}
                </p>
                <p className="text-xs text-gray-500 dark:text-gray-400 mt-2">Trial ID: {t.id}</p>
              </div>
            );
          })}
        </div>
      )}
    </motion.div>
  );
}

export default Bookmarks;
