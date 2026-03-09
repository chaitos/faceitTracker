import { useState } from "react"

export default function AddPlayer({ onAdd }) {

  const [query, setQuery] = useState("")
  const [loading, setLoading] = useState(false)

  async function handleSubmit(e) {

    e.preventDefault()

    if (!query) return

    setLoading(true)

    try {

      await onAdd(query)

      setQuery("")

    } catch (err) {

      alert(err.message)

    }

    setLoading(false)
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="flex gap-3 mb-10"
    >

      <input
        className="flex-1 bg-zinc-900 border border-zinc-700 rounded-lg px-4 py-3 text-white outline-none focus:border-orange-500"
        placeholder="FACEIT nickname or profile link"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button
        disabled={loading}
        className="bg-orange-500 hover:bg-orange-600 px-6 py-3 rounded-lg font-semibold transition"
      >
        {loading ? "Adding..." : "Track"}
      </button>

    </form>
  )
}