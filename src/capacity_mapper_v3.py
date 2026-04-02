"""CapacityMapper for pandemic-preparedness-index v3.

Core module implementing capacity_mapper functionality for the
pandemic preparedness index system.
"""
import logging
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime

logger = logging.getLogger(__name__)


@dataclass
class CapacityMapperConfig:
    """Configuration for capacity_mapper."""
    enabled: bool = True
    batch_size: int = 300
    timeout: int = 30
    max_retries: int = 3


@dataclass
class CapacityMapperResult:
    """Result from capacity_mapper execution."""
    success: bool
    data: List[Dict[str, Any]] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    duration_ms: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


class CapacityMapper:
    """Primary capacity_mapper handler for pandemic-preparedness-index.

    Provides core capacity mapper capabilities including
    batch processing, validation, and result aggregation.
    """

    def __init__(self, config: Optional[CapacityMapperConfig] = None):
        self.config = config or CapacityMapperConfig()
        self._initialized = False
        self._run_count = 0
        self._start_time = datetime.utcnow()

    def initialize(self) -> None:
        if self._initialized:
            return
        logger.info("Initializing capacity_mapper for pandemic-preparedness-index")
        self._initialized = True

    def execute(self, inputs: List[Dict[str, Any]]) -> CapacityMapperResult:
        self.initialize()
        self._run_count += 1
        start = datetime.utcnow()

        results = []
        errors = []

        for batch_start in range(0, len(inputs), self.config.batch_size):
            batch = inputs[batch_start:batch_start + self.config.batch_size]
            for item in batch:
                try:
                    processed = self._process_item(item)
                    if self._validate(processed):
                        results.append(processed)
                except Exception as e:
                    errors.append(f"Item {item.get('id', '?')}: {e}")

        duration = (datetime.utcnow() - start).total_seconds() * 1000

        return CapacityMapperResult(
            success=len(errors) == 0,
            data=results,
            errors=errors,
            duration_ms=duration,
            metadata={
                "run": self._run_count,
                "input_count": len(inputs),
                "output_count": len(results),
                "error_count": len(errors),
            },
        )

    def _process_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        return {
            **item,
            "processed_by": "capacity_mapper",
            "version": 3,
            "timestamp": datetime.utcnow().isoformat(),
        }

    def _validate(self, item: Dict[str, Any]) -> bool:
        return bool(item.get("id")) or bool(item.get("processed_by"))

    @property
    def metrics(self) -> Dict[str, Any]:
        uptime = (datetime.utcnow() - self._start_time).total_seconds()
        return {
            "runs": self._run_count,
            "uptime_s": uptime,
            "initialized": self._initialized,
        }
