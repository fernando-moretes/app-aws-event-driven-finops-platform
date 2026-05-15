from dataclasses import dataclass

@dataclass(frozen=True)
class EventWorkload:
    name: str
    events_per_month: int
    payload_kb: int
    ordering_required: bool
    fanout_consumers: int
    latency_ms_target: int

@dataclass(frozen=True)
class Recommendation:
    service: str
    rationale: str
    risk: str


def recommend_service(workload: EventWorkload) -> Recommendation:
    if workload.ordering_required and workload.events_per_month > 50_000_000:
        return Recommendation("Amazon MSK", "High-volume ordered stream with Kafka ecosystem compatibility.", "medium")
    if workload.ordering_required:
        return Recommendation("Amazon Kinesis Data Streams", "Ordered shard-based stream with managed operations.", "low")
    if workload.fanout_consumers >= 3:
        return Recommendation("Amazon EventBridge", "Many consumers benefit from event routing, schema discovery and decoupling.", "low")
    return Recommendation("Amazon SQS", "Simple queueing pattern with low operational overhead and strong cost profile.", "low")


def estimate_eventbridge_cost(events_per_month: int, price_per_million: float = 1.0) -> float:
    return round(events_per_month / 1_000_000 * price_per_million, 2)


def event_contract(name: str, version: str, source: str) -> dict:
    return {"eventName": name, "version": version, "source": source, "requiredFields": ["id", "time", "detail", "correlationId"]}
