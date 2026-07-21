export type WebhookEvent = {
  id: string
  receivedAt: string
  type: string
  payload: unknown
}

const events: WebhookEvent[] = []
const MAX = 20

export function recordEvent(type: string, payload: unknown): WebhookEvent {
  const event: WebhookEvent = {
    id: Math.random().toString(36).slice(2, 10),
    receivedAt: new Date().toISOString(),
    type,
    payload,
  }
  events.unshift(event)
  if (events.length > MAX) events.length = MAX
  return event
}

export function listEvents(): WebhookEvent[] {
  return [...events]
}

export function clearEvents(): void {
  events.length = 0
}
