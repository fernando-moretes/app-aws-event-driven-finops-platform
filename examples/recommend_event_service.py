from event_finops import EventWorkload, recommend_service

workload = EventWorkload(
    name="PixPaymentRequested",
    events_per_month=10_000_000,
    payload_kb=3,
    ordering_required=False,
    fanout_consumers=5,
    latency_ms_target=500,
)
print(recommend_service(workload))
