# Security

## Controls

- Least-privilege IAM per producer and consumer.
- KMS encryption for event data and queues.
- PII classification for event payloads.
- Audit log for event publication and replay.
- Separate accounts for production and non-production.

## Compliance notes

Financial workloads should avoid publishing sensitive raw payloads to broad fanout channels. Publish references or masked fields when possible.
