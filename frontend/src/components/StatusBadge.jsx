export default function StatusBadge({ status }) {

  const styles = {
    offline: "bg-zinc-700 text-zinc-300",
    searching: "bg-yellow-500/20 text-yellow-400",
    in_match: "bg-green-500/20 text-green-400 animate-pulse",
  }

  const labels = {
    offline: "Offline",
    searching: "Searching match",
    in_match: "In Match",
  }

  return (
    <div className={`inline-block px-3 py-1 rounded-lg text-sm ${styles[status]}`}>
      ● {labels[status] || "Unknown"}
    </div>
  )
}