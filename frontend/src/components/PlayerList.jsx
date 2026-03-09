import PlayerCard from "./PlayerCard"

export default function PlayerList({ players, onDelete }) {

  if (!players.length) {
    return (
      <div className="text-zinc-500 text-center mt-10">
        No tracked players yet
      </div>
    )
  }

  return (
    <div className="flex flex-col gap-4">

      {players.map(player => (
        <PlayerCard
          key={player.player_id}
          player={player}
          onDelete={onDelete}
        />
      ))}

    </div>
  )
}