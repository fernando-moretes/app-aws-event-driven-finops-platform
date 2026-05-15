# AWS Event-Driven FinOps Platform

A realistic reference architecture for an event-driven banking platform on AWS, combining domain events, service selection, FinOps, security and observability.

## Scenario

The fictional platform models a banking event mesh with events such as:

- `AccountOpened`
- `PixPaymentRequested`
- `TransactionAuthorized`
- `FraudRiskScored`
- `StatementGenerated`

## AWS services covered

- Amazon EventBridge for domain event routing.
- Amazon SQS for buffering and decoupling.
- Amazon Kinesis Data Streams for ordered streaming.
- Amazon MSK for Kafka-compatible high-volume workloads.
- AWS Lambda and Step Functions for serverless processing.
- DynamoDB for idempotency and event state.
- CloudWatch and X-Ray for observability.

## What makes it portfolio-ready

- Shows real trade-offs between AWS event services.
- Treats cost as an architectural requirement.
- Documents event contracts and ADRs.
- Includes tests for decision logic.
- Uses CI and GitFlow-compatible contribution guidance.

## Run locally

```bash
python -m pip install -e . pytest
pytest -q
```
