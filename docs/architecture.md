# Architecture

## Goal

Design a secure, observable and cost-aware event-driven platform for financial-service workloads.

## Core domains

- Accounts
- Payments
- Fraud
- Statements
- Notifications

## Pattern

Domain services publish events to an event backbone. Consumers subscribe based on domain needs. Critical paths use idempotency keys, correlation IDs and dead-letter queues.

## Reliability controls

- DLQs for all asynchronous consumers.
- Idempotency table in DynamoDB.
- Event replay strategy for streams.
- Schema evolution rules.
- Backpressure and throttling alarms.
