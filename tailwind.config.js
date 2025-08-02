// tailwind.config.js
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}", // Include all relevant frontend files
  ],
  darkMode: "class", // ✅ Enables dark mode using the `.dark` class
  theme: {
    extend: {
      colors: {
        primary: "#4f46e5", // Indigo
        secondary: "#14b8a6", // Teal
        background: "#f9fafb", // Light background
        darkBackground: "#0f172a", // Dark mode bg
      },
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui"],
      },
    },
  },
  plugins: [
    require("@tailwindcss/forms"), // optional for form styling
    require("@tailwindcss/typography"), // optional for rich text
  ],
};
