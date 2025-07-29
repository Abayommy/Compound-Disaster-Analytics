"""
AI-Powered Compound Disaster Risk Assessment System
Heat Wave and Flood Correlation Analytics for Emergency Management

This package provides tools for emergency managers to monitor, analyze, and respond
to compound disaster events, with a focus on heat wave and flood correlation analytics.

Perfect for monitoring events like the current heat dome affecting 132+ million people.
"""

__version__ = "1.0.0"
__author__ = "Abayomi Ajayi"
__email__ = "ajayi.abayomi5@gmail.com"
__description__ = "AI-Powered Compound Disaster Risk Assessment System"

# Import main classes for easy access
try:
    from .core_analytics import CompoundDisasterAnalytics
    __all__ = ["CompoundDisasterAnalytics"]
except ImportError:
    # Handle case where core_analytics.py doesn't exist yet
    __all__ = []

# Emergency management constants
HEAT_THRESHOLD_TEMP_F = 95.0  # Fahrenheit
HEAT_THRESHOLD_DURATION_DAYS = 3
FLOOD_THRESHOLD_PRECIP_INCHES = 2.0
INFRASTRUCTURE_CRITICAL_THRESHOLD = 1800  # MW

# Risk level constants
RISK_LEVELS = {
    'LOW': (0.0, 0.3),
    'MODERATE': (0.3, 0.6), 
    'HIGH': (0.6, 0.8),
    'EXTREME': (0.8, 1.0)
}

# Current emergency context
CURRENT_HEAT_DOME_INFO = {
    'temperature': 103,  # Current heat dome conditions
    'affected_population': 132_000_000,  # 132+ million people
    'states_affected': 29,
    'emergency_status': 'ACTIVE'
}
