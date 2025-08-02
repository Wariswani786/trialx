import { motion } from "framer-motion";
import { Link } from "react-router-dom";

function Home() {
  return (
    <motion.div
      className="min-h-screen bg-gradient-to-br from-blue-100 to-purple-200 dark:from-gray-900 dark:to-gray-800 flex flex-col justify-center items-center text-center px-4"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.6 }}
    >
      <h1 className="text-5xl md:text-6xl font-extrabold text-purple-800 dark:text-purple-300 mb-6">
        Welcome to Clinical Trials
      </h1>

      <p className="max-w-3xl text-lg md:text-xl text-gray-800 dark:text-gray-200 leading-relaxed">
        Our platform helps patients discover clinical trials they are eligible for and allows researchers to reach the right participants faster. 
        By matching health profiles with ongoing trials, we simplify participation and improve access to cutting-edge treatments. 
        Join us in advancing medical research and improving lives through smarter trial connections.
      </p>

      <p className="mt-6 text-md text-purple-700 dark:text-purple-400 font-semibold">
        Click below to register and get started.
      </p>

      <div className="mt-8">
        <Link
          to="/register"
          className="inline-block bg-purple-600 hover:bg-purple-700 text-white font-semibold px-6 py-3 rounded-xl text-lg transition"
        >
          📝 Register Now
        </Link>
      </div>
    </motion.div>
  );
}

export default Home;
