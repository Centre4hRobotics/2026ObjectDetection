""" Manage Network tables """

import dataclasses
from typing import SupportsInt

import ntcore


@dataclasses.dataclass
class NetworkTables:
    """ Handle Network tables """
    def __init__(self, is_host: bool, team_number=4027) -> None:
        """ Angle (along up axis), bounding box corners """

        nt_instance = ntcore.NetworkTableInstance.getDefault()

        if is_host:
            nt_instance.startServer()
        else:
            nt_instance.setServerTeam(team_number)
            nt_instance.startClient4("visionPi")


        # Set table
        self.table = nt_instance.getTable("Object Detection Vision")

        self.object_count = self.table.getIntegerTopic("Object Count").publish()

        # Bounding box corners
        self.bounding_box_corners = [
            self.table.getIntegerArrayTopic("Bounding Box Corner 1").publish(),
            self.table.getIntegerArrayTopic("Bounding Box Corner 2").publish()
        ]

        # Angle
        self.best_object_angle = self.table.getDoubleTopic("Object Angle").publish()

    def set_values(self, count: int, bounding_box: tuple[list[SupportsInt], list[SupportsInt]], angle: float) -> None:
        """ Write values to network tables """

        self.object_count.set(count)

        self.bounding_box_corners[0].set(bounding_box[0])
        self.bounding_box_corners[1].set(bounding_box[1])

        self.best_object_angle.set(angle)
