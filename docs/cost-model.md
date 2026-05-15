# Cost Model

## Cost drivers

- Number of events per month.
- Payload size.
- Number of consumers.
- Retention period.
- Replay requirements.
- Cross-account or cross-region delivery.

## Decision guidance

- Prefer SQS for simple point-to-point asynchronous workloads.
- Prefer EventBridge for domain event routing and fanout.
- Prefer Kinesis when ordered stream processing is required.
- Prefer MSK when Kafka compatibility or very high-throughput ordered workloads are mandatory.

## FinOps practice

Every event type should have an estimated monthly volume, retention need and business owner.
