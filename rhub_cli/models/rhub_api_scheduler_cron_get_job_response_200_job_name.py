from enum import Enum


class RhubApiSchedulerCronGetJobResponse200JobName(str, Enum):
    EXAMPLE = "example"
    TOWER_LAUNCH = "tower_launch"
    DELETE_EXPIRED_CLUSTERS = "delete_expired_clusters"

    def __str__(self) -> str:
        return str(self.value)
