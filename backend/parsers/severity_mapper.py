from backend.normalization.vulnerability_severity import SeverityLevel

def map_severity(severity: str) -> SeverityLevel:
    if not severity:
        return SeverityLevel.UNDEFINED

    mapping = {
        "critical": SeverityLevel.CRITICAL,
        "error":    SeverityLevel.HIGH,
        "high":     SeverityLevel.HIGH,
        "warning":  SeverityLevel.MEDIUM,
        "medium":   SeverityLevel.MEDIUM,
        "low":      SeverityLevel.LOW,
        "info":     SeverityLevel.LOW,
        "style":    SeverityLevel.LOW,
        "performance": SeverityLevel.LOW,
    }

    return mapping.get(severity.lower(), SeverityLevel.UNDEFINED)