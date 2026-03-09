import StatusBadge from "./StatusBadge"
import { formatTime } from "../utils/time"

export default function PlayerCard({ player, onDelete }) {

  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 flex justify-between items-center hover:border-orange-500 hover:shadow-lg transition-all">

      <div className="flex flex-col gap-2">

        <div className="text-xl font-semibold">
          {player.nickname}
        </div>

        <StatusBadge status={player.status} />

        {player.last_activity_at && (
          <div className="text-sm text-zinc-400">
            Last activity: {formatTime(player.last_activity_at)}
          </div>
        )}

      </div>

      <button
        onClick={() => onDelete(player.player_id)}
        className="text-red-400 hover:text-red-500 text-sm"
      >
        ✕
      </button>

    </div>
  )
}