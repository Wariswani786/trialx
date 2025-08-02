function Footer() {
  return (
    <footer className="bg-pink-50 border-t mt-10 py-4">
      <div className="text-center text-sm text-gray-600">
        © {new Date().getFullYear()} ClinicalTrials — Designed with ❤️ to empower patients & researchers.
      </div>
    </footer>
  );
}

export default Footer;
