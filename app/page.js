"use client";

import { useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("Click the button to fetch data");
  const [loading, setLoading] = useState(false);

  const fetchMessage = async () => {
    setLoading(true);
    try {
      const res = await fetch("/api/hello");
      const data = await res.json();
      setMessage(data.message);
    } catch (err) {
      setMessage("Error fetching data 😢");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main
      style={{
        textAlign: "center",
        marginTop: "50px",
        fontFamily: "system-ui, sans-serif",
      }}
    >
      <h1>Simple Button Next.js App</h1>
      <p>{message}</p>
      <button
        onClick={fetchMessage}
        style={{
          padding: "10px 20px",
          fontSize: "16px",
          borderRadius: "8px",
          backgroundColor: "#0070f3",
          color: "white",
          border: "none",
          cursor: "pointer",
          marginTop: "20px",
        }}
      >
        {loading ? "Loading..." : "Fetch Message"}
      </button>
    </main>
  );
}
 
