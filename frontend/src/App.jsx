import { useEffect, useState } from "react"
import AddPlayer from "./components/AddPlayer"
import PlayerList from "./components/PlayerList"
import PlayerCard from "./components/PlayerCard"

import { getPlayers, addPlayer, deletePlayer } from "./api"

function App() {

  const [players, setPlayers] = useState([])
  const [loading, setLoading] = useState(true)

  async function loadPlayers() {

    try {

      const data = await getPlayers()

      setPlayers(data)

    } catch (err) {

      console.error(err)

    }

    setLoading(false)
  }

  useEffect(() => {

    loadPlayers()

    const interval = setInterval(() => {
      loadPlayers()
    }, 10000)

    return () => clearInterval(interval)

  }, [])

  async function handleAdd(query) {

    const player = await addPlayer(query)

    setPlayers(prev => [player, ...prev])
  }

  async function handleDelete(id) {

    await deletePlayer(id)

    setPlayers(prev =>
      prev.filter(p => p.player_id !== id)
    )
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-black text-white flex items-center justify-center">
        Loading players...
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-black to-zinc-900 text-white">

      <div className="max-w-4xl mx-auto p-10">

        <h1 className="text-5xl font-bold mb-10">
          FACEIT Tracker
        </h1>

        <AddPlayer onAdd={handleAdd} />

        <PlayerList
          players={players}
          onDelete={handleDelete}
        />

      </div>

    </div>
  )
}

export default App