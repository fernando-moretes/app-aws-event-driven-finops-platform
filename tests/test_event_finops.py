from event_finops import EventWorkload, recommend_service, estimate_eventbridge_cost, event_contract

def test_recommends_msk_for_high_volume_ordered_stream():
    w = EventWorkload("Transactions", 80_000_000, 4, True, 2, 100)
    assert recommend_service(w).service == "Amazon MSK"

def test_recommends_eventbridge_for_high_fanout_domain_events():
    w = EventWorkload("AccountOpened", 2_000_000, 2, False, 5, 500)
    assert recommend_service(w).service == "Amazon EventBridge"

def test_estimates_eventbridge_cost_per_million_events():
    assert estimate_eventbridge_cost(2_500_000) == 2.5

def test_event_contract_contains_governance_fields():
    c = event_contract("PixPaymentRequested", "1.0", "payments")
    assert "correlationId" in c["requiredFields"]
