export function formatTime(timestamp) {

  if (!timestamp) return ""

  const date = new Date(timestamp)
  const now = new Date()

  const diff = Math.floor((now - date) / 1000)

  if (diff < 60) return "just now"

  if (diff < 3600)
    return `${Math.floor(diff / 60)} min ago`

  if (diff < 86400)
    return `${Math.floor(diff / 3600)} h ago`

  return `${Math.floor(diff / 86400)} d ago`
}