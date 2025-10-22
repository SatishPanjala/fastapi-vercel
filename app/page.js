"use client";

import { useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("");

  const handleClick = async () => {
    try {
      // Example API call to a placeholder endpoint
      const res = await fetch("/api/hello");
      const data = await res.json();
      setMessage(data.message);
    } catch (err) {
      setMessage("Error fetching data!");
    }
  };

  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
      <h1 className="text-3xl font-bold text-gray-800 mb-6">
        🚀 Next.js + Vercel Sample
      </h1>
      <button
        onClick={handleClick}
        className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
      >
        Click Me
      </button>
      {message && (
        <p className="mt-4 text-lg text-green-700 font-medium">{message}</p>
      )}
    </main>
  );
}
 
