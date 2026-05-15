# Observability

## Metrics

- Events published per domain.
- Consumer lag.
- DLQ message count.
- p95 processing latency.
- Cost per event type.

## Tracing

All events carry `correlationId`, `causationId` and `producer` fields.

## Alerts

- DLQ count greater than zero for critical consumers.
- Consumer lag above agreed SLA.
- Unexpected spike in event volume.
