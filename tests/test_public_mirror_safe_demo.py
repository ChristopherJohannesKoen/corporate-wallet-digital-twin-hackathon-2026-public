"""Public-mirror smoke tests; no private result is asserted."""

from wallet_twin_v2.fixtures import build_fixture


def test_independent_safe_fixture_executes_all_cells():
    fixture = build_fixture()
    assert len(fixture["clients"]) == 20
    assert len(fixture["opportunities"]) == 100
    assert all(item.entity_id.startswith("D") for item in fixture["opportunities"])
    assert not any(item.evidence_tier.value == "E1" for item in fixture["opportunities"])


def test_safe_fixture_never_claims_measured_share_or_causal_value():
    fixture = build_fixture()
    for item in fixture["opportunities"]:
        assert item.share_interval.claim_class.value == "POSTERIOR"
        assert item.commercial.causal_expected_incremental_value is None
