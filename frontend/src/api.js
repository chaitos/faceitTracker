const API = "/api"

export async function getPlayers() {

  const res = await fetch(`${API}/tracked-players/`)

  if (!res.ok) {
    throw new Error("Failed to load players")
  }

  return res.json()
}

export async function addPlayer(query) {

  const res = await fetch(`${API}/tracked-players/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ query })
  })

  if (!res.ok) {
    const err = await res.json()
    throw new Error(err.detail || "Failed to add player")
  }

  return res.json()
}

export async function deletePlayer(playerId) {

  const res = await fetch(`${API}/tracked-players/${playerId}`, {
    method: "DELETE"
  })

  if (!res.ok) {
    throw new Error("Failed to delete player")
  }
}